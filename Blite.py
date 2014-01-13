import pygame, sys, math, time
from pygame.locals import *
from Player import Player


width = 1080
height = 810
size = width, height

pygame.init()

screen = pygame.display.set_mode(size)
bgColor = r,g,b = 0,0,0
bgImage = pygame.image.load("Resources/Screens/StartScreen.png")
bgRect = bgImage.get_rect()

start = False
controls = False

player = Player(("Resources/Player/Player.png"),(3,3), (80,107),(width/2, 0))

while True:
	bgImage = pygame.image.load("Resources/Screens/StartScreen.png")
	
	while not start:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
					start = True
				if event.key == pygame.K_c:
					controls = True
					bgImage = pygame.image.load("Resources/Screens/ControlScreen.png")

		screen.blit(bgImage, bgRect)
		pygame.display.flip()
		#clock.tick(60)
	
	while controls == True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					controls == False
		screen.blit(bgImage, bgRect)
		pygame.display.flip()
	
	while start == True:
		bgImage = pygame.image.load("Resources/Background/Background.png")
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_w or event.key == pygame.K_UP:
					player.direction("up")

				if event.key == pygame.K_s or event.key == pygame.K_DOWN:
					player.direction("down")

				if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
					player.direction("right")

				if event.key == pygame.K_a or event.key == pygame.K_LEFT:
					player.direction("left")

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_w or event.key == pygame.K_UP:
					player.direction("stop up")

				if event.key == pygame.K_s or event.key == pygame.K_DOWN:
					player.direction("stop down")

				if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
					player.direction("stop right")

				if event.key == pygame.K_a or event.key == pygame.K_LEFT:
					player.direction("stop left")
					
		player.update()
		player.collideWall(width, height)
		
		screen.fill(bgColor)
		screen.blit(bgImage, bgRect)		
		screen.blit(bgImage, bgRect)	
		screen.blit(player.image, player.rect)	
		pygame.display.flip()
		#clock.tick(60)