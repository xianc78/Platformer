import pygame, sys, easygui, glob
import constants
from player import Player
from platform import Platform
from map import Map

class Game:
	def __init__(self, mode):
		self.screen = pygame.display.get_surface()
		self.mode = mode
		
		level_list = glob.glob("resources/levels/level?.map")
		levelno = 0
		#print len(level_list)
		self.set_map(level_list[levelno])
		#self.set_map("resources/levels/level.map")
		#self.player = Player(0, 0, self.map)
		
		self.score = 0
		
	
	def update_screen(self):
		if self.mode == "menu":
			pass
		elif self.mode == "game":
			self.screen.fill(constants.BLACK)
			self.screen.blit(self.player.image, (self.player.rect.x, self.player.rect.y))
			for platform in self.platform_list:
				self.screen.blit(platform.image, (platform.rect.x, platform.rect.y))
		elif self.mode == "paused":
			pass
		pygame.display.update()
		
	def check_events(self):
		if self.mode == "game":
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					if easygui.ynbox("Quit?"):
						self.terminate()
					else:
						pass
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_UP:
						self.player.jump()
					elif event.key == pygame.K_p:
						self.mode = "paused"
			pressed = pygame.key.get_pressed()
			if pressed[pygame.K_LEFT]:
				self.player.facing = "l"
				self.player.change_x = -5
			elif pressed[pygame.K_RIGHT]:
				self.player.facing = "r"
				self.player.change_x = 5
		elif self.mode == "paused":
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					if easygui.ynbox("Quit?"):
						self.terminate()
					else:
						pass
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_p:
						self.mode = "game"
	
	def run_logic(self):
		if self.mode == "game":
			self.player.update()
			self.player.change_x = 0
	
	def set_map(self, map):
		self.map = Map(map)
		self.platform_list = self.map.platform_list
		try:
			self.player = self.map.player
		except AttributeError:
			easygui.msgbox("The map doesn't have a player.")
			self.terminate()
			
	def terminate(self):
		pygame.quit()
		sys.exit()