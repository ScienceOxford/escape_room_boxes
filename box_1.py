from microbit import *

# Please tag us if used!
# We'd love to see what you make:
# @ScienceOxford

def right():
   pin0.write_digital(1)
def wrong():
   pin0.write_digital(0)

while True:
    inp1 = pin1.read_digital()
    inp2 = pin2.read_digital()
    inp3 = pin8.read_digital()
    inp4 = pin12.read_digital()
    if inp1 == 1 and inp2 == 0 and inp3 == 1 and inp4 == 0:
        sleep(500)
        right()
    else:
        wrong()
