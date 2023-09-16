#count_to_ten.py

from microbit import *

for counter in range(1,11):
    display.scroll(counter)

display.scroll("All Done!")