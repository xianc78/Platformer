import pygame
import constants

class Enemy():
	image = None
	level = None
	def update(self):
		self.calc_grav()
		self.rect.x += self.change_x
		for platform in self.level.platform_list:
			if self.rect.colliderect(platform.rect):
					if self.change_x > 0:
						self.rect.right = platform.rect.left
					else:
						self.rect.left = platform.rect.right
		for enemy in self.level.enemy_list:
			if self.rect.colliderect(enemy.rect) and enemy != self:
				if self.change_x > 0:
					self.rect.right = enemy.rect.left
				else:
					self.rect.left = enemy.rect.right
		if self.rect.colliderect(self.level.player.rect):
			if self.change_x > 0:
				self.rect.right = self.level.player.rect.left
			else:
				self.rect.left = self.level.player.rect.right
		self.rect.y += self.change_y
		for platform in self.level.platform_list:
			if self.rect.colliderect(platform.rect):
					if self.change_y > 0:
						self.rect.bottom = platform.rect.top
					else:
						self.rect.top = platform.rect.bottom
					self.change_y = 0
		if self.rect.top > constants.SCREEN_HEIGHT:
			self.level.enemy_list.remove(self)
		
	def calc_grav(self):
		if self.change_y == 0:
			self.change_y = 1
		else:
			self.change_y += constants.GRAVITY
		
class Enemy1(Enemy):
	def __init__(self, x, y, change_x, level):
		self.image = pygame.Surface([constants.TILE_WIDTH, constants.TILE_HEIGHT])
		self.image.fill(constants.RED)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.level = level
		self.change_x = change_x
		self.change_y = 0
		