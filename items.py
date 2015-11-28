import pygame
import constants

class Coin:
	def __init__(self, x, y):
		self.image = pygame.image.load("resources/graphics/coin.bmp")
		self.image.set_colorkey(constants.BLACK)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		
class ExtraLife:
	def __init__(self, x, y):
		self.image = pygame.image.load("resources/graphics/heart.bmp")
		self.image.set_colorkey(constants.BLACK)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y