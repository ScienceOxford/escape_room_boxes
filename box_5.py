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
    orange = pin1.read_digital()
    red = pin2.read_digital()
    white = pin3.read_digital()
    blue = pin4.read_digital()
    # note no pin 5!
    green = pin6.read_digital()
    yellow = pin7.read_digital()
    purple = pin8.read_digital()
    pink = pin9.read_digital()
    if orange == 1 and red == 1 and white == 1 and blue == 0 and green == 0 and yellow == 1 and purple == 1 and pink == 1:
        sleep(500)
        right()
    else:
        wrong()
