def speechToText():
	import speech_recognition as sr
	#import webbrowser as wb
	#import speak

	chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

	r = sr.Recognizer()

	text2 = ''
	while text2!='terminate':
		with sr.Microphone() as source:     # mention source it will be either Microphone or audio files.
			print("Speak Anything :")
			audio = r.listen(source, timeout=2, phrase_time_limit=3, snowboy_configuration=None)        # listen to the source
			print('Done.')
			try:
				text = r.recognize_google(audio)    # use recognizer to convert our audio into text part.
				print("You said : {}".format(text))
			except:
				print("Sorry could not recognize your voice")  
def textToSpeech(text):
	import pyttsx3
	engine = pyttsx3.init()
	engine.say(text)
	engine.runAndWait()