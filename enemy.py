import pygame
import constants
from spritesheet_functions import SpriteSheet

class Enemy():
	image = None
	level = None
	game = None
	def update(self):
		if self.rect.colliderect(self.game.camera.rect):
			self.calc_grav()
			if self.change_x != 0:
				self.animate()
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
			'''
			if self.rect.colliderect(self.level.player.rect):
				if self.change_x > 0:
					self.rect.right = self.level.player.rect.left
				else:
					self.rect.left = self.level.player.rect.right
			'''
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
		elif self.rect.right <= self.game.camera.rect.left:
			self.level.enemy_list.remove(self)
		
	def calc_grav(self):
		if self.change_y == 0:
			self.change_y = 1
		else:
			self.change_y += constants.GRAVITY
		
class Enemy1(Enemy):
	frames = None
	def __init__(self, x, y, change_x, level):
		self.spritesheet = SpriteSheet("resources/graphics/enemy.bmp", (36, 50, 63))
		self.frames = []
		
		image = self.spritesheet.grab_image(0, 0, 16, 16)
		image = pygame.transform.scale2x(image)
		self.frames.append(image)
		image = self.spritesheet.grab_image(16, 0, 16, 16)
		image = pygame.transform.scale2x(image)
		self.frames.append(image)
		image = self.spritesheet.grab_image(32, 0, 16, 16)
		image = pygame.transform.scale2x(image)
		self.frames.append(image)
		
		self.index = 0
		self.MAX_FRAMES = 9
		self.image = self.frames[0]
		
		'''
		self.image = pygame.Surface([constants.TILE_WIDTH, constants.TILE_HEIGHT])
		self.image.fill(constants.RED)
		'''
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.level = level
		self.game = self.level.game
		self.change_x = change_x
		self.change_y = 0
		
	def animate(self):
		self.index += 1
		if self.index >= self.MAX_FRAMES:
			self.index = 0
		self.image = self.frames[self.index//3]
		