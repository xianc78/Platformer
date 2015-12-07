import pygame
import constants, spritesheet_functions
from platform import *
from items import *

class Player:
	frames_l = []
	frames_r = []
	def __init__(self, x, y, facing, level):
		# Create the image
		self.spritesheet = spritesheet_functions.SpriteSheet("resources/graphics/player.bmp", constants.WHITE)
		
		image = self.spritesheet.grab_image(0, 16, 16, 16)
		image = pygame.transform.scale2x(image)
		self.frames_l.append(image)
		
		image = self.spritesheet.grab_image(48, 16, 16, 16)
		image = pygame.transform.scale2x(image)
		self.frames_l.append(image)
		
		image = self.spritesheet.grab_image(112, 16, 16, 16)
		image = pygame.transform.scale2x(image)
		self.frames_r.append(image)
		
		image = self.spritesheet.grab_image(64, 16, 16, 16)
		image = pygame.transform.scale2x(image)
		self.frames_r.append(image)
		
		self.index = 0
		self.MAX_FRAMES = 12
		self.facing = facing
		self.animate()
		
		# Set the coordinates
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		
		# Set the speed to 0
		self.change_x = 0
		self.change_y = 0
		
		# Set the level and game
		self.level = level
		self.game = self.level.game
		
	def update(self):
		self.calc_grav()
		if self.change_x != 0:
			self.animate()
		
		# Move the character horizontally and check for collisions.
		self.rect.x += self.change_x
		for platform in self.level.platform_list:
			if self.rect.colliderect(platform.rect):
					if self.change_x > 0:
						self.rect.right = platform.rect.left
					else:
						self.rect.left = platform.rect.right
		for enemy in self.level.enemy_list:
			if self.rect.colliderect(enemy.rect):
				self.die()
		for coin in self.level.coin_list:
			if self.rect.colliderect(coin.rect):
				self.level.coin_list.remove(coin)
				self.game.coins += 1
				self.game.score += 200
		for item in self.level.item_list:
			if self.rect.colliderect(item.rect):
				self.level.item_list.remove(item)
				if isinstance(item, ExtraLife):
					self.game.lives += 1
			'''
				if self.change_x > 0:
					self.rect.right = enemy.rect.left
				else:
					self.rect.left = enemy.rect.right
			'''
		if self.rect.right > self.level.limit:
			self.game.levelno += 1
			try:
				self.game.set_map(self.game.level_list[self.game.levelno])
			except IndexError:
				self.game.__init__("menu")
		elif self.rect.left < 0:
			self.rect.left = 0
						
		# Move the character vertically and check for collisions
		self.rect.y += self.change_y
		for platform in self.level.platform_list:
			if self.rect.colliderect(platform.rect):
					if self.change_y > 0:
						self.rect.bottom = platform.rect.top
					else:
						self.rect.top = platform.rect.bottom
						if isinstance(platform, HiddenBlock):
							self.game.coins += 1
							self.game.score += 200
							self.level.platform_list.remove(platform)
					self.change_y = 0
		for enemy in self.level.enemy_list:
			if self.rect.colliderect(enemy.rect):
				if self.change_y > 0:
					self.level.enemy_list.remove(enemy)
					self.game.score += 100
				else:
					self.die()
		if self.rect.top > constants.SCREEN_HEIGHT:
			self.die()
			#self.rect.bottom = constants.SCREEN_HEIGHT

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
		self.index += 1
		if self.index >= self.MAX_FRAMES:
			self.index = 0
		if self.facing == "r":
			self.image = self.frames_r[self.index//6]
		else:
			self.image = self.frames_l[self.index//6]
	
	def calc_grav(self):
		if self.change_y == 0:
			self.change_y = 1
		else:
			self.change_y += constants.GRAVITY
			
	def die(self):
		self.game.lives -= 1
		self.game.update_screen()
		self.level.reset()