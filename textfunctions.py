import pygame
import constants
pygame.init()

fontObj = pygame.font.SysFont("arial", 32)

class centerText:
	def __init__(self, text):
		self.text = fontObj.render(text, True, constants.WHITE)
		self.rect = self.text.get_rect()
		self.rect.center = (constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)
		
	def __str__(self):
		return self.text
		
class ScoreText:
	def __init__(self):
		self.text = fontObj.render("Score: " + " Lives: ", True, constants.WHITE)
		self.rect = self.text.get_rect()
		self.rect.x = 0
		self.rect.y = 0
		
	def update(self, score, lives, coins):
		self.text = fontObj.render("Score: " + str(score) + "   Lives: " + str(lives) + "  Coin(s): " +  str(coins), True, constants.WHITE)