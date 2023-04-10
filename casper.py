# Companion Artificial Speaking Personal Electronic Robot (C.A.S.P.E.R)

import pyttsx3
import speech_recognition as sr
import wikipedia as wk
import webbrowser as web
from datetime import *
import time
import os

# declaring casper
class Assistant():
    def __init__(self, name, owner, wakeword):
        super().__init__()
        self.name=name
        self.owner=owner
        self.spkr = pyttsx3.init('sapi5')
        self.spkr.setProperty('rate', 160)
        self.hr = datetime.now().hour
        self.mnt = datetime.now().minute

CASPER = Assistant('CASPER', 'Sid', 'casper')

#defining actions

def wish() :
        hr=CASPER.hr%12
        if hr==0 :
            hr=12
        mnt=CASPER.mnt
        if(hr<12 and hr>0) :
            msg=f"Good-morning {CASPER.owner}, {CASPER.name} here, it's {str(hr)}:{str(mnt)} AM"
        elif(hr>=12 and hr<17) :
            msg=f"Good-afternoon {CASPER.owner}, {CASPER.name} here, it's {str(hr)}:{str(mnt)} PM"
        else :
            msg=f"Good-evening {CASPER.owner}, {CASPER.name} here, it's {str(hr)}:{str(mnt)} PM"
        speak(msg)

def speak(msg) :
    for i in msg :
        print(i, end='')
        time.sleep(0.005)
    print('\n')
    CASPER.spkr.say(msg)
    CASPER.spkr.runAndWait()

wish()
