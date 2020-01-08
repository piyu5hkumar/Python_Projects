import pygame

#initialize the pygame
pygame.init()

#create screen

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800


screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT]) #pass a list

#Title and Icon
pygame.display.set_caption("space invaders by PIYU")
icon = pygame.image.load('src/Space Invaders 3.png')
pygame.display.set_icon(icon)

#player
playerImg = pygame.image.load('src/player_48x48.png')
playerX = SCREEN_WIDTH/2
playerY = 7*SCREEN_HEIGHT/8
playerX_change = 0

def player(x, y):
    #blit means draw
    screen.blit(playerImg,(x,y))


#to hold window
RUNNING = True
while RUNNING:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
            print(playerX_change)
        if event.type == pygame.KEYUP:
                playerX_change = 0

    # print(playerX_change)
    playerX += playerX_change

    '''
        remember we have to stop it at 0,
        if we do it at screenwidth then it will first go out of screen
        and the come back at 0
    '''
    if playerX < 0:
        playerX = 0

    '''
        remember we have to stop it at screenwidth - 48,
        if we do it at screenwidth then it will first go out of screen
        and the come back at screenwidth-48
    '''
    if playerX > SCREEN_WIDTH - 48:
        playerX = SCREEN_WIDTH - 48
    #print(playerX)
    player(playerX,playerY)
    #we have to update it // compulsory
    pygame.display.update()