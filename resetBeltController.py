import RPi.GPIO as GPIO
import time
# import the library
from RpiMotorLib import RpiMotorLib

# Declare an named instance of class pass GPIO pins numbers
class resetBeltController:
    def __init__(self):
        # Define Associate pin numbers
        self.GPIO_pins = (-1, -1, -1)
        self.DIR_PIN = 4
        self.STEP_PIN = 17
        self.ENABLE_PIN = -1
            
        self.resetStepper = RpiMotorLib.A4988Nema(self.DIR_PIN, self.STEP_PIN, self.GPIO_pins)
        self.DELAY_BETWEEN_STEPS = .001
        self.MICROSTEP_MODE = "1/16"
        
        # Microsteps between each column
        self.STEPS_PER_COL = 723

    def nextCol(self):
        self.resetStepper.motor_go(False, self.MICROSTEP_MODE, self.STEPS_PER_COL, self.DELAY_BETWEEN_STEPS, False, 0)

    def returnToHome(self):
        self.resetStepper.motor_go(True, self.MICROSTEP_MODE, self.STEPS_PER_COL*7, self.DELAY_BETWEEN_STEPS, False, 0)    

    def test(self):

        print("Reset Motor Testing...")

        self.resetStepper.motor_go(True, self.MICROSTEP_MODE, 16*200, self.DELAY_BETWEEN_STEPS, False, 0)
        self.resetStepper.motor_go(False, self.MICROSTEP_MODE, 16*200, self.DELAY_BETWEEN_STEPS, False, 0)     
