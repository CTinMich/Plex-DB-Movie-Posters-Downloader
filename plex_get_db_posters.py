### Change to your Python3 binary location and chmod the file 750 if you want it to be executable with out running it through python command.
#!/home/pi/venv/bin/python3

import requests
import sys
import os
import xml.etree.ElementTree as ET
import argparse
import fnmatch

# Configuration for the Plex server
PLEX_URL = 'http://<PLEX_SERVER_IP>:<PLEX_PORT>'
PLEX_TOKEN = '<PLEX_TOKEN>'
MOVIES_SECTION_ID = '<MOVIES_SECTION_ID>'  # Replace with your movies section ID from Plex
TV_SECTION_ID = '<TV_SECTION_ID>'  # Replace with your TV Shows section ID from Plex
MOVIES_PATH_PREFIX_REAL = '<PATH_TO_MOVIES>'  # Specify the real path prefix for movie files
TV_SHOWS_PATH_PREFIX_REAL = '<PATH_TO_TV_SHOWS>'  # Specify the real path prefix for TV show files

def copy_movie_posters(overwrite=False):
    """
    Copies movie posters from a Plex media server to local directories.
    This function iterates over all movies in the Plex library, fetches the poster images,
    and saves them to the corresponding movie directories.

    Args:
        overwrite (bool): If True, existing poster images will be overwritten.
    """
    url = f'{PLEX_URL}/library/sections/{MOVIES_SECTION_ID}/all'
    headers = {'X-Plex-Token': PLEX_TOKEN}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        root = ET.fromstring(response.content)
        for video in root.findall('.//Video'):
            poster_url = video.attrib.get('thumb')
            if poster_url:
                poster_url = f'{PLEX_URL}{poster_url}'
                part = video.find('.//Part')
                file_path = part.attrib.get('file')
                if file_path:
                    movie_folder_name = os.path.basename(os.path.dirname(file_path))
                    full_poster_path = os.path.join(MOVIES_PATH_PREFIX_REAL, movie_folder_name, "poster.jpg")

                    if not os.path.exists(full_poster_path) or overwrite:
                        response = requests.get(poster_url, headers=headers)
                        if response.status_code == 200:
                            os.makedirs(os.path.dirname(full_poster_path), exist_ok=True)
                            with open(full_poster_path, 'wb') as f:
                                f.write(response.content)
                            print(f'Writing  {full_poster_path}')
                    else:
                        print(f'Skipping {full_poster_path}, already exists.')

def sanitize_title(title):
    """
    Sanitizes the title of a TV show by replacing certain characters with alternatives.
    
    Args:
        title (str): The title to sanitize.

    Returns:
        str: The sanitized title.
    """
    return title.replace(':', ' -').replace('?', '')

def copy_tv_show_posters(overwrite=False):
    """
    Copies TV show posters from a Plex media server to local directories.
    This function iterates over all TV shows in the Plex library, fetches the poster images,
    and saves them to the corresponding TV show directories.

    Args:
        overwrite (bool): If True, existing poster images will be overwritten.
    """
    url = f'{PLEX_URL}/library/sections/{TV_SECTION_ID}/all'
    headers = {'X-Plex-Token': PLEX_TOKEN}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        root = ET.fromstring(response.content)
        for directory in root.findall('.//Directory'):
            poster_url = directory.attrib.get('thumb')
            if poster_url:
                poster_url = f'{PLEX_URL}{poster_url}'
                title = directory.attrib.get('title')
                if title:
                    sanitized_title = sanitize_title(title)
                    search_pattern = f"{sanitized_title} {{*}}"
                    matching_folders = [folder for folder in os.listdir(TV_SHOWS_PATH_PREFIX_REAL)
                                        if fnmatch.fnmatch(folder, search_pattern)]
                    if len(matching_folders) == 1:
                        folder_path = os.path.join(TV_SHOWS_PATH_PREFIX_REAL, matching_folders[0], "poster.jpg")
                        if not os.path.exists(folder_path) or overwrite:
                            response = requests.get(poster_url, headers=headers)
                            if response.status_code == 200:
                                os.makedirs(os.path.dirname(folder_path), exist_ok=True)
                                with open(folder_path, 'wb') as f:
                                    f.write(response.content)
                                print(f'Writing  {folder_path}')
                        else:
                            print(f'Skipping {folder_path}, already exists.')
                    elif len(matching_folders) > 1:
                        print(f'Error: Multiple matching folders for "{title}" found: {", ".join(matching_folders)}')
                    else:
                        print(f'No matching folder found for "{title}".')

def main():
    """
    Main function to parse command line arguments and trigger
    It allows users to select between copying movie posters, TV show posters, or both, and to choose whether to overwrite existing files.
    """
    parser = argparse.ArgumentParser(description='Copy posters from Plex.')
    parser.add_argument('-m', '--movies', action='store_true', help='Copy movie posters')
    parser.add_argument('-t', '--tv', action='store_true', help='Copy TV show posters')
    parser.add_argument('-o', '--overwrite', action='store_true', help='Overwrite existing poster.jpg files')

    args = parser.parse_args()

    if not args.movies and not args.tv:
        print("No option specified. Use '-m' to copy movie posters or '-t' to copy TV show posters.")
    else:
        if args.movies:
            copy_movie_posters(overwrite=args.overwrite)
        if args.tv:
            copy_tv_show_posters(overwrite=args.overwrite)

if __name__ == "__main__":
    main()
