# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 18:37:59 2021

@author: Neel
"""

from gtts import gTTS
from time import sleep
import os
import serial

serial_push = serial.Serial("COM4", 115200, 8, serial.PARITY_NONE, serial.STOPBITS_ONE)
serial_push.flushInput()

init = 'Hey there, I am Gym Bot, your personalized Gym Assistant! Let us begin with the first work out of the day. 5, 4, 3, 2, 1, Start running!'
language = 'en'
myobj = gTTS(text=init, lang=language, slow=True)
myobj.save("welcome.mp3")
os.system("start welcome.mp3")

sleep(20)

mid = '10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0. Now we can start with push ups!'
print('here')
midvoice = gTTS(text=mid, lang=language, slow=True)
midvoice.save("mid.mp3")
os.system("start mid.mp3")

sleep(15)

os.system("start music.mp3")

sleep(25)

mid2 = '5, 4, 3, 2, 1, 0. Let us get back to running!'
print('here')
midvoice2 = gTTS(text=mid2, lang=language, slow=True)
midvoice2.save("mid2.mp3")
os.system("start mid2.mp3")

sleep(15)

iterate = 0
decoded_bytes = 0

    try:
        serial_push.write(bytes("4", "utf-8"))
        decoded_bytes=serial_push.readline().decode('Ascii')
        print(decoded_bytes)
    except:
        print('error')  

final = 'Concluding this workout, you were able to finish up' + str(decoded_bytes) + ' push ups in the whole session! Thank you for using Gym Bot!'
print('here')
finalvoice = gTTS(text=final, lang=language, slow=True)
finalvoice.save("final.mp3")
os.system("start final.mp3")

serial_push.close()
