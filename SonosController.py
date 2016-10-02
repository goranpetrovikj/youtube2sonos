#!/usr/bin/env python
# -*- coding: utf-8 -*-

import soco
import requests

class SonosController:

    def __init__(self):
        self.speakers = soco.discover()
        self.speakers = list(self.speakers)
        if not self.speakers:
            raise Exception('No speakers found')
        for speaker in self.speakers:
            print('Speaker: {}, Volume {}'.format(self.getSpeakerNameAndIp(speaker), speaker.volume))

    def selectSonosSpeaker(self, speakerIpAddress):
        for speaker in self.speakers:
            if speakerIpAddress == speaker.ip_address:
                return speaker
        return None

    def getModelName(self, speaker):
        modelName = 'Unknown'
        try:
            response = requests.get('http://' + str(speaker.ip_address) + ':1400/xml/device_description.xml')
            modelName = response.content.split('<modelName>')[1].split('</modelName>')[0]
            modelName = modelName.strip()
        except Exception as e:
            print e
            pass
        return modelName

    def getSpeakerNameAndIp(self, speaker):
        return speaker.ip_address + ' - ' + self.getModelName(speaker)

    def setSpeakerVolume(self, newVolume):
        print('Setting speakers volume to:', newVolume)
        for speaker in self.speakers:
            speaker.volume = newVolume
            print('Speaker: {}, Volume {}'.format(self.getSpeakerNameAndIp(speaker), speaker.volume))

if __name__ == "__main__":
    sonos = SonosController()
