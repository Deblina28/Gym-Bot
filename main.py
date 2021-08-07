# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 18:37:59 2021

@author: Neel
"""

from gtts import gTTS
import os
  
mytext = 'Hello World'
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=True)
myobj.save("welcome.mp3")
os.system("start welcome.mp3")
