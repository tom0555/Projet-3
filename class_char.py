"""class character"""
import pygame
from ressources import *
class char:
    """class char"""
    def __init__(self, tilemap, items):
        #Character's position in cases and pixels.
        self.case_x = 0
        self.case_y = 10
        self.x_pixel = 0
        self.y_pixel = 320
        #Recuperation of the main's parameters
        self.tilemap = tilemap
        self.items = items
    #Function to make the character to be able to move in the right direction we want.
    def move(self, direction):
        """def move"""
        if direction == 'right':
            #If character doesn't move out of the screen while moving right.
            if self.case_x < (SPRITES - 1):
                #Checking if the next place wanted isn't a wall.
                if self.tilemap[self.case_y][self.case_x + 1] != 1:
                    #Replacing the character's position by the original place which was floor.
                    self.tilemap[self.case_y][self.case_x] = 0
                    #Moving on by 1 case.
                    self.case_x += 1
                    #Checking if the actual position isn't an item position.
                    if self.tilemap[self.case_y][self.case_x] == 97 or self.tilemap[self.case_y][self.case_x] == 98 or self.tilemap[self.case_y][self.case_x] == 99:
                        #If yes , we add one item to our count.
                        self.items = self.items + 1
                    #Calculation of pixel's position.
                    self.x_pixel = self.case_x * SPRITE_WIDHT
                    #Attributing our character in that position.
                    self.tilemap[self.case_y][self.case_x] = 3
        #Move to the left.
        if direction == 'left':
            if self.case_x > 0:
                if self.tilemap[self.case_y][self.case_x - 1] != 1:
                    self.tilemap[self.case_y][self.case_x] = 0
                    self.case_x -= 1
                    if self.tilemap[self.case_y][self.case_x] == 97 or self.tilemap[self.case_y][self.case_x] == 98 or self.tilemap[self.case_y][self.case_x] == 99:
                        self.items = self.items + 1
                    self.x_pixel = self.case_x * SPRITE_WIDHT
                    self.tilemap[self.case_y][self.case_x] = 3
        #Move up
        if direction == 'up':
            if self.case_y > 0:
                if self.tilemap[self.case_y - 1][self.case_x] != 1:
                    self.tilemap[self.case_y][self.case_x] = 0
                    self.case_y -= 1
                    if self.tilemap[self.case_y][self.case_x] == 97 or self.tilemap[self.case_y][self.case_x] == 98 or self.tilemap[self.case_y][self.case_x] == 99:
                        self.items = self.items + 1
                    self.y_pixel = self.case_y * SPRITE_HEIGHT
                    self.tilemap[self.case_y][self.case_x] = 3
        #Move down
        if direction == 'down':
            if self.case_y < (SPRITES - 1):
                if self.tilemap[self.case_y + 1][self.case_x] != 1:
                    self.tilemap[self.case_y][self.case_x] = 0
                    self.case_y += 1
                    if self.tilemap[self.case_y][self.case_x] == 97 or self.tilemap[self.case_y][self.case_x] == 98 or self.tilemap[self.case_y][self.case_x] == 99:
                        self.items = self.items + 1
                    self.y_pixel = self.case_y * SPRITE_HEIGHT
                    self.tilemap[self.case_y][self.case_x] = 3
        #Returning the number of item we've got so far.
        return self.items
    #Function to make the guard sleep.
    def sleep_guard(self, mac_x, mac_y):
        #Recuperation of the guard position.
        self.mac_x = mac_x
        self.mac_y = mac_y
        #sleep the guard by making him disapear with attributing floor case on his position.
        self.tilemap[self.mac_y][self.mac_x] = 0
        