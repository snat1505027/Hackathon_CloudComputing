def speechToText():
    import cloudconvert
    api = cloudconvert.Api('dNjRGRXdyfWenzq21X1zRYbM3aFXGMF30udg3zTqxe7vYy0i9eO0rdx5fAdCjUNH')

    process = api.convert({
        "inputformat": "oga",
        "outputformat": "wav",
        "input": "upload",
        "file": open('received.oga', 'rb')
    })
    process.wait()
    process.download()

    import speech_recognition as sr
    from pydub import AudioSegment
    r = sr.Recognizer()
    # x=AudioSegment.from_file("received.oga", format='oga')
    # x.export("received.wav", format="wav")
    with sr.AudioFile(('received.wav')) as source:
        audio = r.record(source)
        #print(audio)
    try:
        text = r.recognize_google(audio)  # use recognizer to convert our audio into text part.
        print("You said : {}".format(text))
        return text
    except:
        print("Sorry could not recognize your voice")
        return ""

def textToSpeech(text):
    """import pyttsx3
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    #engine."""
    # Import the required module for text
    # to speech conversion
    from gtts import gTTS

    # This module is imported so that we can
    # play the converted audio
    import os

    # The text that you want to convert to audio
    mytext = 'Welcome to geeksforgeeks!'

    # Language in which you want to convert
    language = 'en'

    # Passing the text and language to the engine,
    # here we have marked slow=False. Which tells
    # the module that the converted audio should
    # have a high speed
    myobj = gTTS(text=mytext, lang=language, slow=False)

    # Saving the converted audio in a mp3 file named
    # welcome
    myobj.save("CONSTANT_AUDIO.mp3")

    # Playing the converted file
    #os.system("mpg321 welcome.mp3")

