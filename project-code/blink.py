# Francis Rayos del Sol - fmr32
# Lab 3

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.OUT)

# Define constants
GPIO_pin = 13
freq = 10
dc = 20.0

# Start PWM
p = GPIO.PWM(GPIO_pin, freq)
p.start(dc)

# Continue until stop button is pressed
while GPIO.input(27):
    # print("Button 27 has been pressed.")
    pass

p.stop
GPIO.cleanup()
