import pygame, sys, easygui, glob
import constants
from player import Player
from platform import Platform
from map import Map
from textfunctions import *
from camera import Camera
from button import Button

if pygame.joystick.get_count() > 0:
	controller = pygame.joystick.Joystick(0)
	controller.init()
else:
	controller = None

# In game text
titleText = centerText(constants.TITLE)
pausedText = centerText("Paused")
gameOverText = centerText("Game Over")
scoreText = ScoreText()

# Menu buttons
startButton = Button(constants.SCREEN_WIDTH/2, 304, "Start")
exitButton = Button(constants.SCREEN_WIDTH/2, 368, "Exit")


class Game:
	def __init__(self, mode):
		self.screen = pygame.display.get_surface()
		self.mode = mode
		self.camera = Camera(0, 0)
		
		self.level_list = glob.glob("resources/levels/level?.map")
		self.levelno = 0
		#print len(self.level_list)
		self.set_map(self.level_list[self.levelno])
		#self.set_map("resources/levels/level.map")
		#self.player = Player(0, 0, self.map)
		
		self.score = 0
		self.coins = 0
		self.lives = 3
		self.status = "normal"
		
	
	def update_screen(self):
		# Display images
		if self.mode == "menu":
			self.screen.fill(constants.BLACK)
			self.screen.blit(titleText.text, titleText.rect)
			self.screen.blit(startButton.image, startButton.rect)
			self.screen.blit(exitButton.image, exitButton.rect)
		elif self.mode == "game":
			self.screen.fill(constants.BLACK)
			self.screen.blit(self.map.background, (-self.camera.rect.x, -self.camera.rect.y))
			for coin in self.coin_list:
				self.screen.blit(coin.image, (coin.rect.x - self.camera.rect.x, coin.rect.y - self.camera.rect.y))
			for item in self.item_list:
				self.screen.blit(item.image, (item.rect.x - self.camera.rect.x, item.rect.y - self.camera.rect.y))
			self.screen.blit(self.player.image, (self.player.rect.x - self.camera.rect.x, self.player.rect.y - self.camera.rect.y))
			for enemy in self.enemy_list:
				self.screen.blit(enemy.image, (enemy.rect.x - self.camera.rect.x, enemy.rect.y - self.camera.rect.y))
			for fireball in self.fire_list:
				self.screen.blit(fireball.image, (fireball.rect.x - self.camera.rect.x, fireball.rect.y - self.camera.rect.y))
			for platform in self.platform_list:
				self.screen.blit(platform.image, (platform.rect.x - self.camera.rect.x, platform.rect.y - self.camera.rect.y))
			self.screen.blit(scoreText.text, scoreText.rect)
		elif self.mode == "paused":
			self.screen.blit(pausedText.text, pausedText.rect)
		elif self.mode == "gameover":
			self.screen.fill(constants.BLACK)
			self.screen.blit(gameOverText.text, gameOverText.rect)
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
				elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
					self.mode = "game"
				elif event.type == pygame.MOUSEBUTTONDOWN:
					self.mouse_click()
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
					elif event.key == pygame.K_z:
						self.player.shoot()
				elif (event.type == pygame.JOYBUTTONDOWN) and (controller != None):
					print "Button down"
					if event.button == 6:
						self.player.jump()
					elif event.button == 9:
						self.mode = "paused"
				elif event.type == pygame.JOYHATMOTION:
					print "Controll pad moved"
			if controller != None:
				if controller.get_hat(0)[0] < 0:
						self.player.facing = "l"
						self.player.change_x = -4
				elif controller.get_hat(0)[0] > 0:
						self.player.facing = "r"
						self.player.change_x = 4
					
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
				elif event.type == pygame.KEYDOWN:
					if event.button == 6:
						self.mode = "game"
		elif self.mode == "gameover":
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					if easygui.ynbox("Quit?"):
						self.terminate()
					else:
						pass
				elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.JOYBUTTONDOWN:
					self.__init__("menu")
	
	def run_logic(self):
		# Run the game
		if self.mode == "game":
			if self.lives <= 0:
				self.mode = "gameover"
			if self.coins >= 100:
				self.coins = 0
				self.lives += 1
			self.player.update()
			if self.player.rect.right > self.camera.rect.right - (constants.SCREEN_WIDTH/4):
				self.camera.move(self.player.change_x, 0)
			self.player.change_x = 0
			for enemy in self.enemy_list:
				enemy.update()
			for fireball in self.fire_list:
				fireball.update()
			scoreText.update(self.score, self.lives, self.coins)
	
	def set_map(self, map):
		self.map = Map(map, self)
		self.platform_list = self.map.platform_list
		self.enemy_list = self.map.enemy_list
		self.coin_list = self.map.coin_list
		self.item_list = self.map.item_list
		self.fire_list = self.map.fire_list
		self.camera.set_pos(0, 0)
		try:
			self.player = self.map.player
		except AttributeError:
			easygui.msgbox("The map doesn't have a player.")
			self.terminate()
			
	def mouse_click(self):
		if self.mode == "menu":
			if startButton.rect.collidepoint(pygame.mouse.get_pos()):
				self.mode = "game"
			elif exitButton.rect.collidepoint(pygame.mouse.get_pos()):
				self.terminate()
			
	def terminate(self):
		pygame.quit()
		sys.exit()