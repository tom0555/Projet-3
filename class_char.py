import class_map
import os
import sys
from ressources import *
import pygame, sys
from pygame.locals import *

class char :

	def __init__(self, tilemap, items):
		#Character's position in cases and pixels.
		self.case_x = 0
		self.case_y = 10
		self.x = 0
		self.y = 320
		#Recuperation of the main's parameters
		self.tilemap = tilemap
		self.items = items
	#Function to make the character to be able to move in the right direction we want.
	def move(self, direction):
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
					self.x = self.case_x * SPRITE_WIDHT
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
					self.x = self.case_x * SPRITE_WIDHT
					self.tilemap[self.case_y][self.case_x] = 3
		#Move up
		if direction == 'up':
			if self.case_y > 0:
				if self.tilemap[self.case_y - 1][self.case_x] != 1:
					self.tilemap[self.case_y][self.case_x] = 0
					self.case_y -= 1
					if self.tilemap[self.case_y][self.case_x] == 97 or self.tilemap[self.case_y][self.case_x] == 98 or self.tilemap[self.case_y][self.case_x] == 99:
						self.items = self.items + 1
					self.y = self.case_y * SPRITE_HEIGHT
					self.tilemap[self.case_y][self.case_x] = 3
		#Move down
		if direction == 'down':
			if self.case_y < (SPRITES - 1):
				if self.tilemap[self.case_y + 1][self.case_x] != 1:
					self.tilemap[self.case_y][self.case_x] = 0
					self.case_y += 1
					if self.tilemap[self.case_y][self.case_x] == 97 or self.tilemap[self.case_y][self.case_x] == 98 or self.tilemap[self.case_y][self.case_x] == 99:
						self.items = self.items + 1
					self.y = self.case_y * SPRITE_HEIGHT
					self.tilemap[self.case_y][self.case_x] = 3
		#Returning the number of item we've got so far.
		return self.items
	#Function to make the guard sleep.
	def sleep_guard(self, MAC_X , MAC_Y):
		#Recuperation of the guard position.
		self.MAC_X = MAC_X
		self.MAC_Y = MAC_Y
		#sleep the guard by making him disapear with attributing floor case on his position.
		self.tilemap[self.MAC_Y][self.MAC_X] = 0