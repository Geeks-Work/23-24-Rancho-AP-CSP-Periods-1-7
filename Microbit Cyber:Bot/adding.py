# adding.py

from microbit import *

def add_one(value):
    value = value + 1
    return value
    
def addTogether(value1, value2):
    result = value1 + value2
    return result
    
display.scroll(add_one(5))
display.scroll(addTogether(5,6))