from microbit import *

# Please tag us if used!
# We'd love to see what you make:
# @ScienceOxford

def right():
    pin0.write_digital(1)
def wrong():
    pin0.write_digital(0)

while True:
    if accelerometer.is_gesture("down"):
        sleep(500)
        right()
    else:
        wrong()
