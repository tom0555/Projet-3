import pygame, sys
from pygame.locals import *
import random

FLOOR = 0
GUARDIAN = 4
WALL = 1
OUT = 2
START = 3
MAC = 5


pygame.init()
WINDOW = pygame.display.set_mode((645 , 480), RESIZABLE)
pygame.display.flip()

Pics = {
			WALL : pygame.image.load("wall1.png").convert(),
			FLOOR : pygame.image.load("floor1.jpg").convert(),
			OUT : pygame.image.load("door.jpg").convert(),
			MAC : pygame.image.load("mac_gyver.png").convert(),
			GUARDIAN : pygame.image.load("GUARDIAN.png").convert()
		}


tilemap =   [
			[FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR],
			[FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, OUT],
			[FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, FLOOR, FLOOR,FLOOR, WALL, GUARDIAN],
			[FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR],
			[FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR],
			[FLOOR, FLOOR, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR],
			[FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR],
			[FLOOR, WALL, FLOOR,FLOOR, FLOOR, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR],
			[FLOOR, WALL, FLOOR,FLOOR, FLOOR, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR],
			[FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR],
			[START, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, FLOOR, FLOOR],
			[FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, FLOOR, FLOOR],
			[FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR],
			[FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, FLOOR, FLOOR,FLOOR, WALL, FLOOR],
			[FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, FLOOR, FLOOR,FLOOR, WALL, FLOOR],
			]


y = 0
x = 0
while y < 15: 
	if tilemap [y][x] == 0:
		WINDOW.blit(pygame.image.load("floor1.jpg").convert(), [x*43, y*32])
		print("floor")
		pygame.display.flip()
	elif tilemap [y][x] == 1:
		WINDOW.blit(pygame.image.load("wall1.png").convert(), [x*43, y*32])
		print("wall")
		pygame.display.flip()
	elif tilemap [y][x] == 2:
		DOOR = pygame.image.load("door.jpg").convert()
		DOOR.set_colorkey((0,0,0))
		WINDOW.blit(DOOR, [x*43, y*32])
		pygame.display.flip()
	elif tilemap [y][x] == 3:
		WINDOW.blit(pygame.image.load("mac_gyver.png").convert_alpha(), [x*43, y*32])
		pygame.display.flip()
	elif tilemap [y] [x] == 4:
		WINDOW.blit(pygame.image.load("GUARDIAN.png").convert_alpha(), [x*43, y*32])
		pygame.display.flip()
	print (x)
	print (y)
	x += 1
	if x%15 == 0: # toutes les 15 colonnes je saute une ligne
		y += 1
		x = 0

