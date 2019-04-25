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
    inp = pin1.read_digital()
    if inp == 1:
        sleep(500)
        right()
    else:
        wrong()
