from microbit import *

# Please tag us if used!
# We'd love to see what you make:
# @ScienceOxford

def right():
    pin0.write_digital(1)
def wrong():
    pin0.write_digital(0)

correct = False

while True:
    print(correct)
    if accelerometer.is_gesture("left"):
        sleep(500)
        correct = True
    if accelerometer.is_gesture('face up') and correct == True:
        right()
    else:
        wrong()
