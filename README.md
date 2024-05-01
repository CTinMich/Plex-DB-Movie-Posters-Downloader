
# Plex-DB-Covers-Downloader

Linux Python Script to download the covers stored in your Plex DB and store them as "poster.jpg" files in your movie library folders.


# LICENSE

Creative Commons Attribution-NonCommercial 4.0 International License.

This work is licensed under a Creative Commons Attribution-NonCommercial 4.0 International License.


# Python Requirements

Python v3.6 or greater.

Python "Requests" library 
    
    pip install -r requirements.txt or 
    pip install requests).


# Documentation

I just wrote this short Linux based python script and sharing it to anyone else that may find it useful.

I wrote this script after I had to re-add my Plex Movies and TV libraries and realized I lost a lot of my fixed/custom poster art for my Movies/TVs.

This script will look up what posters you currently have configured in your Plex DB and will save a copy of it as "poster.jpg" in each appropriate folder location. ***This does expect you are following the standard that each movie/show is in its own folder.

You can then update your Plex library Movie library config to use "Use local assets " and then when you run a media library scan it will now use those posters first if you have to reload in the future.

Other things to take in consideration:

1) I run Plex in Linux Docker Container
2) The Script can find the exact Movie folder path, but there was challenges in trying to find TV Show paths using the API so I fusged it a little to assume the folder matches the show "title" with a {xxxxx} after it for {tmdb-xxxx} string to help assure it found the correct folder path.  If anyone know how to get the physical paths for TV Shows using the API please send me a note!
3) My pathing:
   Physical Movies = "/home/pi/usbhdd/Media/Movies"  - Docker mapping sees it as "/Media/Movies"
   Physical TV Shows = "/home/pi/usbhdd-02/Media/'TV Shows'" - Docker mapping sees it as "/Media/'TV Shows'"
4) My file naming patterns:
   Movies = "/home/pi/usbhdd/Media/Movies/{MOVIE} {{tmdb-xxxxx}}"
   TV = "/home/pi/usbhdd-02/Media/'TV Shows'/{TV SHOW} {{tvdb-xxxx}}/{SEASON}"

I made no effort to make this work on Windows, but it can be used as a reference to those that want to go that route.

Because I use docker... Plex's library does not have the "complete" path to my ext movie folders, so I have a path prefix variable in there to tack on the missing path pieces. If you do not use docker I think this script will still work, you just need to "blank out" the variable value.
Variables:

    PLEX_URL = 'http://<PLEX_SERVER_IP>:<PLEX_PORT>'
    PLEX_TOKEN = '<PLEX_TOKEN>'
    MOVIES_SECTION_ID = '<MOVIES_SECTION_ID>'  # Replace with your movies section ID from Plex
    TV_SECTION_ID = '<TV_SECTION_ID>'  # Replace with your TV Shows section ID from Plex
    MOVIES_PATH_PREFIX_REAL = '<PATH_TO_MOVIES>'  # Specify the real path prefix for movie files
    TV_SHOWS_PATH_PREFIX_REAL = '<PATH_TO_TV_SHOWS>'  # Specify the real path prefix for TV show files


If you do not know your Plex token the easiest way to do this is use the "Get Info" option on one of your movies.  In the Media Info box at the bottom click on the "view xml".  This will open the XML data in a browser.  The token can be seen at the end of the URL address line right after "Plex-Token="

[Documentation](https://linktodocumentation)
