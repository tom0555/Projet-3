"""Ressources are stocked here"""

#Useful attributes
ITEM1 = 63
ITEM2 = 64
ITEM3 = 65
F = 0
GUARDIAN = 4
WALL = 1
DOOR = 2
START = 3
MACDO = 5
#Tilemap's disposition
TILEMAP = [
				[F, WALL, F, F, WALL, F, WALL, WALL, F, F, WALL, F, F, WALL, F],
				[F, WALL, F, F, WALL, F, F, WALL, F, F, WALL, F, F, WALL, DOOR],
				[F, WALL, F, F, WALL, WALL, F, WALL, F, F, F, F, F, WALL, GUARDIAN],
				[F, WALL, F, F, WALL, F, F, WALL, F, WALL, WALL, F, F, WALL, F],
				[F, WALL, F, F, WALL, F, F, WALL, F, WALL, WALL, F, WALL, WALL, F],
				[F, F, F, F, WALL, F, F, WALL, F, F, WALL, WALL, F, WALL, F],
				[F, WALL, F, F, WALL, F, F, WALL, F, F, WALL, F, F, WALL, F],
				[F, WALL, F, F, F, F, F, F, F, F, WALL, F, F, WALL, F],
				[F, WALL, F, F, F, F, F, WALL, F, F, WALL, F, F, WALL, F],
				[F, WALL, F, F, WALL, WALL, F, WALL, F, F, WALL, F, F, WALL, F],
				[START, WALL, WALL, F, WALL, F, F, WALL, F, F, WALL, F, F, F, F],
				[F, WALL, F, WALL, WALL, F, F, WALL, F, F, WALL, F, F, F, F],
				[F, WALL, F, F, WALL, F, WALL, WALL, F, WALL, WALL, WALL, F, WALL, F],
				[F, WALL, F, F, WALL, F, WALL, WALL, F, WALL, F, F, F, WALL, F],
				[F, F, F, F, F, F, F, WALL, F, F, F, F, F, WALL, F],
				]

#Pics dictionnary
PICS = {
				WALL : "wall1.png",
				F : "F1.jpg",
				DOOR : "door.jpg",
				MACDO : "mac_gyver.png",
				GUARDIAN : "GUARDIAN.png",
				ITEM1 : "key1.jpg",
				ITEM2 : "key2.jpg",
				ITEM3 : "key3.jpg"
				}

#Window parameters

WINDOW_WIDHT = 645
WINDOW_HEIGHT = 480
SPRITE_HEIGHT = WINDOW_HEIGHT/15
SPRITE_WIDHT = WINDOW_WIDHT/15
SPRITES = 15
TITLE = "MAC"
ITEMS = 0
GUARD_POS_X = 14
GUARD_POS_Y = 2
DOOR_POS_X = 14
DOOR_POS_Y = 1
