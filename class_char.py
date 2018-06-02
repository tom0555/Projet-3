import class_map
from ressources import *
import pygame, sys
from pygame.locals import *

class char :

	def __init__(self, tilemap, items):
		#Position du personnage en cases et en pixels
		self.case_x = 0
		self.case_y = 10
		self.x = 0
		self.y = 320
		#Niveau dans lequel le personnage se trouve 
		self.tilemap = tilemap
		self.items = items

	def move(self, direction):
		#print(self.tilemap[self.case_y][self.case_x])
		if direction == 'right':
			#Pour ne pas dépasser l'écran
			if self.case_x < (SPRITES - 1):
				#On vérifie que la case de destination n'est pas un mur
				if self.tilemap[self.case_y][self.case_x+1] != 1:
					self.tilemap[self.case_y][self.case_x] = 0
					self.case_x += 1
					#Calcul de la position "réelle" en pixel
					if self.tilemap[self.case_y][self.case_x] == 97 or self.tilemap[self.case_y][self.case_x] == 98 or self.tilemap[self.case_y][self.case_x] == 99:
						self.items = self.items+1
					self.x = self.case_x * SPRITE_HEIGHT
					self.tilemap[self.case_y][self.case_x] = 3
		#Déplacement vers la gauche
		if direction == 'left':
			if self.case_x > 0:
				if self.tilemap[self.case_y][self.case_x-1] != 1:
					self.tilemap[self.case_y][self.case_x] = 0
					self.case_x -= 1
					if self.tilemap[self.case_y][self.case_x] == 97 or self.tilemap[self.case_y][self.case_x] == 98 or self.tilemap[self.case_y][self.case_x] == 99:
						self.items = self.items+1
					self.x = self.case_x * SPRITE_HEIGHT
					self.tilemap[self.case_y][self.case_x] = 3
		#Déplacement vers le haut
		if direction == 'up':
			if self.case_y > 0:
				if self.tilemap[self.case_y-1][self.case_x] != 1:
					self.tilemap[self.case_y][self.case_x] = 0
					self.case_y -= 1
					#print(self.tilemap[self.case_y][self.case_x])
					if self.tilemap[self.case_y][self.case_x] == 97 or self.tilemap[self.case_y][self.case_x] == 98 or self.tilemap[self.case_y][self.case_x] == 99:
						self.items = self.items+1
					self.y = self.case_y * SPRITE_WIDHT
					self.tilemap[self.case_y][self.case_x] = 3
					#print(self.tilemap[self.case_y][self.case_x])
		#Déplacement vers le bas
		if direction == 'down':
			if self.case_y < (SPRITES - 1):
				if self.tilemap[self.case_y+1][self.case_x] != 1:
					self.tilemap[self.case_y][self.case_x] = 0
					self.case_y += 1
					if self.tilemap[self.case_y][self.case_x] == 97 or self.tilemap[self.case_y][self.case_x] == 98 or self.tilemap[self.case_y][self.case_x] == 99:
						self.items = self.items+1
					self.y = self.case_y * SPRITE_WIDHT
					self.tilemap[self.case_y][self.case_x] = 3
				
		return self.items
	def sleep_guard(self, MAC_X , MAC_Y):
		self.MAC_X = MAC_X
		self.MAC_Y = MAC_Y
		#self.GUARD = 58
		self.tilemap[self.MAC_Y][self.MAC_X] = 0
		#return self.GUARD