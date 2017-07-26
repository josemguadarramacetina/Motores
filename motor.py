import sys
import time 
from Phidget22.Devices.Stepper import *
from Phidget22.PhidgetException import *
from Phidget22.Phidget import *
from Phidget22.Net import *

try:
    ch0 = Stepper()
    ch1 = Stepper()
    ch2 = Stepper()
    ch3 = Stepper()
except RuntimeError as e:
    print("Runtime Exception %s" % e.details)
    print("Press Enter to Exit...\n")
    readin = sys.stdin.read(1)
    exit(1)

def StepperAttached(e):
    try:
        attached = e

    except PhidgetException as e:
        print("Phidget Exception %i: %s" % (e.code, e.details))
        print("Press Enter to Exit...\n")
        readin = sys.stdin.read(1)
        exit(1)   
    
def StepperDetached(e):
    detached = e
    try:
        print("\nDetach event on Port %d Channel %d" % (detached.getHubPort(), detached.getChannel()))
    except PhidgetException as e:
        print("Phidget Exception %i: %s" % (e.code, e.details))
        print("Press Enter to Exit...\n")
        readin = sys.stdin.read(1)
        exit(1)   

def ErrorEvent(e, eCode, description):
    print("Error %i : %s" % (eCode, description))

def motor0(e, position):
    print("Position: %f" % position)

try:
    ch0.setOnAttachHandler(StepperAttached)
    ch0.setOnDetachHandler(StepperDetached)
    ch0.setOnErrorHandler(ErrorEvent)
    ch0.setOnPositionChangeHandler(motor0)
    ch0.setChannel(0)
    ch0.openWaitForAttachment(500)
except PhidgetException as e:
    print("Phidget Exception %i: %s" % (e.code, e.details))
    print("Press Enter to Exit...\n")
    readin = sys.stdin.read(1)
    exit(1)

def motor1(e, position):
    print("Position: %f" % position)

try:
    ch1.setOnAttachHandler(StepperAttached)
    ch1.setOnDetachHandler(StepperDetached)
    ch1.setOnErrorHandler(ErrorEvent)
    ch1.setOnPositionChangeHandler(motor1)
    ch1.setChannel(1)
    ch1.openWaitForAttachment(500)
except PhidgetException as e:
    print("Phidget Exception %i: %s" % (e.code, e.details))
    print("Press Enter to Exit...\n")
    readin = sys.stdin.read(1)
    exit(1)

def motor2(e, position):
    print("Position: %f" % position)

try:
    ch2.setOnAttachHandler(StepperAttached)
    ch2.setOnDetachHandler(StepperDetached)
    ch2.setOnErrorHandler(ErrorEvent)
    ch2.setOnPositionChangeHandler(motor2)
    ch2.setChannel(2)
    ch2.openWaitForAttachment(500)
except PhidgetException as e:
    print("Phidget Exception %i: %s" % (e.code, e.details))
    print("Press Enter to Exit...\n")
    readin = sys.stdin.read(1)
    exit(1)

def motor3(e, position):
    print("Position: %f" % position)

try:
    ch3.setOnAttachHandler(StepperAttached)
    ch3.setOnDetachHandler(StepperDetached)
    ch3.setOnErrorHandler(ErrorEvent)
    ch3.setOnPositionChangeHandler(motor3)
    ch3.setChannel(3)
    ch3.openWaitForAttachment(500)
except PhidgetException as e:
    print("Phidget Exception %i: %s" % (e.code, e.details))
    print("Press Enter to Exit...\n")
    readin = sys.stdin.read(1)
    exit(1)

print("Engaging the motor\n")
ch0.setEngaged(1)
ch1.setEngaged(1)
ch2.setEngaged(1)
ch3.setEngaged(1)

print("Setting Position to 15000 for 5 seconds...\n")
ch0.setTargetPosition(15000)
ch1.setTargetPosition(15000)
ch2.setTargetPosition(15000)
ch3.setTargetPosition(15000)
time.sleep(5)

print("Setting Position to -15000 for 5 seconds...\n")
ch0.setTargetPosition(-15000)
ch1.setTargetPosition(-15000)
ch2.setTargetPosition(-15000)
ch3.setTargetPosition(-15000)
time.sleep(5)

print("Setting Position to 0 for 5 seconds...\n")
ch0.setTargetPosition(0)
ch1.setTargetPosition(0)
ch2.setTargetPosition(0)
ch3.setTargetPosition(0)
time.sleep(5)

try:
    ch0.close()
    ch1.close()
    ch2.close()
    ch3.close()
except PhidgetException as e:
    print("Phidget Exception %i: %s" % (e.code, e.details))
    print("Press Enter to Exit...\n")
    readin = sys.stdin.read(1)
    exit(1) 

print("Closed Stepper device")
exit(0)

