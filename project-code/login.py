import os
import subprocess
import pygame
from pygame.locals import *

import time
import RPi.GPIO as GPIO

# Create variables for quit and timeout

GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Note that this is the order of LED light sequencei

GPIO.setup(6, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

start = time.time()

# Monitor configuration
os.putenv("SDL_VIDEODRIVER", "fbcon")
os.putenv("SDL_FBDEV", "/dev/fb1")
os.putenv("SDL_MOUSEDRV", "TSLIB")
os.putenv("SDL_MOUSEDEV", "/dev/input/touchscreen")

# Initialize variables
running = True
start_game = False
pygame.init()
pygame.mouse.set_visible(True)
WHITE = 255, 255, 255
BLACK = 0,0,0
RED = 255,0,0
GREEN = 0,255,0

size = width, height = 320, 240
speed_v1 = [5,5]
speed_v2 = [7,7]
screen = pygame.display.set_mode((320,240))
hit_at = "HIT AT"

flag = 0
servo_flag = 2
video_flag = 0
my_font = pygame.font.Font(None,30)
hitat_font = pygame.font.Font(None,10)
two_buttons = {"9":(80,60), "8":(160,60), "7":(240,60),
        "6":(80,120), "5":(160,120), "4":(240,120),
        "3":(80,180), "2":(160,180), "1":(240,180)}
light_switches = {"SPEED UP":(160,120), "SEQUENCE LIGHTS":(160,60), "DONE WITH LIGHTS?":(160,180)}
playback_buttons = {"PLAY MUSIC":(160,120)}
screen.fill(WHITE)

# LOGIN FUNCTIONALITIES

attempt = 0
pw_input = []
correct = [1,2,2,5]

# LED FUNCTIONALITIES

freq = 2

a = GPIO.PWM(13, freq)
b = GPIO.PWM(6, freq)
c = GPIO.PWM(5, freq)
d = GPIO.PWM(19, freq)
e = GPIO.PWM(26, freq)
f = GPIO.PWM(21, freq)
g = GPIO.PWM(20, freq)
h = GPIO.PWM(16, freq)

while running:
    #lock.tick(40)
    time.sleep(0.02)
    if (flag == 0):
        for text, text_pos in two_buttons.items():
            text_surface = my_font.render(text,True,RED)
            rect = text_surface.get_rect(center=text_pos)
            #screen.blit(text_surface,rect)
            screen.blit(pygame.transform.flip(text_surface, True, True), rect)

        for event in pygame.event.get():
        
            pygame.draw.circle(screen, BLACK, (100,25), 10)
            pygame.draw.circle(screen, BLACK, (140,25), 10)
            pygame.draw.circle(screen, BLACK, (180,25), 10)
            pygame.draw.circle(screen, BLACK, (220,25), 10)
            
            if(event.type is MOUSEBUTTONDOWN):
                pos = pygame.mouse.get_pos()
                print(pos)
            elif(event.type is MOUSEBUTTONUP):
                pos = pygame.mouse.get_pos()
                x,y = pos


                if y > 20 and y < 80:
                    if x > 40 and x < 120:
                        #print "Number 9 Pressed"
                        pw_input.append(9)
                        print pw_input
                    elif x > 140 and x < 200:
                        #print "Number 8 Pressed"
                        pw_input.append(8)
                        print pw_input
                    elif x > 220 and x < 260:
                        #print "Number 7 Pressed"
                        pw_input.append(7)
                        print pw_input

                elif y < 140 and y > 100:
                    if x > 40 and x < 120:
                        #print "Number 6 Pressed"
                        pw_input.append(6)
                        print pw_input
                    elif x > 140 and x < 200:
                        #print "Number 5 Pressed"
                        pw_input.append(5)
                        print pw_input
                    elif x > 220 and x < 260:
                        #print "Number 4 Pressed"
                        pw_input.append(4)
                        print pw_input

                elif y > 160 and y < 220:
                    if x > 40 and x < 120:
                        #print "Number 3 Pressed"
                        pw_input.append(3)
                        print pw_input
                    elif x > 140 and x < 200:
                        #print "Number 2 Pressed"
                        pw_input.append(2)
                        print pw_input
                    elif x > 220 and x < 260:
                        #print "Number 1 Pressed"
                        pw_input.append(1)
                        print pw_input

                # Reconsider this text placement!
                else:
                    if (hit_at == "HIT AT"):
                        screen.fill(WHITE)
                        text_surface = hitat_font.render(hit_at + " " + str(pos),True,RED)
                        rect = text_surface.get_rect(center=(160,10))
                        screen.blit(pygame.transform.flip(text_surface, True, True), rect)

                start_pos = 260
                for number in pw_input:
                    start_pos = start_pos - 40
                    circlerect = pygame.draw.circle(screen, GREEN, (start_pos,25), 10)
                    pygame.display.update(circlerect)

    # Check if password is correct
    if len(correct) == len(pw_input) and correct == pw_input:
        flag = 1
        if (flag == 1):
            screen.fill(WHITE)
            for text, text_pos in light_switches.items():
                text_surface = my_font.render(text,True,GREEN)
                rect = text_surface.get_rect(center=text_pos)
                screen.blit(pygame.transform.flip(text_surface, True, True), rect)

            # LED FUNCTIONALITIES
            if (servo_flag == 2):
                os.system("python pwm_calibrate.py")
                servo_flag = 3

            # Turn on lights
            dc = 40.0
            a.start(dc)
            b.start(dc)
            c.start(dc)
            d.start(dc)
            e.start(dc)
            f.start(dc)
            g.start(dc)
            h.start(dc)

            for event in pygame.event.get():
                
                if(event.type is MOUSEBUTTONDOWN):
                    pos = pygame.mouse.get_pos()
                    print(pos)
                elif(event.type is MOUSEBUTTONUP):
                    pos = pygame.mouse.get_pos()
                    x,y = pos

                    if y > 160 and y < 220:
                        if x > 60 and x < 260:
                            print "Done Pressed"
                            video_flag = 1

                    elif y > 100 and y < 140:
                        if x > 60 and x < 260:
                            print "Speed Up Pressed"
                            # LED FUNCTIONALITIES - FAST

                            freq = 5
                            dc = 40.0

                            a.ChangeFrequency(freq)
                            b.ChangeFrequency(freq)
                            c.ChangeFrequency(freq)
                            d.ChangeFrequency(freq)
                            e.ChangeFrequency(freq)
                            f.ChangeFrequency(freq)
                            g.ChangeFrequency(freq)
                            h.ChangeFrequency(freq)
 
                            a.start(dc)
                            b.start(dc)
                            c.start(dc)
                            d.start(dc)
                            e.start(dc)
                            f.start(dc)
                            g.start(dc)
                            h.start(dc)

                    elif y > 20 and y < 80:
                        if x > 60 and x < 260:
                            # LED FUNCTIONALITIES - TOGGLE
                            print "Toggle Pressed"
                            freq = 2
                            dc1 = 10.0
                            dc2 = 20.0
                            dc3 = 30.0
                            dc4 = 40.0
                            dc5 = 50.0
                            dc6 = 60.0
                            dc7 = 70.0
                            dc8 = 80.0

                            a.ChangeFrequency(freq)
                            b.ChangeFrequency(freq)
                            c.ChangeFrequency(freq)
                            d.ChangeFrequency(freq)
                            e.ChangeFrequency(freq)
                            f.ChangeFrequency(freq)
                            g.ChangeFrequency(freq)
                            h.ChangeFrequency(freq)
                            
                            a.ChangeDutyCycle(dc1)
                            b.ChangeDutyCycle(dc2)
                            c.ChangeDutyCycle(dc3)
                            d.ChangeDutyCycle(dc4)
                            e.ChangeDutyCycle(dc5)
                            f.ChangeDutyCycle(dc6)
                            g.ChangeDutyCycle(dc7)
                            h.ChangeDutyCycle(dc8)

            pygame.display.flip()

        if (video_flag == 1):
            screen.fill(WHITE)
            for text, text_pos in playback_buttons.items():
                text_surface = my_font.render(text,True,RED)
                rect = text_surface.get_rect(center=text_pos)
                screen.blit(pygame.transform.flip(text_surface, True, True), rect)

            if y > 100 and y < 140:
                if x > 140 and x < 200:
                    print "Play Pressed"
                    pygame.quit()
                    #os.system("clear")
                    #os.system("bash start_video")
                    os.system("./start_video")
                    #subprocess.call("/home/pi/Desktop/final-project/start_video.sh", shell=True)
            
    # Check is password is incorrect
    if len(correct) == len(pw_input) and correct != pw_input:
        pw_input = []
        attempt += 1
        print("number of attempts: " + str(attempt))
        print(pw_input)

        error = my_font.render("PLEASE TRY AGAIN",True,RED)
        rect = error.get_rect(center=(160,215))
        screen.blit(pygame.transform.flip(error, True, True), rect)
      
        pygame.draw.circle(screen, RED, (100,25), 10)
        pygame.draw.circle(screen, RED, (140,25), 10)
        pygame.draw.circle(screen, RED, (180,25), 10)
        pygame.draw.circle(screen, RED, (220,25), 10)

        if attempt == 5:
            running = False
    
    pygame.display.flip()


    # Check buttons and timeout condition
    if not GPIO.input(27):
        running = False

    current = time.time()
    elapsed = current - start
    if elapsed >= 300:
        running = False

#servo_on.stop()
a.stop()
b.stop()
c.stop()
d.stop()
e.stop()
f.stop()
g.stop()
h.stop()
GPIO.cleanup()
