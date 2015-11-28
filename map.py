import pygame, sys, ConfigParser, easygui
import constants
from platform import Platform
from player import Player
from enemy import *
from items import *

confg = ConfigParser.RawConfigParser()

class Map():
	platform_list = None
	enemy_list = None
	background = None
	def __init__(self, file, game):
		self.file = file
		self.game = game
		self.platform_list = []
		self.enemy_list = []
		self.coin_list = []
		try:
			confg.read(self.file)
		except FileError:
			easygui.msgbox(self.file + " does not exist.", constants.TITLE)
			pygame.quit()
			sys.exit()
		self.create_level()
		
	def create_level(self):
		# Load all the data from the file if it exists.
		try:
			self.limit = int(confg.get("meta", "limit")) * constants.TILE_WIDTH
		except ConfigParser.NoSectionError:
			easygui.msgbox("meta section does not exist in " + self.file + ".")
			pygame.quit()
			sys.exit()
		except ConfigParser.NoOptionError:
			easygui.msgbox("limit option does not exist in " + self.file + ".")
			pygame.quit()
			sys.exit()
		except ValueError:
			easygui.msgbox("limit must be a whole number.")
			pygame.quit()
			sys.exit()
		try:
			self.layout = confg.get("map", "layout").split("\n")
		except ConfigParser.NoSectionError:
			easygui.msgbox("map section does not exist.", constants.TITLE)
			pygame.quit()
			sys.exit()
		except ConfigParser.NoOptionError:
			easygui.msgbox("layout option does not exist.", constants.TITLE)
			pygame.quit()
			sys.exit()
			
		x = y = 0
		for row in self.layout:
			for tile in row:
				if tile == ".":
					pass
				elif tile == "#":
					self.platform_list.append(Platform(x, y, self))
				elif tile == "@":
					self.player = Player(x, y, "r", self)
				elif tile == "e":
					self.enemy_list.append(Enemy1(x, y, -4, self))
				elif tile == "$":
					self.coin_list.append(Coin(x, y))
				else:
					easygui.msgbox(tile + " is not a valid tile", constants.TITLE)
					pygame.quit()
					sys.exit()
				x += constants.TILE_WIDTH
			y += constants.TILE_HEIGHT
			x = 0
			
	def reset(self):
		self.game.set_map(self.file)