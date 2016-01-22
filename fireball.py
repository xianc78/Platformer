import pygame
import constants

class FireBall:
	def __init__(self, x, y, change_x, level):
		self.image = pygame.Surface([10, 10])
		self.image.fill(constants.RED)
		
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.centery = y
		
		self.change_x = change_x
		self.change_y = 0
		
		self.level = level
		
	def update(self):
		self.calc_grav()
		self.rect.x += self.change_x
		self.rect.y += self.change_y
		for platform in self.level.platform_list:
			if self.rect.colliderect(platform.rect):
				self.change_y *= -1
		
	def calc_grav(self):
		if self.change_y == 0:
			self.change_y = 1
		else:
			self.change_y += constants.GRAVITY