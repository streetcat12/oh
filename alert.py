import datetime

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

db_url = 'https://onlinehelper-62a05.firebaseio.com/'
cred = credentials.Certificate("C:/Users/pinok/PycharmProjects/oh/onlinehelper-62a05-firebase-adminsdk-vdifv-f27e94e1f4.json")
default_app = firebase_admin.initialize_app(cred, {'databaseURL':db_url})

def save(x,y):
    ref = db.reference()
    try:
        if x.startswith("(") and ")" in x:
            if "<시간표>" in x:
                if int(x.split(">")[1].split(":")[0]) >= 0 and int(x.split(">")[1].split(":")[0]) <= 24 and int(x.split(">")[1].split(":")[1]) >= 0 and int(x.split(">")[1].split(":")[1]) <= 59:
                    ref.update({x.split("<")[0]+x.split("> ")[1].split(":")[0]+":"+x.split("> ")[1].split(":")[1]:y})
    except:
        pass