import RPi.GPIO as GPIO
import time
# import the library
from RpiMotorLib import RpiMotorLib

#define GPIO pins
step = 27
dir = 22
enable = -1

# Declare an named instance of class pass GPIO pins numbers
class elevatorBeltController:
    def __init__(self):
        self.GPIO_pins = (-1, -1, -1)
        self.DIR_PIN = dir
        self.STEP_PIN = step
        self.ENABLE_PIN = enable
        self.elevatorStepper = RpiMotorLib.A4988Nema(self.DIR_PIN, self.STEP_PIN, self.GPIO_pins)
        self.DELAY_BETWEEN_STEPS = .001
        
        self.STEPS_PER_COL = 723

    def columnRoutine(self):
        time.sleep(1)

    def test(self):
        print("Elevator Motor Testing...")

        self.elevatorStepper.motor_go(True, "1/16", 16*200, self.DELAY_BETWEEN_STEPS, False, 0)
        self.elevatorStepper.motor_go(False, "1/16", 16*200, self.DELAY_BETWEEN_STEPS, False, 0)     

        
