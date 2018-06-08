#!/usr/bin/python3
# -*- coding: Utf-8 -*
import os
import sys
import pygame
from pygame.locals import *
from class_char import *
from ressources import *
from class_map import *

pygame.init()

#Window opening(widht, height).
WINDOW = pygame.display.set_mode((WINDOW_WIDHT, WINDOW_HEIGHT))
#Instance of the Map.
map_lvl_1 = Map()
#Instance of the character.
mac_gyver = char(tilemap, ITEMS)
pygame.display.set_caption(TITLE)
#Random items placement.
map_lvl_1.random_item()
#Item's count
ITM = 0


#Main loop
MOVE_ON = 1

while MOVE_ON:
	#Loop speed limit.
	pygame.time.Clock().tick(60)
	for event in pygame.event.get():
		
		if event.type == KEYDOWN:
			#If escape is used ,program stops.
			if event.key == K_ESCAPE:
				MOVE_ON = 0
					
			#Move binds
			elif event.key == K_RIGHT:
				#Return's recuperation and making the character moving to the right.
				ITM = mac_gyver.move('right')
			elif event.key == K_LEFT:
				ITM = mac_gyver.move('left')
			elif event.key == K_UP:
				ITM = mac_gyver.move('up')
			elif event.key == K_DOWN:
				ITM = mac_gyver.move('down')
			#Checking if we have our 3 items and if the guard's position is just on top of the character's actual position.
			if ITM == 3 and mac_gyver.case_y - 1 == GUARD_POS_Y and mac_gyver.case_x == GUARD_POS_X:
				if event.key == K_RCTRL:
					#Make the guard sleep.
					mac_gyver.sleep_guard(mac_gyver.case_x, mac_gyver.case_y - 1)
					#Modifying guard's absisse to deny any guard replacement while refreshing tilemap.
					GUARD_POS_X = 199
		#Lose condition (if the character walks on the guard's case without made him to sleep before).
		if mac_gyver.case_y == GUARD_POS_Y and mac_gyver.case_x == GUARD_POS_X:
			print("Game over")
			MOVE_ON = 0			
	#Display refresh
	map_lvl_1.images_display() 
	pygame.display.flip()

	#Win condition (if the character walks on the outdoor).
	if mac_gyver.case_y == DOOR_POS_Y and mac_gyver.case_x == DOOR_POS_X:
		print("You won")
		MOVE_ON = 0

