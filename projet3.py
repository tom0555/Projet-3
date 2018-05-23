#définir zone
from random import *
import pygame
from pygame.locals import *
#faire fonction avec choice pour choisir un placement random
#import numpy pour les murs


WINDOW_LENGHT = 480
WINDOW_WIDHT = 640
pygame.init()
WINDOW = pygame.display.set_mode((640 , 480), RESIZABLE)
CONTINUE = 1
MAC_PIC = pygame.image.load("mac_gyver.png").convert()
WINDOW.blit(MAC_PIC, (200,250))
pygame.display.flip()



class Zone:

	WIDHT = 15
	LENGHT = 15
	UNIT = 1
	START = 0



	#def __init__(self, corner1, corner2):
		#self.corner1 = corner1
		#self.corner2 = corner2

	@classmethod
	def initialize_zone(cls):
		ZONES = []
		ZONES = [[0] * 15 for i in range(15)]
		print(ZONES)
		return(ZONES)
	def build_walls(self, ZONES):
		WALL = 1
		initialize_zone.ZONES [0] [2] = WALL



	#def object_placement(self , ZONES)
		#MAC_GYVER = 1
		#GUARD = 2
		#NEEDLE = 3




def main():
	Zone.initialize_zone()
main()

while(CONTINUE):
	continue