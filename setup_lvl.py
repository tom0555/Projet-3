#!/usr/bin/python3
# -*- coding: Utf-8 -*
""" Main folder"""
import pygame
from class_char import char
from class_map import Map
from ressources import DOOR_POS_X
from ressources import DOOR_POS_Y
from ressources import GUARD_POS_X
from ressources import GUARD_POS_Y
from ressources import ITEMS
from ressources import WINDOW_WIDHT
from ressources import WINDOW_HEIGHT

pygame.init()
TILEMAP = 0
#Window opening(widht, height).
WINDOW = pygame.display.set_mode((WINDOW_WIDHT, WINDOW_HEIGHT))
#Instance of the Map.
MAP_LVL_1 = Map()
#Instance of the character.
MAC_GYVER = char(TILEMAP, ITEMS)
#Random items placement.
MAP_LVL_1.random_item()
#Item's count
ITM = 0
#Main loop
MOVE_ON = 1
while MOVE_ON:
#Loop speed limit.
    pygame.time.Clock().tick(60)
    for event in pygame.event.get():
        if event.type == pygame.key.keydown():
            #If escape is used ,program stops.
            if event.key == pygame.key.k_escape:
                MOVE_ON = 0
            #Move binds
            elif event.key == pygame.key.k_right():
                #Return's recuperation and making the character moving to the right.
                ITM = MAC_GYVER.move('right')
            elif event.key == pygame.key.k_left:
                ITM = MAC_GYVER.move('left')
            elif event.key == pygame.key.k_up:
                ITM = MAC_GYVER.move('up')
            elif event.key == pygame.key.k_down:
                ITM = MAC_GYVER.move('down')
            #Checking if we have our 3 items and if the guard's
            #position is just on top of the character's actual position.
            if ITM == 3 and MAC_GYVER.case_y - 1 == GUARD_POS_Y and MAC_GYVER.case_x == GUARD_POS_X:
                if event.key == pygame.key.k_rctrl:
                    #Make the guard sleep.
                    MAC_GYVER.sleep_guard(MAC_GYVER.case_x, MAC_GYVER.case_y - 1)
                    #Modifying guard's absisse to deny any guard
                    #replacement while refreshing tilemap.
                    GUARD_POS_X = 199
        #Lose condition (if the character walks on the
        #guard's case without made him to sleep before).
        if MAC_GYVER.case_y == GUARD_POS_Y and MAC_GYVER.case_x == GUARD_POS_X:
            print("Game over")
            MOVE_ON = 0
    #Display refresh
    MAP_LVL_1.images_display()
    pygame.display.flip()

    #Win condition (if the character walks on the outdoor).
    if MAC_GYVER.case_y == DOOR_POS_Y and MAC_GYVER.case_x == DOOR_POS_X:
        print("You won")
        MOVE_ON = 0
