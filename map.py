import pygame, sys, ConfigParser, easygui
import constants
from platform import Platform
from player import Player

confg = ConfigParser.RawConfigParser()

class Map():
	platform_list = []
	enemy_list = []
	def __init__(self, file):
		self.file = file
		try:
			confg.read(self.file)
		except FileError:
			easygui.msgbox(self.file + " does not exist.", constants.TITLE)
			pygame.quit()
			sys.exit()
		self.create_level()
		
	def create_level(self):
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
					self.player = Player(x, y, self)
				else:
					easygui.msgbox(tile + " is not a valid tile", constants.TITLE)
					pygame.quit()
					sys.exit()
				x += constants.TILE_WIDTH
			y += constants.TILE_HEIGHT
			x = 0