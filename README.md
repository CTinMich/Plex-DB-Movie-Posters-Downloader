
# Plex-DB-Covers-Downloader

Linux Python Script to download the covers stored in your Plex DB and store them as "poster.jpg" files in your movie library folders.


# LICENSE

Creative Commons Attribution-NonCommercial 4.0 International License.

This work is licensed under a Creative Commons Attribution-NonCommercial 4.0 International License.


# Python Requirements

Python v3.6 or greator.

Python "Requests" library (pip install -r requirements.txt or pip install requests).


# Documentation

I just wrote this short Linux based python script and sharing it to anyone else that may find it useful.

I wrote this script after I had to re-add my Plex movies libraries and realized I lost a lot of my fixed/custom poster art for my movies.

This script will look up what posters you currently have configured in your Plex DB and will save a copy of it as "poster.jpg" in each appropriate movie folder location. ***This does expect you are following the standard that each movie is in its own folder.

You can then update your Plex library Movie library config to use "Use local assets " and then when you run a media library scan it will now use those posters first if you have to reload in the future.

Other things to take in consideration:

I run Plex in Linux Docker Container

I made no effort to make this work on Windows, but it can be used as a reference to those that want to go that route.

Because I use docker... Plex's library does not have the "complete" path to my ext movie folders, so I have a path prefix variable in there to tack on the missing path pieces. If you do not use docker I think this script will still work, you just need to "blank out" the variable value.
Variables:

    PLEX_URL = 'http://{IP or FQDN}:32400'

    PLEX_TOKEN = 'xxxxxxxxxxxxxxxx' # Replace with you Plex token
    
    MOVIES_SECTION_ID = '1' # Replace with your movies section ID
    
    MOVIES_PATH_PREFIX_REAL = '/home/pi/usbhdd'  # Specify the real path prefix for movie files

If you do not know your Plex token the easiest way to do this is use the "Get Info" option on one of your movies.  In the Media Info box at the bottom click on the "view xml".  This will open the XML data in a browser.  The token can be seen at the end of the URL address line right after "Plex-Token="

[Documentation](https://linktodocumentation)
