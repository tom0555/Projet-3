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
#print(" la position y du garde est {} ,la position x du garde est {}" .format(GUARD_POS_Y, GUARD_POS_X))
while continuer:
	#Limitation de vitesse de la boucle
	pygame.time.Clock().tick(60)
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
			if ITM >= 3 and MAC.case_y-1 == GUARD_POS_Y and MAC.case_x == GUARD_POS_X:
				if event.key == K_RCTRL:
					MAC.sleep_guard(MAC.case_x, MAC.case_y-1)
					GUARD_POS_X = 199
			#print(MAC.case_y, MAC.case_x)
			#print(ITM)
		#game over
		if MAC.case_y == GUARD_POS_Y and MAC.case_x == GUARD_POS_X:
			print("YOLO")
			continuer = 0			
	#Affichages aux nouvelles positions
	MAP.images_display() 
	pygame.display.flip()
	#print("il y a {} items" .format(ITM))

	#Victoire -> Retour à l'accueil
	if MAC.case_y == DOOR_POS_Y and MAC.case_x == DOOR_POS_X:
		print("gg")
		continuer = 0

