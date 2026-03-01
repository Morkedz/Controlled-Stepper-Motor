#Stepmotor, have motor pins be on GPIO 17,18,19,20.
import RPi.GPIO as GPIO
from RpiMotorLib.RpiMotorLib import BYJMotor

GPIO.setmode(GPIO.BCM)

pins = [17,18,19,20]
GPIO.setup(pins,GPIO.OUT)
motor = BYJMotor("stepper", "28BYJ48")

def get_valid_input(prompt, value_type=float):
    while True:
        try:
            return value_type(input(prompt))
        except ValueError:
            print(f"Invalid input. Please enter a {value_type.__name__}.")

def loop():
    while True:
        rev = get_valid_input("Enter number of revolutions: ")
        steps = rev * 512
        speed = get_valid_input("Enter angular speed in radians per seconds (max 1.5): ", float)
        #need to correct speed conversion
        delay = (2*math.pi)/(512*speed)
        direction = -1
        while direction not in [0, 1]:
            direction = get_valid_input("Enter direction (0 for CW, 1 for CCW): ", int)
        
        is_ccw = (direction == 1)

        print(f"Running: {rev} revolutions, {speed} rad/s, CCW={is_ccw}")
        
        # Execute movement
        motor.motor_run(pins, delay, steps, is_ccw, False, "half", 0.05)

if __name__ == "__main__":
    try:
        loop()
    except KeyboardInterrupt:
        motor.motor_stop()
        GPIO.output(pins, GPIO.LOW)
        GPIO.cleanup()