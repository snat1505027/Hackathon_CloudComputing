from gtts import gTTS
import pyglet
import time, os

def textToSpeech(t, l):
	f = gTTS(text = t, lang = l)
	fname = 'temp.mp3'
	f.save(fname)
	
	music = pyglet.media.load(fname)
	music.play()
	time.sleep(music.duration)
	
	
	
