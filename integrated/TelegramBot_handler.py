import json
import requests
import urllib.request
import telegram
from random import random, randint

import FaceAPI
import YoutubeAPI
import SpeechAndText
import CrawlerForLyrics
import CrawlerForJokes
import UserAssist
#from Bot2 import *

TOKEN = "791156268:AAGX1D98KLqXw_LPvbcQYHzquOJO5PBdg1M"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)
DOWNLOAD_URL = "https://api.telegram.org/file/bot{}/".format(TOKEN)
Bot = telegram.Bot(TOKEN)

#english_bot = training()

def runner_(bot=Bot, max_=5):
    max_ = 1000
    old_updates = 0
    for i in range(max_):
        #sleep(10)
        check=bot.get_updates()
        while not check:
            # chat_id = bot.get_updates()[-1].message.chat_id
            print('stuck..')
        #print(check)
        json=get_updates()
        num_updates = len(json["result"])
        last_update = num_updates - 1
        """if num_updates == old_updates:
            print(num_updates)
            print(old_updates)
            print("No new json received.")
            continue"""
        old_updates = num_updates
        while last_update!=old_updates-1:
            print(json["result"][last_update])
            user_id = json["result"][last_update]["message"]["from"]["id"]
            if not UserAssist.check_cred(user_id):
                send_message("Please register in our site: ",user_id)
                continue
            # print(updates["result"][last_update]["message"])
            if "text" in json["result"][last_update]["message"]:
                text_id = json["result"][last_update]["message"]["text"]
                text, chat_id = get_last_chat_id_and_text(get_updates())
                #send_message(text, chat_id)
                if("show lyrics" in text):
                    title, artist, link, lyrics = CrawlerForLyrics.find_lyrics_title_artist(text.replace("show lyrics ",""), base_artist=None)
                    send_message("Here is the lyric of the song: "+title+"\nBy "+artist, chat_id)
                    send_message(lyrics, chat_id)
                else:
                    #res = str(english_bot.get_response(text))
                    send_message(res, chat_id)
            elif "voice" in json["result"][last_update]["message"]:
                voice_id = json["result"][last_update]["message"]["voice"]
                voice_id, chat_id = get_last_chat_id_and_audio(get_updates())
                send_audio(voice_id, chat_id)
                download_audio(voice_id,chat_id=chat_id)
                text = SpeechAndText.speechToText()
                if text == "":
                    send_message("Sorry I couldn't hear that!", chat_id=chat_id)
                print("Recognized:: ", text)
                #reply_text = generate_reply(text)
                #send_message(reply_text)
                #res = str(english_bot.get_response(text))
                #send_message(res,chat_id)
                SpeechAndText.textToSpeech(text)
                send_my_aud(chat_id)

                #received.oga
            elif "photo" in json["result"][last_update]["message"] or "document" in json["result"][last_update]["message"]:
                try:
                    photo_id = json["result"][last_update]["message"]["photo"][0]["file_id"]
                    # print(file_id)
                except:
                    photo_id = json["result"][last_update]["message"]["document"]["file_id"]
                    # pass
                photo_id, chat_id = get_last_chat_id_and_image(get_updates())
                #send_image(photo_id, chat_id)
                download_image(photo_id,chat_id=chat_id)
                #face_emo.jpg
                attr = FaceAPI.face_attributes()
                smileOrNot = attr['smile']
                for key in attr['emotion']:
                    print(key," ",attr['emotion'][key])
                opt = max(attr['emotion'], key=attr['emotion'].get)
                print(opt)
                songs = YoutubeAPI.youtube_search_by_word(option=opt, maxR=5)
                for song in songs:
                    send_message(song, chat_id)
                    send_message(songs[song], chat_id)
                print('Sent song suggestions.')
                if(smileOrNot<.5 or attr['emotion']['sadness']>.5):
                    print("saddy")
                    #if randint(0,1000)%2==0:
                    print("joke")
                    send_message("May be a joke will cheer you up!!", chat_id)
                    joke = CrawlerForJokes.extractJoke()
                    send_message(joke, chat_id)
                #else:
                    print("meme")
                    send_message("May be a meme will cheer you up!!", chat_id)
                    meme = CrawlerForJokes.extractMeme()
                    send_message(meme, chat_id)
            last_update-=1



#FaceAPI.face_attributes()

#SpeechAndText.speechToText()
#SpeechAndText.textToSpeech(text=)


def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates():
    url = URL + "getUpdates"
    js = get_json_from_url(url)
    return js


def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    # print(updates["result"][last_update]["message"])
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)


def send_message(text, chat_id):
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)


def get_last_chat_id_and_audio(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    # print(updates["result"][last_update]["message"])
    file_id = updates["result"][last_update]["message"]["voice"]["file_id"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (file_id, chat_id)


def download_audio(file_id, chat_id=None):
    # print(file_id)
    url = URL + "getFile?file_id={}".format(file_id)
    json = get_json_from_url(url)
    # print(json)
    result_json = json['result']
    download_url = DOWNLOAD_URL + result_json['file_path']
    print(download_url)
    response = urllib.request.urlretrieve(download_url, "received.oga")
    # print(get_url(download_url))
    print('downloaded ', result_json['file_path'])


def send_audio(voice_id, chat_id):
    url = URL + "sendVoice?voice={}&chat_id={}".format(voice_id, chat_id)
    get_url(url)


def get_last_chat_id_and_image(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    # print(updates["result"][last_update]["message"])
    try:
        file_id = updates["result"][last_update]["message"]["photo"][0]["file_id"]
        # print(file_id)
    except:
        file_id = updates["result"][last_update]["message"]["document"]["file_id"]
        # pass
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (file_id, chat_id)


def download_image(file_id, chat_id=None):
    # print(file_id)
    url = URL + "getFile?file_id={}".format(file_id)
    json = get_json_from_url(url)
    # print(json)
    result_json = json['result']
    download_url = DOWNLOAD_URL + result_json['file_path']
    print(download_url)
    response = urllib.request.urlretrieve(download_url, "face_emo.jpg")
    # print(get_url(download_url))
    print('downloaded ', result_json['file_path'])


def send_image(photo_id, chat_id):
    url = URL + "sendphoto?photo={}&chat_id={}".format(photo_id, chat_id)
    get_url(url)


"""text, chat_id = get_last_chat_id_and_text(get_updates())
send_message(text, chat_id)"""
# download_audio(get_last_chat_id_and_audio(get_updates())[0])
# voice_id, chat_id = get_last_chat_id_and_audio(get_updates())
# send_audio(voice_id, chat_id)
# voice_id, chat_id = get_last_chat_id_and_image(get_updates())
# send_image(voice_id, chat_id)
# download_image(get_last_chat_id_and_image(get_updates())[0])

def send_pic(remote_id,bot=Bot):
    print(bot.get_me())
    bot.send_photo(remote_id, photo=open('CONSTANT_PIC.png', 'rb'))


def send_my_aud(remote_id,bot=Bot):
#    bot = telegram.Bot(TOKEN)
    #print(bot.get_me())
    bot.send_audio(remote_id, audio=open('CONSTANT_AUDIO.mp3', 'rb'))

