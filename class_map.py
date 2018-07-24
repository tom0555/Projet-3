"""class map"""
import random

import pygame

from ressources import WINDOW_HEIGHT
from ressources import WINDOW_WIDHT
from ressources import SPRITE_WIDHT
from ressources import SPRITE_HEIGHT
from ressources import PICS
from ressources import TILEMAP
from ressources import F
from ressources import WALL
from ressources import MACDO
from ressources import DOOR
from ressources import GUARDIAN
from ressources import ITEM1
from ressources import ITEM2
from ressources import ITEM3

class Map:
    """class map"""
    #Pygame initialization
    pygame.init()

    def __init__(self):
        #Window's size attribution
        self.window = pygame.display.set_mode((WINDOW_WIDHT, WINDOW_HEIGHT))
    #function used to place items at a random place.
    def random_item(self):
        """Define random item"""
        TILEMAP[random.randint(0, 5)][random.randint(2, 3)] = 99
        TILEMAP[random.randint(6, 11)][random.randint(8, 9)] = 98
        TILEMAP[random.randint(0, 3)][random.randint(11, 12)] = 97
    #function which is displaying the whole map on the screen.
    def images_display(self):
        """displaying method"""
        #Useful attributes to control the loop( y for lignes and x for columns).
        line = 0
        column = 0
        #Screen refresh
        pygame.display.flip()
        #Begining of the loop
        while line < 15:
            if TILEMAP[line][column] == 0: #0 = floor
                self.window.blit(pygame.image.load(PICS[F]).convert(),
                                 [column * SPRITE_WIDHT, line * SPRITE_HEIGHT])
                pygame.display.flip()
            elif TILEMAP[line][column] == 1: #1 = wall
                self.window.blit(pygame.image.load(PICS[WALL]).convert(),
                                 [column * SPRITE_WIDHT, line * SPRITE_HEIGHT])
                pygame.display.flip()
            elif TILEMAP[line][column] == 2: #2 = outdoor
                self.window.blit(pygame.image.load(PICS[DOOR]).convert(),
                                 [column * SPRITE_WIDHT, line * SPRITE_HEIGHT])
                pygame.display.flip()
            elif TILEMAP[line][column] == 3: #3 = mac gyver
                self.window.blit(pygame.image.load(PICS[MACDO]).convert(),
                                 [column * SPRITE_WIDHT, line * SPRITE_HEIGHT])
                pygame.display.flip()
            elif TILEMAP[line][column] == 4: #4 = guard
                self.window.blit(pygame.image.load(PICS[GUARDIAN]).convert(),
                                 [column * SPRITE_WIDHT, line * SPRITE_HEIGHT])
                pygame.display.flip()
            elif TILEMAP[line][column] == 99: #99 = first item
                self.window.blit(pygame.image.load(PICS[ITEM1]).convert(),
                                 [column * SPRITE_WIDHT, line * SPRITE_HEIGHT])
                pygame.display.flip()
            elif TILEMAP[line][column] == 98: #98 = second item
                self.window.blit(pygame.image.load(PICS[ITEM2]).convert(),
                                 [column * SPRITE_WIDHT, line * SPRITE_HEIGHT])
                pygame.display.flip()
            elif TILEMAP[line][column] == 97: #97 = third item
                self.window.blit(pygame.image.load(PICS[ITEM3]).convert(),
                                 [column * SPRITE_WIDHT, line * SPRITE_HEIGHT])
                pygame.display.flip()
            column += 1
            if column % 15 == 0: #Every 15 columns , drop down one line.
                line += 1
                column = 0
