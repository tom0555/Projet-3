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
WINDOW = pygame.display.set_mode((640 , 480), RESIZABLE)
pygame.display.flip()

#Pics = {
#			WALL : pygame.image.load("wall1.png").convert(),
#			FLOOR : pygame.image.load("floor1.jpg").convert(),
#			OUT : pygame.image.load("door.jpg").convert(),
#			MAC : pygame.image.load("mac_gyver.png").convert(),
#			GUARDIAN : pygame.image.load("GUARDIAN.png").convert()
#		}



#tilemap =   [
#			[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],
#			[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],
#			[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],
#			[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],
#			[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],
#			[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],
#			[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],
#			[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],
#			[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],
#			[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],
#			[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],
#			[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],
#			[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],
#			[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],
#			[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, FLOOR, OUT],
#			]

TILESIZE = 60
MAPWIDHT = 15
MAPHEIGHT = 15




class Zone:
	@classmethod
	def init_zone(cls):
		tilemap =   [
			[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],
			[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],
			[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],
			[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],
			[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],
			[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],
			[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],
			[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],
			[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],
			[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],
			[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],
			[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],
			[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],
			[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],
			[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, WALL, FLOOR],[FLOOR, FLOOR, OUT],
			]
		return tilemap
	@classmethod
	def load_pics(cls, tilemap):
		i = 1
		while i <= 226:
			y = 0
			print(tilemap[i][y])
			if tilemap [i][y] == 0:
				pygame.image.load("mac_gyver.png").convert()
			elif tilemap [i][y] == 1:
				pygame.image.load("wall1.png").convert()
			i += 1
			if i%15 == 0:
				y += 1
		return tilemap

def main():
	Zone.init_zone()
	Zone.load_pics(tilemap)
main()

	

#while True:
	#for event in pygame.event.get():
		#if event.type == QUIT:
			#pygame.quit()
			#sys.exit()





#while tilemap[0]:
	#pygame.image.load("wall1.png").convert(),	
#for WALL in tilemap:
#	pygame.image.load("wall1.png").convert()
#for FLOOR in tilemap:
#	pygame.image.load("floor1.jpg").convert(),



