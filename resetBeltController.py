import RPi.GPIO as GPIO
import time
# import the library
from RpiMotorLib import RpiMotorLib

#define GPIO pins
step = 17
dir = 4
enable = -1

# Declare an named instance of class pass GPIO pins numbers
class resetBeltController:
    def __init__(self):
        self.GPIO_pins = (-1, -1, -1)
        self.DIR_PIN = dir
        self.STEP_PIN = step
        self.ENABLE_PIN = enable
        self.resetStepper = RpiMotorLib.A4988Nema(self.DIR_PIN, self.STEP_PIN, self.GPIO_pins)
        self.DELAY_BETWEEN_STEPS = .001
        
        self.STEPS_PER_COL = 723

    def nextCol(self):
        self.resetStepper.motor_go(False, "Full", self.STEPS_PER_COL, self.DELAY_BETWEEN_STEPS, False, 0)

    def returnToHome(self):
        self.resetStepper.motor_go(True, "Full", self.STEPS_PER_COL*7, self.DELAY_BETWEEN_STEPS, False, 0)    

    def test(self):

        print("Reset Motor Testing...")

        self.resetStepper.motor_go(True, "1/16", 16*200, self.DELAY_BETWEEN_STEPS, False, 0)
        self.resetStepper.motor_go(False, "1/16", 16*200, self.DELAY_BETWEEN_STEPS, False, 0)     
