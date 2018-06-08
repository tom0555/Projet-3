import pygame
import sys
import os
from pygame.locals import *
import random
from ressources import *



class Map :
	#Pygame initialization
	pygame.init()

	def __init__(self):
		#Window's size attribution
		self.WINDOW = pygame.display.set_mode((WINDOW_WIDHT , WINDOW_HEIGHT), RESIZABLE)
	#function used to place items at a random place.
	def random_item(self):
		tilemap[random.randint(0, 5)][random.randint(2, 3)] = 99
		tilemap[random.randint(6, 11)][random.randint(8, 9)] = 98
		tilemap[random.randint(0, 3)][random.randint(11, 12)] = 97
	#function which is displaying the whole map on the screen.
	def images_display(self):
		#Useful attributes to control the loop( y for lignes and x for columns).
		y = 0
		x = 0
		#Screen refresh
		pygame.display.flip()
		#Begining of the loop
		while y < 15: 
			if tilemap [y][x] == 0: #0 = floor
				self.WINDOW.blit(pygame.image.load(Pics[FLOOR]).convert(), [x * SPRITE_WIDHT, y * SPRITE_HEIGHT])
				pygame.display.flip()
			elif tilemap [y][x] == 1: #1 = wall
				self.WINDOW.blit(pygame.image.load(Pics[WALL]).convert(), [x * SPRITE_WIDHT, y * SPRITE_HEIGHT])
				pygame.display.flip()
			elif tilemap [y][x] == 2: #2 = outdoor
				self.WINDOW.blit(pygame.image.load(Pics[DOOR]).convert(), [x * SPRITE_WIDHT, y * SPRITE_HEIGHT])
				pygame.display.flip()
			elif tilemap [y][x] == 3: #3 = mac gyver
				self.WINDOW.blit(pygame.image.load(Pics[MACDO]).convert(), [x * SPRITE_WIDHT, y * SPRITE_HEIGHT])
				pygame.display.flip()
			elif tilemap [y] [x] == 4: #4 = guard
				self.WINDOW.blit(pygame.image.load(Pics[GUARDIAN]).convert(), [x * SPRITE_WIDHT, y * SPRITE_HEIGHT])
				pygame.display.flip()
			elif tilemap [y] [x] == 99: #99 = first item
				self.WINDOW.blit(pygame.image.load(Pics[ITEM1]).convert(), [x * SPRITE_WIDHT, y * SPRITE_HEIGHT])
				pygame.display.flip()
			elif tilemap [y] [x] == 98: #98 = second item
				self.WINDOW.blit(pygame.image.load(Pics[ITEM2]).convert(), [x * SPRITE_WIDHT, y * SPRITE_HEIGHT])
				pygame.display.flip()
			elif tilemap [y] [x] == 97: #97 = third item
				self.WINDOW.blit(pygame.image.load(Pics[ITEM3]).convert(), [x * SPRITE_WIDHT, y * SPRITE_HEIGHT])
				pygame.display.flip()
			x += 1
			if x % 15 == 0: #Every 15 colums , drop down one line.
				y += 1
				x = 0

