# Play Youtube audio to Sonos

Use this Python app to play Youtube audio on your Sonos speaker.

Working principle:
- grab the audio for the specified video link
- store it on a local shared network location
- instruct the Sonos speaker to play music from a local network storage

## Usage

Use it over the command line:

    python playYoutube.py https://www.youtube.com/watch?v=xxx

Use the gui:

    python gui.py

## Installation

The app relies on multiple libraries, the most important being:
- [youtube-dl](https://github.com/rg3/youtube-dl)
- [SoCo](https://github.com/SoCo/SoCo)

To install them all, execute the command below.

    sudo ./requirementsInstall.sh

## Create samba share

Create a network share via SAMBA.
The app requires that following path is used:

    /srv/music/youtube2sonos

## Create application shortcut

Create an application shortcut in Xubuntu:
- edit the file icon/youtube2sonos.desktop, by setting up the paths of the icon and the executable
- copy the file youtube2sonos.desktop to /usr/share/applications/

## Limitations

The music will be played on the first speaker the app finds.
