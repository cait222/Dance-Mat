#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 18:17:42 2021

@author: caitlinyeo
"""


import RPi.GPIO as GPIO
import time
import random

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

arrows = ['UP', 'DOWN', 'LEFT', 'RIGHT']
correctArrows = []
answers = []

for i in range(10):
    correctArrows.append(random.choice(arrows))

j = 0

while j < 10:
    print('Press ', correctArrows[j])
    if GPIO.input(TouchPinUp) == GPIO.HIGH:
        print('UP')
        time.sleep(1)
        answers.append('UP')
        
    elif GPIO.input(TouchPinDown) == GPIO.HIGH:
        print('DOWN')
        time.sleep(1)
        answers.append('DOWN')
        
    elif GPIO.input(TouchPinLeft) == GPIO.HIGH:
        print('LEFT')
        time.sleep(1)
        answers.append('LEFT')
        
    elif GPIO.input(TouchPinRight) == GPIO.HIGH:
        print('RIGHT')
        time.sleep(1)
        answers.append('RIGHT')
    else:
        continue
    
    print(j)
    j = j+1

score = 0
k = 0

while k < 10:
    if answers[k] == correctArrows[k]:
        score = score + 1
    k = k + 1

print('SCORE = ', score, "/10")

final = {'GIVEN': [], 'PRESSED': []}
for l in range(0,10):
    final['GIVEN'].append(correctArrows[l])
    final['PRESSED'].append(answers[l])
    
print("CORRECT ANSWERS: ", final['GIVEN'])
print("PRESSED: ", final['PRESSED'])