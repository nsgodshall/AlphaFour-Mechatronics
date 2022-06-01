import RPi.GPIO as GPIO
import time
# import the library
from RpiMotorLib import RpiMotorLib

# Declare an named instance of class pass GPIO pins numbers
class elevatorBeltController:
    def __init__(self):
        # Define Associate pin numbers
        self.GPIO_pins = (-1, -1, -1)
        self.DIR_PIN = 22
        self.STEP_PIN = 27
        self.ENABLE_PIN = -1

        self.elevatorStepper = RpiMotorLib.A4988Nema(self.DIR_PIN, self.STEP_PIN, self.GPIO_pins)
        self.DELAY_BETWEEN_STEPS = .001
        self.MICROSTEP_MODE = "1/16"

        self.STEPS_PER_COL = 723

    def columnRoutine(self):
        time.sleep(1)

    def test(self):
        print("Elevator Motor Testing...")

        self.elevatorStepper.motor_go(True, SELF.MICROSTEP_MODE, 16*200, self.DELAY_BETWEEN_STEPS, False, 0)
        self.elevatorStepper.motor_go(False, SELF.MICROSTEP_MODE, 16*200, self.DELAY_BETWEEN_STEPS, False, 0)     

        
