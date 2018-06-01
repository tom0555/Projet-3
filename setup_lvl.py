#!/usr/bin/python3
# -*- coding: Utf-8 -*

import pygame
from pygame.locals import *
from class_char import *
from ressources import *
from class_map import *

pygame.init()

#Ouverture de la fenêtre Pygame (carré : largeur = hauteur)
WINDOW = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDHT))
MAP = Map()
#MAP.random_item()
#MAP.images_display()
MAC = char(tilemap, ITEMS)
pygame.display.set_caption(TITLE)
MAP.random_item()
ITM = 0


#BOUCLE PRINCIPALE
continuer = 1
while continuer:
	
	#Limitation de vitesse de la boucle
	pygame.time.Clock().tick(30)
	for event in pygame.event.get():
		
		if event.type == QUIT:
			continuer = 0
		
		elif event.type == KEYDOWN:
			#Si l'utilisateur presse Echap , quit
			if event.key == K_ESCAPE:
				continuer = 0
					
			#Touches de déplacement
			elif event.key == K_RIGHT:
				ITM = MAC.move('right')
			elif event.key == K_LEFT:
				ITM = MAC.move('left')
			elif event.key == K_UP:
				ITM = MAC.move('up')
			elif event.key == K_DOWN:
				ITM = MAC.move('down')
		#game over
		if ITM < 3 and tilemap[MAC.case_y][MAC.case_x] == 4:
			continuer = 0			
	#Affichages aux nouvelles positions
	MAP.images_display() 
	pygame.display.flip()
	print("il y a {} items" .format(ITM))

	#Victoire -> Retour à l'accueil
	if tilemap[MAC.case_y][MAC.case_x] == 2:
		continuer = 0
