import pygame
import constants

class Player:
	def __init__(self, x, y, level):
		self.image = pygame.Surface([32, 32])
		self.image.fill(constants.RED)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.change_x = 0
		self.change_y = 0
		self.level = level
		
	def update(self):
		self.calc_grav()
		
		# Move the character horizontally and check for collisions.
		self.rect.x += self.change_x
		for platform in self.level.platform_list:
			if self.rect.colliderect(platform.rect):
					if self.change_x > 0:
						self.rect.right = platform.rect.left
					else:
						self.rect.left = platform.rect.right
						
		# Move the character vertically and check for collisions
		self.rect.y += self.change_y
		for platform in self.level.platform_list:
			if self.rect.colliderect(platform.rect):
					if self.change_y > 0:
						self.rect.bottom = platform.rect.top
					else:
						self.rect.top = platform.rect.bottom
					self.change_y = 0
		if self.rect.bottom > constants.SCREEN_HEIGHT:
			self.rect.bottom = constants.SCREEN_HEIGHT

	def jump(self):
		platform_hit_list = []
		self.rect.y += 2
		for platform in self.level.platform_list:
			if self.rect.colliderect(platform.rect):
				platform_hit_list.append(platform)
		self.rect.y -= 2
		if (len(platform_hit_list) > 0) or (self.rect.bottom == constants.SCREEN_HEIGHT):
			self.change_y = -10
		
	def animate(self):
		pass
	
	def calc_grav(self):
		if self.change_y == 0:
			self.change_y = 1
		else:
			self.change_y += constants.GRAVITY