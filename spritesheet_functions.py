import pygame
import constants

class SpriteSheet:
	def __init__(self, image, colorkey):
		self.sprite_sheet = pygame.image.load(image)
		self.colorkey = colorkey
		
	def grab_image(self, x, y, w, h):
		image = pygame.Surface([w, h])
		image.blit(self.sprite_sheet, (0, 0), (x, y, w, h))
		image.set_colorkey(self.colorkey)
		return image