# Plex-DB-Covers-Downloader
Python Script to download the covers stored in your Plex DB and store them as "poster.jpg" files in the movie folders.

Creative Commons Attribution-NonCommercial 4.0 International License
This work is licensed under a Creative Commons Attribution-NonCommercial 4.0 International License.

I wrote this script after I had to re-add my Plex Movies libraries and realized I lost a lot of my fixed/custom poster art for my movies.  When you have your Plex library setup the way you like it, this script when ran will download the covers you have stored into you Plex movie DB into the individual movies folders as "poster.jpg" files.  If you then have you Movies library configured to us "Local Artwork" and you run a Media Scan it will now use thos posters first if you have to reload.

This script was setup for my Plex config which is a Linux Docker container whose physical movies library location is "/home/pi/usbhdd/Media/Movies/{Movies Folders}".  If you do not use a Docker Container and Plex see the full true path to your library you will need to blank out the  "MOVIES_PATH_PREFIX_REAL" variable to remove that prefix to the Library path.

Other Variable that will (or may need to) be adjusted are the:
  # Plex server configuration
  PLEX_URL = 'http://{IP or FQDN}:32400'
  PLEX_TOKEN = 'xxxxxxxxxxx' # To get your token do a XML view on one of your movies and in the URL address look at the very end for a "token=" string.
  MOVIES_SECTION_ID = '1' # Replace with your movies section ID
  MOVIES_PATH_PREFIX_REAL = '/home/pi/usbhdd'  # Specify the real path prefix for movie files
