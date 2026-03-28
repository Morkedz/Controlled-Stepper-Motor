#Stepmotor, have motor pins be on GPIO 17,18,19,20.
import RPi.GPIO as GPIO
from gpiozero import DistanceSensor
from RpiMotorLib.RpiMotorLib import BYJMotor
import math
import time

GPIO.setmode(GPIO.BCM)

pins = [17,18,19,20]
GPIO.setup(pins,GPIO.OUT)
motor = BYJMotor("stepper", "28BYJ48")

def loop():
    while True:
        # Execute movement
        #motor.motor_run(pins, delay, steps, is_ccw, False, "half", 0.05)

if __name__ == "__main__":
    try:
        loop()
    except KeyboardInterrupt:
        GPIO.output(pins, GPIO.LOW)
        GPIO.cleanup()