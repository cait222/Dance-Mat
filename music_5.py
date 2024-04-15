#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 23:02:31 2021

@author: caitlinyeo
"""


from tkinter import *
import tkinter
import pygame
import numpy as np
import matplotlib.pyplot as plt
import random
import sys
import RPi.GPIO as GPIO

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

root = tkinter.Tk()
root.title('Happy Feet')
root.geometry("600x600")

pygame.mixer.init()
pygame.display.init()


upImg = Image.open('1.png')
upImgNumpyFormat = np.asarray(upImg)

downImg = Image.open('2.png')
downImgNumpyFormat = np.asarray(downImg)

leftImg = Image.open('3.png')
leftImgNumpyFormat = np.asarray(leftImg)

rightImg = Image.open('4.png')
rightImgNumpyFormat = np.asarray(rightImg)

Iterations = 3

songs = ['DancewithSomebody.mp3', 'NeverGonnaGiveYouUp.mp3']

def play():
    pygame.mixer.music.load(random.choice(songs))
    pygame.mixer.music.play(loops=0)
    main()
    stop()
    scoring()
    displayScore()
    

def main():
    prevArrow = ''
    
    for i in range(Iterations):
        arrow = random.choice(arrows)
        if i > 0:
            while arrow == prevArrow:
                arrow = random.choice(arrows)
        correctArrows.append(arrow)

        game_loop(arrow)
        
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


def game_loop(arrow):
    if arrow == 'up':
        arrowDisplay(upImgNumpyFormat)

    elif arrow == 'down':
        arrowDisplay(downImgNumpyFormat)

    elif arrow == 'left':
        arrowDisplay(leftImgNumpyFormat)

    elif arrow == 'right':
        arrowDisplay(rightImgNumpyFormat)


def arrowDisplay(image):
    fig = plt.imshow(image)
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)
    plt.draw()
    plt.pause(1)


def stop():
    pygame.mixer.music.stop()

    
def scoring():
    global score
    score = 0
    k = 0

    while k < Iterations:
        if answers[k] == correctArrows[k]:
            score = score + 1
        k = k + 1

    print('SCORE = ', score, "/", Iterations)

    final = {'GIVEN': [], 'PRESSED': []}
    for l in range(0,Iterations):
        final['GIVEN'].append(correctArrows[l])
        final['PRESSED'].append(answers[l])
  
    print("CORRECT ANSWERS: ", final['GIVEN'])
    print("PRESSED: ", final['PRESSED'])
    
def displayScore():
    global my_score, reminder
    my_score = Label(root, text=("SCORE:", score, "/", Iterations), font=("Helvetica", 50))
    my_score.pack(pady=20)
    reminder = Label(root, text="Close window before playing again", font=("Helvetica", 15))
    reminder.pack(pady=20)

my_button = Button(root, text="Start Playing", font=("Helvetica", 20), command=play)
my_button.pack(pady=20)


arrows = ['up', 'down', 'left', 'right']
correctArrows = []
answers = []

root.mainloop()

sys.exit()