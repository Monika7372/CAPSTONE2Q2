# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 22:31:41 2021

@author: My Laptop
"""
import pygame

pygame.init()

velocity=[1,1]
carryOn = True
GRAY=(100,100,100)
RED=(255,0,0)
d=0
ball=pygame.Rect(200,300,10,10)
screen = pygame.display.set_mode((400,600))
screen.fill(GRAY)
while carryOn:
    for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                  carryOn = False # Flag that we are done so we exit this loop             
    if (ball.y > 0 and d == 0):
        ball.y = ball.y - 1
    if (ball.y == 0):
        d=1
    if (ball.y < 580 and d == 1):
        ball.y = ball.y + 1
    if (ball.y == 580):
        d=0
    screen.fill(GRAY)
    pygame.draw.rect(screen,RED ,ball)
    pygame.display.update()

    