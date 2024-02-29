
# Plex-DB-Covers-Downloader

Linux Python Script to download the covers stored in your Plex DB and store them as "poster.jpg" files in your movie library folders.


## Documentation

I wrote this script after I had to re-add my Plex movies libraries and realized I lost a lot of my fixed/custom poster art for my movies.  

When you have your Plex library setup the way you like it, this script when ran, will download the covers you have stored into you Plex movie DB into the individual movies folders as "poster.jpg" files.  Then modify your Movie library to use "Local Artwork when present" and then when you run a media library can it will now use those posters first if you have to reload.

This script was designed around Plex running on Linux as a Docker Container.  It will not work as is if you are using a Windows based Plex server.  It will "probably" (not tested) work on non-Docker Linux setup if you blank out the "MOVIES_PATH_PREFIX_REAL" variable seeing that your Plex should see the full true path to your Movies library.

Variables:

    PLEX_URL = 'http://{IP or FQDN}:32400'

    PLEX_TOKEN = 'xxxxxxxxxxxxxxxx' # Replace with you Plex token
    
    MOVIES_SECTION_ID = '1' # Replace with your movies section ID
    
    MOVIES_PATH_PREFIX_REAL = '/home/pi/usbhdd'  # Specify the real path prefix for movie files

If you do not know your Plex token the easiest way to do this is use the "Get Info" option on one of your movies.  In the Media Info box at the bottom click on the "view xml".  This will open the XML data in a browser.  The token can be seen at the end of the URL address line right after "Plex-Token="

[Documentation](https://linktodocumentation)
