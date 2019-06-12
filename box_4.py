from microbit import *

# Please tag us if used!
# We'd love to see what you make:
# @ScienceOxford

def right():
    pin0.write_digital(1)
def wrong():
    pin0.write_digital(0)

display.off()

red = pin8
green = pin1
blue = pin2

while True:
    inp1 = pin3.read_analog()
    inp2 = pin4.read_analog()
    inp3 = pin10.read_analog()
    red.write_analog(inp1)
    green.write_analog(inp2)
    blue.write_analog(inp3)
    
    if (0 < inp1 < 20) and (300 < inp2 < 500) and (300 < inp3 < 500):
        sleep(500)
        inp1 = pin3.read_analog()
        inp2 = pin4.read_analog()
        inp3 = pin10.read_analog()
        
        if (0 < inp1 < 20) and (300 < inp2 < 500) and (300 < inp3 < 500):
            right()
    else:
        wrong()
