import RPi.GPIO as GPIO
import time
# import the library
from RpiMotorLib import RpiMotorLib

#define GPIO pins
step = 5
dir = 6
enable = -1

# Declare an named instance of class pass GPIO pins numbers
class dropperController:
    def __init__(self):
        # Define GPIO pin
        self.GPIO_pins = (-1, -1, -1)
        self.DIR_PIN = 6
        self.STEP_PIN = 5
        self.ENABLE_PIN = -1

        self.dropperStepper = RpiMotorLib.A4988Nema(self.DIR_PIN, self.STEP_PIN, self.GPIO_pins)
        self.DELAY_BETWEEN_STEPS = .001
        self.MICROSTEP_MODE = "Full"
        self.STEPS_PER_COL = 200
        

    def nextCol(self):
        self.dropperStepper.motor_go(False, self.MICROSTEP_MODE, self.STEPS_PER_COL, self.DELAY_BETWEEN_STEPS, False, 0)

    def collectNewToken(self):
        self.dropperStepper.motor_go(True, self.MICROSTEP_MODE, 3600, self.DELAY_BETWEEN_STEPS, False, 0)   

    def test(self):
        print("Dropper Motor Testing...")
        self.dropperStepper.motor_go(True, self.MICROSTEP_MODE, 200, self.DELAY_BETWEEN_STEPS, False, 0)
        self.dropperStepper.motor_go(False, self.MICROSTEP_MODE, 200, self.DELAY_BETWEEN_STEPS, False, 0)     
