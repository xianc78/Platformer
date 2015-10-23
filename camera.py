import pygame
import constants

# In game camera.
class Camera:
	def __init__(self, x, y):
		self.rect = pygame.Rect(x, y, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
	
	def move(self, x, y):
		self.rect.x += x
		self.rect.y += y
		
	def set_pos(self, x, y):
		self.rect.x = x
		self.rect.y = y
		
	def get_pos(self):
		return [self.rect.x, self.rect.y]
		
	def update(self, target):
		self.rect.centerx = target.rect.centerx
		self.rect.centery = target.rect.centery