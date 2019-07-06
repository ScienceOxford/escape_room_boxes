from microbit import *
import radio

# Please tag us if used!
# We'd love to see what you make:
# @ScienceOxford

radio.on()
radio.config(channel=7) #change 7 to a different number between 0-100

box0 = False
box1 = False
box2 = False
box3 = False

while True:
    message = radio.receive()
    if message == 'box0':
        box0 = True
    if message == 'box1':
        box1 = True
    
    
    if box0 == True:
        display.set_pixel(0, 4, 9)
    if box 1 == True:
        display.set_pixel(4, 4, 9)
