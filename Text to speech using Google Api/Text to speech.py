# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 19:20:25 2020

@author: deep
"""

from gtts import gTTS
import os

mytext = 'Hello This is deep'
language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False) 
myobj.save("welcome.mp3") 
os.system("welcome.mp3") 