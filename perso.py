import class_map
import ressources
import pygame, sys
from pygame.locals import *

class char :

	def __init__(self, droite, gauche, haut, bas, niveau):
		#Position du personnage en cases et en pixels
		self.case_x = 0
		self.case_y = 10
		self.x = 0
		self.y = 320
		#Niveau dans lequel le personnage se trouve 
		self.map = tilemap

	def move(self):
		"""Methode permettant de déplacer le personnage"""
		
		#Déplacement vers la droite
		if direction == 'right':
			#Pour ne pas dépasser l'écran
			if self.case_x < (SPRITES - 1):
				#On vérifie que la case de destination n'est pas un mur
				if self.map[self.case_y][self.case_x+1] != 1:
					#Déplacement d'une case
					self.case_x += 1
					#Calcul de la position "réelle" en pixel
					self.x = self.case_x * SPRITE_HEIGHT
		
		#Déplacement vers la gauche
		if direction == 'left':
			if self.case_x > 0:
				if self.map[self.case_y][self.case_x-1] != 1:
					self.case_x -= 1
					self.x = self.case_x * SPRITE_HEIGHT
		
		#Déplacement vers le haut
		if direction == 'up':
			if self.case_y > 0:
				if self.map[self.case_y-1][self.case_x] != 1:
					self.case_y -= 1
					self.y = self.case_y * SPRITE_HEIGHT
		
		#Déplacement vers le bas
		if direction == 'down':
			if self.case_y < (nombre_sprite_cote - 1):
				if self.map[self.case_y+1][self.case_x] != 1:
					self.case_y += 1
					self.y = self.case_y * SPRITE_HEIGHT