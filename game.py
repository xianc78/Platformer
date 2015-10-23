import pygame, sys, easygui, glob
import constants
from player import Player
from platform import Platform
from map import Map
from textfunctions import *
from camera import Camera

titleText = centerText(constants.TITLE)
pausedText = centerText("Paused")
levelClearText = centerText("Level Cleared")

class Game:
	def __init__(self, mode):
		self.screen = pygame.display.get_surface()
		self.mode = mode
		self.camera = Camera(0, 0)
		
		self.level_list = glob.glob("resources/levels/level?.map")
		self.levelno = 0
		#print len(level_list)
		self.set_map(self.level_list[self.levelno])
		#self.set_map("resources/levels/level.map")
		#self.player = Player(0, 0, self.map)
		
		self.score = 0
		
	
	def update_screen(self):
		# Display images
		if self.mode == "menu":
			self.screen.blit(titleText.text, titleText.rect)
		elif self.mode == "game":
			self.screen.fill(constants.BLACK)
			self.screen.blit(self.player.image, (self.player.rect.x - self.camera.rect.x, self.player.rect.y - self.camera.rect.y))
			for platform in self.platform_list:
				self.screen.blit(platform.image, (platform.rect.x - self.camera.rect.x, platform.rect.y - self.camera.rect.y))
		elif self.mode == "paused":
			self.screen.blit(pausedText.text, pausedText.rect)
		pygame.display.update()
		
	def check_events(self):
		# Check for in game events
		if self.mode == "menu":
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					if easygui.ynbox("Quit?"):
						self.terminate()
					else:
						pass
				elif event.type == pygame.KEYDOWN:
					self.mode = "game"
		elif self.mode == "game":
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
				self.player.change_x = -4
			elif pressed[pygame.K_RIGHT]:
				self.player.facing = "r"
				self.player.change_x = 4
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
		# Run the game
		if self.mode == "game":
			self.player.update()
			if self.player.rect.right > constants.SCREEN_WIDTH - (constants.SCREEN_WIDTH/4):
				self.camera.move(self.player.change_x, 0)
			self.player.change_x = 0
	
	def set_map(self, map):
		self.map = Map(map, self)
		self.platform_list = self.map.platform_list
		self.camera.set_pos(0, 0)
		try:
			self.player = self.map.player
		except AttributeError:
			easygui.msgbox("The map doesn't have a player.")
			self.terminate()
			
	def terminate(self):
		pygame.quit()
		sys.exit()