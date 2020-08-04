"""
from CrawlerForJokes import *
from CrawlerForLyrics import *
from FaceAPI import *
from SpeechAndText import *
from TelegramBot_handler import *
from YoutubeAPI import *
"""

import CrawlerForJokes
import CrawlerForLyrics
import FaceAPI
import SpeechAndText
import TelegramBot_handler
import YoutubeAPI

#FaceAPI.face_attributes()

#SpeechAndText.speechToText()
#SpeechAndText.textToSpeech(text=)

def check_cred(id):
    import cx_Oracle
    con = cx_Oracle.connect("SAZAN_1", "hr", 'localhost/orcl')
    cur = con.cursor()
    query = 'select * from users where profile_pic_id = %s'%(id)
    cur.execute(query)
    len_ = 0
    for result in cur:
        len_+=1
    cur.close()
    con.close()
    print(len_)
    if len_ == 0:
        return False
    return True

def register(id):
    import cx_Oracle
    con = cx_Oracle.connect("SAZAN_1", "hr", 'localhost/orcl')
    cur = con.cursor()
    cur.execute('''insert into users(username, password, email, first_name, last_name, gender, 
                    date_of_birth, nationality, relationship_status, language, occupation, education_current,
                    profile_pic_id, account_state, online_check)
                    values('--','--','--','--','--','--','--','--','--','--','--','--', %s,'active','offline')''',[id])

#TelegramBot_handler.recheck_until()

