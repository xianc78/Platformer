import pygame, sys, ConfigParser, easygui
import constants
from platform import *
from player import Player
from enemy import *
from items import *
from fireball import FireBall


class Map():
	platform_list = None
	enemy_list = None
	coin_list = None
	item_list = None
	fire_list = None
	background = None
	music = None
	def __init__(self, file, game):
		self.confg = ConfigParser.RawConfigParser()
		self.file = file
		self.game = game
		self.platform_list = []
		self.enemy_list = []
		self.coin_list = []
		self.item_list = []
		self.fire_list = []
		try:
			self.confg.read(self.file)
		except FileError:
			easygui.msgbox(self.file + " does not exist.", constants.TITLE)
			pygame.quit()
			sys.exit()
		self.create_level()
		
	def create_level(self):
		# Load all the data from the file if it exists.
		try:
			self.limit = int(self.confg.get("meta", "limit")) * constants.TILE_WIDTH
		except ConfigParser.NoSectionError:
			easygui.msgbox("meta section does not exist in " + self.file + ".", constants.TITLE)
			pygame.quit()
			sys.exit()
		except ConfigParser.NoOptionError:
			easygui.msgbox("limit option does not exist in " + self.file + ".", constants.TITLE)
			pygame.quit()
			sys.exit()
		except ValueError:
			easygui.msgbox("limit must be a whole number.", constants.TITLE)
			pygame.quit()
			sys.exit()
		try:
			background = self.confg.get("meta", "background")
			self.background = pygame.image.load("resources/graphics/" + background)
		except ConfigParser.NoOptionError:
			easygui.msgbox("background option does not exist in " + self.file + ".", constants.TITLE)
			pygame.quit()
			sys.exit()
		except pygame.error:
			easygui.msgbox(background + " does not exist.", constants.TITLE)
			pygame.quit()
			sys.exit()
		try:
			self.layout = self.confg.get("map", "layout").split("\n")
		except ConfigParser.NoSectionError:
			easygui.msgbox("'map' section does not exist.", constants.TITLE)
			pygame.quit()
			sys.exit()
		except ConfigParser.NoOptionError:
			easygui.msgbox("'layout' option does not exist.", constants.TITLE)
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
				elif tile == "+":
					self.item_list.append(ExtraLife(x, y))
				elif tile == "f":
					self.item_list.append(FireFlower(x, y))
				elif tile == "?":
					self.platform_list.append(HiddenBlock(x, y, self))
				else:
					easygui.msgbox(tile + " is not a valid tile", constants.TITLE)
					pygame.quit()
					sys.exit()
				x += constants.TILE_WIDTH
			y += constants.TILE_HEIGHT
			x = 0
			
	def reset(self):
		self.game.set_map(self.file)