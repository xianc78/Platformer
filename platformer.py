import pygame, sys
import constants
from game import Game
pygame.init()

screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption(constants.TITLE)
clock = pygame.time.Clock()
game = Game("menu")

def main():
	while True:
		game.update_screen()
		game.check_events()
		game.run_logic()
		clock.tick(constants.FPS)

if __name__ == "__main__":
	main()