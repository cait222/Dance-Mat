#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 13:54:58 2021

@author: caitlinyeo
"""

import time
import random
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import RPi.GPIO as GPIO


############### TOUCH PIN SETUP ################################

TouchPinUp = 37
TouchPinDown = 36
TouchPinLeft = 33
TouchPinRight = 31
 

def setup() :
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(TouchPinUp, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(TouchPinDown, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(TouchPinLeft, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(TouchPinRight, GPIO.IN, pull_up_down=GPIO.PUD_UP)

setup()

################ IMAGE LOADING ###################################

upImg = Image.open('1.png')
upImgNumpyFormat = np.asarray(upImg)

downImg = Image.open('2.png')
downImgNumpyFormat = np.asarray(downImg)

leftImg = Image.open('3.png')
leftImgNumpyFormat = np.asarray(leftImg)

rightImg = Image.open('4.png')
rightImgNumpyFormat = np.asarray(rightImg)

################## DISPLAY FUNCTIONS #############################

def arrowDisplay(image):
    fig = plt.imshow(image)
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)
    plt.draw()
    plt.pause(1)


def game_loop():
    if arrow == 'up':
        arrowDisplay(upImgNumpyFormat)
    elif arrow == 'down':
        arrowDisplay(downImgNumpyFormat)
    elif arrow == 'left':
        arrowDisplay(leftImgNumpyFormat)
    elif arrow == 'right':
        arrowDisplay(rightImgNumpyFormat)

################ MAIN CODE ########################################

arrows = ['up', 'down', 'left', 'right']
correctArrows = []
answers = []
    
prevArrow = ''

for i in range(5):
    arrow = random.choice(arrows)
    if i > 0:
        while arrow == prevArrow:
            arrow = random.choice(arrows)
    correctArrows.append(arrow)

    game_loop()
    
    pressed = False
    
    while pressed == False:
        if GPIO.input(TouchPinUp) == GPIO.HIGH:
            print('up')
            time.sleep(1)
            answer = 'up'
            pressed = True
        elif GPIO.input(TouchPinDown) == GPIO.HIGH:
            print('down')
            time.sleep(1)
            answer = 'down'  
            pressed = True
        elif GPIO.input(TouchPinLeft) == GPIO.HIGH:
            print('left')
            time.sleep(1)
            answer = 'left'  
            pressed = True
        elif GPIO.input(TouchPinRight) == GPIO.HIGH:
            print('right')
            time.sleep(1)
            answer = 'right'
            pressed = True
        else:
            continue

    
    answers.append(answer)
    plt.close()
    

    
    prevArrow = arrow

############ SCORING ###########################################

score = 0
k = 0

while k < 5:
    if answers[k] == correctArrows[k]:
        score = score + 1
    k = k + 1

print('SCORE = ', score, "/5")

final = {'GIVEN': [], 'PRESSED': []}
for l in range(0,5):
    final['GIVEN'].append(correctArrows[l])
    final['PRESSED'].append(answers[l])
    
print("CORRECT ANSWERS: ", final['GIVEN'])
print("PRESSED: ", final['PRESSED'])
