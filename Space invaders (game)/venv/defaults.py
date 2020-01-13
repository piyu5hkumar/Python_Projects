import pygame

# initialize the pygame
pygame.init()

# create screen

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
GAMEOVER = False
text = pygame.font.Font('freesansbold.ttf', 32)
POINTS = 0

SCREEN = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])  # pass a list

# Title and Icon
pygame.display.set_caption("space invaders by PIYU")
icon = pygame.image.load('src/images/icon.png')
pygame.display.set_icon(icon)

# background
backgroundImg = pygame.image.load('src/images/BG.png').convert()

# boundary
BOUNDARY_HEIGHT = 7 * (SCREEN_HEIGHT / 8) - 60
