import pygame
import constants
from textfunctions import fontObj

class Button():
	def __init__(self, x, y, text):
		self.image = fontObj.render(text, True, constants.WHITE, constants.BLUE)
		self.rect = self.image.get_rect()
		self.rect.centerx = x
		self.rect.centery = y