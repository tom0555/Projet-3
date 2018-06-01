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
		"""Methode permettant de déplacer le personnage"""
		
		#Déplacement vers la droite
		if direction == 'right':
			#Pour ne pas dépasser l'écran
			if self.case_x < (SPRITES - 1):
				#On vérifie que la case de destination n'est pas un mur
				if self.tilemap[self.case_y][self.case_x+1] != 1:
					self.tilemap[self.case_y][self.case_x] = 0
					self.case_x += 1
					#Calcul de la position "réelle" en pixel
					self.x = self.case_x * SPRITE_HEIGHT
					self.tilemap[self.case_y][self.case_x] = 3
				elif self.tilemap[self.case_y][self.case_x+1] == 97 or 98 or 99:
					self.items = self.items+1
		#Déplacement vers la gauche
		if direction == 'left':
			if self.case_x > 0:
				if self.tilemap[self.case_y][self.case_x-1] != 1:
					self.tilemap[self.case_y][self.case_x] = 0
					self.case_x -= 1
					self.x = self.case_x * SPRITE_HEIGHT
					self.tilemap[self.case_y][self.case_x] = 3
				elif self.tilemap[self.case_y][self.case_x-1] == 97 or 98 or 99:
					self.items = self.items+1
		#Déplacement vers le haut
		if direction == 'up':
			if self.case_y > 0:
				if self.tilemap[self.case_y-1][self.case_x] != 1:
					self.tilemap[self.case_y][self.case_x] = 0
					print("test")
					print(self.tilemap[self.case_y][self.case_x])
					self.case_y -= 1
					self.y = self.case_y * SPRITE_WIDHT
					self.tilemap[self.case_y][self.case_x] = 3
					print(self.tilemap[self.case_y][self.case_x])
				elif self.tilemap[self.case_y-1][self.case_x] == 97 or 98 or 99:
					self.items = self.items+1
		#Déplacement vers le bas
		if direction == 'down':
			if self.case_y < (SPRITES - 1):
				if self.tilemap[self.case_y+1][self.case_x] != 1:
					self.tilemap[self.case_y][self.case_x] = 0
					self.case_y += 1
					self.y = self.case_y * SPRITE_WIDHT
					self.tilemap[self.case_y][self.case_x] = 3
				elif self.tilemap[self.case_y+1][self.case_x] == 97 or 98 or 99:
					self.items = self.items+1
		return self.items