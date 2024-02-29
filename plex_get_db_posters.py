### Change to your Python3 binary location and chmod the file 750 if you want it to be executable with out running it through python command.
#!/home/pi/venv/bin/python3

import requests
import os
import xml.etree.ElementTree as ET

# Plex server configuration
PLEX_URL = 'http://{IP or FQDN}:32400'  ### Replace with your Plex Server IP or FQDN
PLEX_TOKEN = 'YourPrivatePlexToken'  ### Replace with your Plex token
MOVIES_SECTION_ID = '1' # Replace with your movies section ID
MOVIES_PATH_PREFIX_REAL = '/home/pi/usbhdd'  # Specify the real path prefix for movie files (needed if Dockerized and Plex does not see the full external Library path).  Blank it out if non-Docker build.

# Function to copy posters for movies
def copy_movie_posters():
    # URL for Plex movies library
    url = f'{PLEX_URL}/library/sections/{MOVIES_SECTION_ID}/all'
    headers = {'X-Plex-Token': PLEX_TOKEN}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        root = ET.fromstring(response.content)
        for video in root.findall('.//Video'):
            poster_url = video.attrib.get('thumb')
            if poster_url:
                poster_url = f'{PLEX_URL}{poster_url}'  # Construct absolute URL
                part = video.find('.//Part')
                file_path = part.attrib.get('file')
                if file_path:
                    parent_folder_path = os.path.dirname(file_path)
                    poster_filename = "poster.jpg"  # Set poster filename to "poster.jpg"
                    poster_path = os.path.join(parent_folder_path, poster_filename)
                    # Download the poster image with authentication headers
                    response = requests.get(poster_url, headers=headers)
                    if response.status_code == 200:
                        print(f'{MOVIES_PATH_PREFIX_REAL}{poster_path}')
                        with open(f'{MOVIES_PATH_PREFIX_REAL}{poster_path}', 'wb') as f:
                            f.write(response.content)
                            print(f"Poster saved for movie: {os.path.basename(parent_folder_path)}\n")

# Execute the function
copy_movie_posters()
