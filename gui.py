#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
from playYoutube import playSong

root = Tk() #main window
root.title('Youtube 2 Sonos')
root.resizable(width=False, height=False)

def Play():
	txt = url.get()
	if txt.startswith('http'):
		playSong(txt)

url = Entry(root, width=60, text = 'Enter video url')
url.bind('<Return>', lambda event: Play())
button = Button(root, text = 'Play', command = Play)
url.pack()
button.pack()

url.focus_set()

root.mainloop()
