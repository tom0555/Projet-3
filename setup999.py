import pygame, sys
from pygame.locals import *

FLOOR = 0
GUARDIAN = 4
MAC = 3
WALL = 1
OUT = 2
TILESIZE = 100
MAPWIDHT = 15
MAPHEIGHT = 15

pygame.init()
WINDOW = pygame.display.set_mode((1600 , 900), RESIZABLE)
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
			[FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, FLOOR, FLOOR,FLOOR, WALL, FLOOR],
			[FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR],
			[FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR],
			[FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR],
			[FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR],
			[FLOOR, WALL, FLOOR,FLOOR, FLOOR, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR],
			[FLOOR, WALL, FLOOR,FLOOR, FLOOR, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR],
			[FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR],
			[FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, FLOOR, FLOOR],
			[FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, FLOOR, FLOOR],
			[FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR],
			[FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, FLOOR, FLOOR,FLOOR, WALL, FLOOR],
			[FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, WALL, FLOOR,FLOOR, FLOOR, FLOOR,FLOOR, WALL, FLOOR],
			]

TILESIZE = 60
MAPWIDHT = 15
MAPHEIGHT = 15

i = 1
y = 0
z = 0
while i <= 226: #15*15
	if tilemap [y][z] == 0:
		WINDOW.blit(pygame.image.load("floor1.jpg").convert(), [z*106, y*60])
		print("floor")
		pygame.display.flip()
	elif tilemap [y][z] == 1:
		WINDOW.blit(pygame.image.load("wall1.png").convert(), [z*106, y*60])
		print("wall")
		pygame.display.flip()
	elif tilemap [y][z] == 2:
		DOOR = pygame.image.load("door.jpg").convert()
		DOOR.set_colorkey((0,0,0))
		WINDOW.blit(DOOR, [z*106, y*60])
		pygame.display.flip()
	i += 1
	z += 1
	print (z)
	print (y)
	if z%15 == 0: # toutes les 15 colonnes je saute une ligne
		y += 1
		z = 0
