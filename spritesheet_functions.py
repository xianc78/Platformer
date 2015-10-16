import pygame
import constants
pygame.init()

class SpriteSheet:
	def __init__(self, image):
		self.sprite_sheet = pygame.image.load(image)
		
	def grab_image(self, x, y, w, h):
		image = pygame.Surface([w, h])
		image.blit(self.sprite_sheet, (0, 0), (x, y, w, h))
		image.set_colorkey(constants.BLACK)
		return image