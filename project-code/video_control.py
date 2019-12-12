# Francis Rayos del Sol
# Lab 1 - Thursday Lab
# fmr32

import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)

while True:
    GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    time.sleep(0.2)

    if(not GPIO.input(17)):
        os.system('echo pause > /home/pi/Desktop/final-project/christmas-fifo')
        print("Button 17 has been pressed.")
    if(not GPIO.input(22)):
        os.system('echo seek 10 > /home/pi/Desktop/final-project/christmas-fifo')
        print("Button 22 has been pressed.")
    if(not GPIO.input(23)):
        os.system('echo seek -10 > /home/pi/Desktop/final-project/christmas-fifo')
        print("Button 23 has been pressed.")
    if(not GPIO.input(27)):
        os.system('echo quit > /home/pi/Desktop/final-project/christmas-fifo')
        print("Button 27 has been pressed.")
        break
