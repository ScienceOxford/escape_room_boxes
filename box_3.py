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
    inp = pin1.read_analog()
    if 300 < inp < 400:
        sleep(500)
        if 300 < inp < 400:
            right()
    else:
        wrong()
