import pygame, sys
from pygame.locals import *
import random
from ressources import *



pygame.init()
WINDOW = pygame.display.set_mode((WINDOW_HEIGHT , WINDOW_WIDHT), RESIZABLE)
pygame.display.flip()


tilemap [random.randint(0, 5)] [random.randint(2, 3)] = 99
tilemap [random.randint(6, 11)] [random.randint(8, 9)] = 98
tilemap [random.randint(0, 3)] [random.randint(11, 12)] = 97
y = 0
x = 0
while y < 15: 
	if tilemap [y][x] == 0:
		WINDOW.blit(pygame.image.load(Pics[FLOOR]).convert(), [x*SPRITE_HEIGHT, y*SPRITE_WIDHT])
		print("floor")
		pygame.display.flip()
	elif tilemap [y][x] == 1:
		WINDOW.blit(pygame.image.load(Pics[WALL]).convert(), [x*SPRITE_HEIGHT, y*SPRITE_WIDHT])
		print("wall")
		pygame.display.flip()
	elif tilemap [y][x] == 2:
		WINDOW.blit(pygame.image.load(Pics[DOOR]).convert(), [x*SPRITE_HEIGHT, y*SPRITE_WIDHT])
		pygame.display.flip()
	elif tilemap [y][x] == 3:
		WINDOW.blit(pygame.image.load(Pics[MAC]).convert(), [x*SPRITE_HEIGHT, y*SPRITE_WIDHT])
		pygame.display.flip()
	elif tilemap [y] [x] == 4:
		WINDOW.blit(pygame.image.load(Pics[GUARDIAN]).convert(), [x*SPRITE_HEIGHT, y*SPRITE_WIDHT])
		pygame.display.flip()
	elif tilemap [y] [x] == 99:
		WINDOW.blit(pygame.image.load(Pics[ITEM1]).convert(), [x*SPRITE_HEIGHT, y*SPRITE_WIDHT])
		pygame.display.flip()
	elif tilemap [y] [x] == 98:
		WINDOW.blit(pygame.image.load(Pics[ITEM2]).convert(), [x*SPRITE_HEIGHT, y*SPRITE_WIDHT])
		pygame.display.flip()
	elif tilemap [y] [x] == 97:
		WINDOW.blit(pygame.image.load(Pics[ITEM3]).convert(), [x*SPRITE_HEIGHT, y*SPRITE_WIDHT])
		pygame.display.flip()
	print (x)
	print (y)
	x += 1
	if x%15 == 0: # toutes les 15 colonnes je saute une ligne
		y += 1
		x = 0

new = tilemap