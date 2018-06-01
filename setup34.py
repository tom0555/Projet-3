import pygame, sys
from pygame.locals import *
import random

ITEM1 = 84
ITEM2 = 16
ITEM3 = 15
FLOOR = 0
GUARDIAN = 4
WALL = 1
DOOR = 2
START = 3
MAC = 5



pygame.init()
WINDOW = pygame.display.set_mode((645 , 480), RESIZABLE)
pygame.display.flip()

Pics = {
			WALL : pygame.image.load("wall1.png").convert(),
			FLOOR : pygame.image.load("floor1.jpg").convert(),
			DOOR : pygame.image.load("door.jpg").convert(),
			MAC : pygame.image.load("mac_gyver.png").convert(),
			GUARDIAN : pygame.image.load("GUARDIAN.png").convert(),
			ITEM1 : pygame.image.load("key1.jpg").convert_alpha(),
			ITEM2 : pygame.image.load("key2.jpg").convert_alpha(),
			ITEM3 : pygame.image.load("key3.jpg").convert_alpha()
		}


tilemap =   [
			[FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,WALL, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR],
			[FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, DOOR],
			[FLOOR, WALL, FLOOR,FLOOR, WALL, WALL,FLOOR, WALL, FLOOR,FLOOR, FLOOR, FLOOR,FLOOR, WALL, GUARDIAN],
			[FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,WALL, WALL, FLOOR,FLOOR, WALL, FLOOR],
			[FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,WALL, WALL, FLOOR,WALL, WALL, FLOOR],
			[FLOOR, FLOOR, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, WALL,FLOOR, WALL, FLOOR],
			[FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR],
			[FLOOR, WALL, FLOOR,FLOOR, FLOOR, FLOOR,FLOOR, FLOOR, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR],
			[FLOOR, WALL, FLOOR,FLOOR, FLOOR, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR],
			[FLOOR, WALL, FLOOR,FLOOR, WALL, WALL,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR],
			[START, WALL, WALL,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, FLOOR, FLOOR],
			[FLOOR, WALL, FLOOR,WALL, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, FLOOR, FLOOR],
			[FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,WALL, WALL, FLOOR,WALL, WALL, WALL,FLOOR, WALL, FLOOR],
			[FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,WALL, WALL, FLOOR,WALL, FLOOR, FLOOR,FLOOR, WALL, FLOOR],
			[FLOOR, FLOOR, FLOOR,FLOOR, FLOOR, FLOOR,FLOOR, WALL, FLOOR,FLOOR, FLOOR, FLOOR,FLOOR, WALL, FLOOR],
			]


#D = {emplacement possible1 : "5  0 " , emplacement2 : "6  0" }
 #random.choice(D.keys())
 #choix = choix.split()
 #tilemap [choix[0]][choix[1]] = 99

tilemap [random.randint(0, 5)] [random.randint(2, 3)] = 99
tilemap [random.randint(6, 11)] [random.randint(8, 9)] = 98
tilemap [random.randint(0, 3)] [random.randint(11, 12)] = 97
y = 0
x = 0
while y < 15: 
	if tilemap [y][x] == 0:
		WINDOW.blit(Pics[FLOOR], [x*43, y*32])
		print("floor")
		pygame.display.flip()
	elif tilemap [y][x] == 1:
		WINDOW.blit(Pics[WALL], [x*43, y*32])
		print("wall")
		pygame.display.flip()
	elif tilemap [y][x] == 2:
		WINDOW.blit(Pics[DOOR], [x*43, y*32])
		pygame.display.flip()
	elif tilemap [y][x] == 3:
		WINDOW.blit(Pics[MAC], [x*43, y*32])
		pygame.display.flip()
	elif tilemap [y] [x] == 4:
		WINDOW.blit(Pics[GUARDIAN], [x*43, y*32])
		pygame.display.flip()
	elif tilemap [y] [x] == 99:
		WINDOW.blit(Pics[ITEM1], [x*43, y*32])
		pygame.display.flip()
	elif tilemap [y] [x] == 98:
		WINDOW.blit(Pics[ITEM2], [x*43, y*32])
		pygame.display.flip()
	elif tilemap [y] [x] == 97:
		WINDOW.blit(Pics[ITEM3], [x*43, y*32])
		pygame.display.flip()
	print (x)
	print (y)
	x += 1
	if x%15 == 0: # toutes les 15 colonnes je saute une ligne
		y += 1
		x = 0

