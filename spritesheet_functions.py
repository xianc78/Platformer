import pygame, sys, easygui
import constants

class SpriteSheet:
	def __init__(self, image, colorkey):
		try:
			self.sprite_sheet = pygame.image.load(image)
		except ValueError:
			msgbox(image + " doesn't exist.")
			pygame.quit()
			sys.exit()
		self.colorkey = colorkey
		
	def grab_image(self, x, y, w, h):
		image = pygame.Surface([w, h])
		image.blit(self.sprite_sheet, (0, 0), (x, y, w, h))
		image.set_colorkey(self.colorkey)
		return image