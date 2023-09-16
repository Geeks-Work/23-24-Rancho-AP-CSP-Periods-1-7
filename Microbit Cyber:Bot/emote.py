# emote.py

from microbit import *
 
def emote(feeling):
    if feeling == "happy":
        display.show(Image.HAPPY)
    elif feeling == "sad":
        display.show(Image.SAD)
    else:
        display.scroll("I don't understand that feeling. Try happy or sad.")
    sleep(2000)

emote("happy")