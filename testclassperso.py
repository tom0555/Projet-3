import pygame, sys
from pygame.locals import *
import random
from ressources import *



class Map :

	pygame.init()

	def __init__(self):
		self.WINDOW = pygame.display.set_mode((WINDOW_HEIGHT , WINDOW_WIDHT), RESIZABLE)

	def random_item(self):
		tilemap [random.randint(0, 5)] [random.randint(2, 3)] = 99
		tilemap [random.randint(6, 11)] [random.randint(8, 9)] = 98
		tilemap [random.randint(0, 3)] [random.randint(11, 12)] = 97

	def images_display(self):
		y = 0
		x = 0
		pygame.display.flip()

		while y < 15: 
			if tilemap [y][x] == 0:
				self.WINDOW.blit(pygame.image.load(Pics[FLOOR]).convert(), [x*43, y*32])
				print("floor")
				pygame.display.flip()
			elif tilemap [y][x] == 1:
				self.WINDOW.blit(pygame.image.load(Pics[WALL]).convert(), [x*43, y*32])
				print("wall")
				pygame.display.flip()
			elif tilemap [y][x] == 2:
				self.WINDOW.blit(pygame.image.load(Pics[DOOR]).convert(), [x*43, y*32])
				pygame.display.flip()
			elif tilemap [y][x] == 3:
				self.WINDOW.blit(pygame.image.load(Pics[MAC]).convert(), [x*43, y*32])
				pygame.display.flip()
			elif tilemap [y] [x] == 4:
				self.WINDOW.blit(pygame.image.load(Pics[GUARDIAN]).convert(), [x*43, y*32])
				pygame.display.flip()
			elif tilemap [y] [x] == 99:
				self.WINDOW.blit(pygame.image.load(Pics[ITEM1]).convert(), [x*43, y*32])
				pygame.display.flip()
			elif tilemap [y] [x] == 98:
				self.WINDOW.blit(pygame.image.load(Pics[ITEM2]).convert(), [x*43, y*32])
				pygame.display.flip()
			elif tilemap [y] [x] == 97:
				self.WINDOW.blit(pygame.image.load(Pics[ITEM3]).convert(), [x*43, y*32])
				pygame.display.flip()
			print (x)
			print (y)
			x += 1
			if x%15 == 0: # toutes les 15 colonnes je saute une ligne
				y += 1
				x = 0
def main():
        tilemap = Map()
        tilemap.random_item()
        tilemap.images_display()

	
main()
