from microbit import *

counter = 0

while counter < 10:
    counter = counter + 1
    display.scroll(counter)

"""
while True:
    counter += 1
    display.scroll(counter)
"""

