import speech_recognition as sr 
import webbrowser as wb
from text_to_speech_custom import tts

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
		

		tts(text,lang)
		if(text=="left"):
			print("sending.. "+text+":"+str(1))
		elif(text=="right"):
			print("sending.. "+text+":"+str(2))
		elif(text=="front"):
			print("sending.. "+text+":"+str(3))
		elif(text=="back"):
			print("sending.. "+text+":"+str(4))
		else:
			print("please insert a correct command.")
		
	except Exception as e:
		print (e)