#Stepmotor, have motor pins be on GPIO 17,18,19,20.
#WIP: Angular Displacement as function of time
import RPi.GPIO as GPIO
from RpiMotorLib.RpiMotorLib import BYJMotor
from matplotlib import pyplot as py

GPIO.setmode(GPIO.BCM)

pins = [17,18,19,20]
GPIO.setup(pins,GPIO.OUT)
motor = BYJMotor("stepper", "28BYJ48")
x = []
y = []
displacement = 0

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

        rad_per_step = (2*math.pi)/512
        step_value = rad_per_step if is_ccw else -rad_per_step
        
        for i in range(int(steps)):
            x.append(i * delay)
            current_rad += step_value
            y.append(current_rad)
            
        
        # Execute movement
        motor.motor_run(pins, delay, steps, is_ccw, False, "half", 0.05)

if __name__ == "__main__":
    try:
        loop()
    except KeyboardInterrupt:
        py.plot(x,y)
        plt.title("Angular Displacement as a function of time")
        plt.show()
        motor.motor_stop()
        GPIO.output(pins, GPIO.LOW)
        GPIO.cleanup()