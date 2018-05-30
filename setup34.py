import pygame, sys
from pygame.locals import *
import numpy as np
import random

KEY1 = 10
KEY2 = 11
KEY3 = 12
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
			[FLOOR, WALL, FLOOR,FLOOR, WALL, KEY1,KEY1, WALL, FLOOR,FLOOR, WALL, KEY3,KEY3, WALL, FLOOR],
			[FLOOR, WALL, FLOOR,FLOOR, WALL, KEY1,KEY1, WALL, FLOOR,FLOOR, WALL, KEY3,KEY3, WALL, OUT],
			[FLOOR, WALL, FLOOR,FLOOR, WALL, KEY1,KEY1, WALL, FLOOR,FLOOR, FLOOR, KEY3,KEY3, WALL, GUARDIAN],
			[FLOOR, WALL, FLOOR,FLOOR, WALL, KEY1,KEY1, WALL, FLOOR,FLOOR, WALL, KEY3,KEY3, WALL, FLOOR],
			[FLOOR, WALL, FLOOR,FLOOR, WALL, KEY1,KEY1, WALL, FLOOR,FLOOR, WALL, KEY3,KEY3, WALL, FLOOR],
			[FLOOR, FLOOR, FLOOR,FLOOR, WALL, KEY1,KEY1, WALL, FLOOR,FLOOR, WALL, KEY3,KEY3, WALL, FLOOR],
			[FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR],
			[FLOOR, WALL, FLOOR,FLOOR, FLOOR, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR],
			[FLOOR, WALL, FLOOR,FLOOR, FLOOR, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR],
			[FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR],
			[START, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, FLOOR, FLOOR],
			[FLOOR, WALL, FLOOR,FLOOR, WALL, KEY2,KEY2, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, FLOOR, FLOOR],
			[FLOOR, WALL, KEY2,KEY2, WALL, KEY2,KEY2, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR],
			[FLOOR, WALL, KEY2,KEY2, WALL, KEY2,KEY2, WALL, FLOOR,FLOOR, FLOOR, KEY3,KEY3, WALL, FLOOR],
			[FLOOR, WALL, KEY2,KEY2, WALL, KEY2,KEY2, WALL, FLOOR,FLOOR, FLOOR, KEY3,KEY3, WALL, FLOOR],
			]


emplacement = {emplacement possible1 : "3  2 " , emplacement2 : 2 }
 choix = choice.emplacement()#.split()
 choix = choix.split()
 tilemap [choix[0]][choix[1]] = 99
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
	elif tilemap [y] [x] == 10:
		random = randrange(0, 5)
		if random == 1:
			WINDOW.blit(pygame.image.load("key1.png").convert_alpha(), [x*43, y*32])
			pygame.display.flip()
	print (x)
	print (y)
	x += 1
	if x%15 == 0: # toutes les 15 colonnes je saute une ligne
		y += 1
		x = 0






# fonction définissant floor acceptable = 10
# placement objets aléatoire



while False :
	key1 = random.choice(tilemap)
	
	if key1 == 10 :
		key2 = random.choice(tilemap)

		if key2 == 10 :
			key3 = random.choice(tilemap)

			if key3 == 10 :
				return True

	else :
		return False
