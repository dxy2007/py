import pygame
import sys
import os


# Unty PYG02: Pygame hello world Game

'``Introduce pygame module'''

'``Introduce the sys module, or you can only introduce an exit function'''

pygame.init()
'``Initialize pygame window'''
screen = pygame.display.set_mode((480,700))
'``Set window size'''
pygame.display.set_caption("hello world")
"""Define Title"""
cd = pygame.image.load("E:/coed/背景.png")
'``Set Picture Path'''
screen.blit(cd,(0,0))
'``Show pictures'''

while True:
    '``Define an infinite loop'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


    pygame.display.update()
    '``Refresh window'''
