#!/usr/bin/python
import time
import sys
import numpy as np

try:
    from sklearn import neighbors, svm
    HAVE_SK = True
except ImportError:
    HAVE_SK = False

import struct

import myo

from adafruit_motorkit import MotorKit
mkit = Motorkit()
stepper_position = 0

from adafruit_motor import stepper

from adafruit_servokit import ServoKit
skit = ServoKit(channels=16,address=0x41)
num_motor = 5

#Initialize Myo object
m = myo.Myo(myo.NNClassifier(), sys.argv[1] if len(sys.argv) >= 2 else None)
    
m.add_raw_pose_handler(print)

m.connect()

loop_num = 0

var = 1 
while var == 1 :
    m.run()
    loop_num = loop_num+1;
    pos = m.last_pose
    #print(m.last_pose)
    #print(loop_num)
    
    #Pose 0 is rest
    if pos == 0:
        if stepper_position == 0:
            pass
        else
            for i in range(1000) :
                mkit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.SINGLE)
            stepper_position = 0
        for j in range(num_motor):
            mkit.servo[j].angle = 0
        pass#print("Rest pose.")
    elif pos == 1.0:
        #Pose 1 is Pointing Pointer Finger
        if stepper_position == 1:
            pass
        else
            for i in range(1000) :
                mkit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.SINGLE)
            stepper_position = 1
        for j in range(num_motor):
            skit.servo[j].angle = 90
    elif pos == 2.0:
        #Pose 2 is a fist
        if stepper_position == 1:
            pass
        else
            for i in range(1000) :
                mkit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.SINGLE)
            stepper_position = 1
        for j in range(num_motor):
            skit.servo[j].angle = 180
    elif pos == 3.0:
        #Pose 3 is a thumbs up
        if stepper_position == 0:
            pass
        else
            for i in range(1000) :
                mkit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.SINGLE)
            stepper_position = 0
        #for j in range(num_motor):
    elif pos == 4.0:
        pass
        #MOTOR CODE
    elif pos == 5.0:
        pass
        #MOTOR CODE
    elif pos == 6.0:
        pass
        #MOTOR CODE
    elif pos == 7.0:
        pass
        #MOTOR CODE
    elif pos == 8.0:
        pass
        #MOTOR CODE
    elif pos == 9.0:
        pass
        #MOTOR CODE
    elif pos == 10.0:
        pass
        #MOTOR CODE
    elif pos == 11.0:
        pass
        #MOTOR CODE
    elif pos == 12.0:
        pass
        #MOTOR CODE
    elif pos == 13.0:
        pass
        #MOTOR CODE
    elif pos == 14.0:
        pass
        #MOTOR CODE
    elif pos == 15.0:
        pass
        #MOTOR CODE
    elif pos == 16.0:
        pass
        #MOTOR CODE
    else:
        #print("Pose not registered.: ", pos)
        pass
