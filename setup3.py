from random import *
import pygame
from pygame.locals import *

pygame.init()
WINDOW = pygame.display.set_mode((1600 , 900), RESIZABLE)
CONTINUE = 1
FLOOR = pygame.image.load("floor1.jpg").convert()
WINDOW.blit(FLOOR, (0,0))
MAC_PIC = pygame.image.load("mac_gyver.png").convert_alpha()
WINDOW.blit(MAC_PIC, (106,60))
pygame.display.flip()


while CONTINUE:
	continue