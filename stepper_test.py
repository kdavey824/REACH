from adafruit_motorkit import MotorKit
mkit = MotorKit()

import sys

from adafruit_motor import stepper

var = 1

if __name__ == '__main__':
    try:
        print("TEST")
        while var == 1 :
    #mkit.stepper1.release()
            for i in range(1000) :
                mkit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.SINGLE)  
            for i in range(1000) :
                mkit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.SINGLE)
    except KeyboardInterrupt:
        print("INTERRUPTED!")
        mkit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.SINGLE)
        sys.exit(0)

  
 