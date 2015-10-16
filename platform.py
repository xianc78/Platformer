import pygame
import constants

class Platform:
	def __init__(self, x, y, level):
		self.image = pygame.Surface([constants.TILE_WIDTH, constants.TILE_HEIGHT])
		self.image.fill(constants.WHITE)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y