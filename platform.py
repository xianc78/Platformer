import pygame
import constants

class Platform:
	def __init__(self, x, y, level):
		self.image = pygame.Surface([constants.TILE_WIDTH, constants.TILE_HEIGHT])
		image = pygame.image.load("resources/graphics/block.bmp")
		#image = pygame.transform.scale(image, (constants.TILE_WIDTH, constants.TILE_HEIGHT))
		self.image.blit(image, (0, 0))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		
class HiddenBlock:
	def __init__(self, x, y, level):
		self.image = pygame.Surface([constants.TILE_WIDTH, constants.TILE_HEIGHT])
		self.image.fill(constants.BLUE)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.active = True