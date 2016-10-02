#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import glob
import socket
from subprocess import call
from SonosController import SonosController

HOSTNAME = socket.getfqdn()

scriptDir = os.path.dirname(os.path.realpath(__file__))
sambaDirLocal = '/srv/music/sonos2youtube'
sambaDirPublic = '/music/sonos2youtube'

def getPublicSongUri(songFilename):
	songName = os.path.split(songFilename)[-1]
	songSambaPath = os.path.join(sambaDirPublic, songName)
	songUri = 'x-file-cifs://' + HOSTNAME + songSambaPath
	return songUri

def extractSongAudio(videoUrl):
	if not os.path.isdir(sambaDirLocal):
		print 'The directory "{}" does not exits. Creating...'.format(sambaDirLocal)
		os.makedirs(sambaDirLocal)

	oldMp3s = glob.glob(os.path.join(sambaDirLocal, '*.mp3'))
	oldWebms = glob.glob(os.path.join(sambaDirLocal, '*.webm'))
	for fname in oldMp3s:
		os.remove(fname)
	for fname in oldWebms:
		os.remove(fname)

	print 'Extracting:', videoUrl
	command = "youtube-dl  --no-warnings --extract-audio --audio-format mp3 -l " + videoUrl
	call(command.split(), cwd=sambaDirLocal)

	songFilename = glob.glob(os.path.join(sambaDirLocal, '*.mp3'))[0]
	return songFilename

def playSong(videoUrl):
	sonos = SonosController()
	songFilename = extractSongAudio(videoUrl)
	sonos.speaker = sonos.selectSonosSpeaker(sonos.speakers[0].ip_address)
	sonos.speaker.stop()
	songUri = getPublicSongUri(songFilename)
	sonos.speaker.play_uri(songUri)

def playPlaylist(playlistUrl):
	raise NotImplementedError()

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print 'Please specify video'
		exit()
	mediaSourceUrl = sys.argv[1]
	if mediaSourceUrl.startswith('https://www.youtube.com/watch?v='):
		playSong(mediaSourceUrl)
	elif mediaSourceUrl.startswith('https://www.youtube.com/playlist?list='):
		playPlaylist(mediaSourceUrl)
	else:
		print 'Unsupported media source'
