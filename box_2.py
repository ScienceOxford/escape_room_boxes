from microbit import *

# Please tag us if used!
# We'd love to see what you make:
# @ScienceOxford

def right():
    pin0.write_digital(1)
def wrong():
    pin0.write_digital(0)

display.off()

while True:
    if accelerometer.is_gesture("left"):
        sleep(1000) # the accelerometer doesn't allow us to use the same tactic as the other boxes for checking for a decision
        right()     # so instead, I have added a longer wait time, so you must keep it on the correct side for longer to be sure
    else:
        wrong()
