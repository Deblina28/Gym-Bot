# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 18:37:59 2021

@author: Neel
"""

from gtts import gTTS
import os
  
mytext = 'Hey there, I am Gym Bot, your personalized Gym Assistant! Let us begin with the first work out of the day. 5, 4, 3, 2, 1, Start running!'
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=True)
myobj.save("welcome.mp3")
os.system("start welcome.mp3")
