import speech_recognition as sr 
import webbrowser as wb
from text_to_speech_custom import textToSpeech

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

r = sr.Recognizer()

text2 = ''

while text2!='terminate':
	with sr.Microphone() as source:
		print ('Say Something!')
		audio = r.listen(source)
		print ('Done!')
	 
	try:
		text = r.recognize_google(audio)
		text2 = text
		print('Your command:\n' + text)
		lang = 'en'
		

		textToSpeech(text, lang)

		#f_text = 'https://www.google.co.in/search?q=' + text
		#wb.get(chrome_path).open(f_text)
	 
	except Exception as e:
		print (e)