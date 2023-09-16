#simple_decision.py

from microbit import *

a = 89
b = 42
if a > b:
    display.scroll("a is greater than b")
else:
    display.scroll("a is not greater than b")