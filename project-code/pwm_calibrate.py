# Francis Rayos del Sol - fmr32
# Lab 3

import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(3, GPIO.OUT)

# Define constants
GPIO_pin = 3
freq = 50
dc = 7.10

# Start PWM
p = GPIO.PWM(GPIO_pin, freq)

start = time.time()
while time.time() < start + 0.15:
    p.start(dc)
p.ChangeFrequency(50)
p.ChangeDutyCycle(0)

# Continue until stop button is pressed
#while GPIO.input(27):
    # print("Button 27 has been pressed.")
#    pass

p.stop()
#GPIO.cleanup()
sys.exit()

