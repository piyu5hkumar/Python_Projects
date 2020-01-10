import random
from pygame import mixer
from elements import *

WELCOME_RUNNING = True
wecomeImg = pygame.image.load('src/welcome.png')
while WELCOME_RUNNING:
    SCREEN.blit(backgroundImg, (0, 0))
    SCREEN.blit(wecomeImg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            WELCOME_RUNNING = False

    pygame.display.update()

# print('BH', BOUNDARY_HEIGHT)
RUNNING = True
while RUNNING:

    # screen.fill((0, 0, 0))
    SCREEN.blit(backgroundImg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                PLAYER.X_change = -0.5
            if event.key == pygame.K_RIGHT:
                PLAYER.X_change = 0.5
            if event.key == pygame.K_SPACE:
                if BULLET.isShooted == False:
                    bulletSound = mixer.Sound('src/music/shoot.wav')
                    bulletSound.play()
                    BULLET.X = PLAYER.X
                    BULLET.isShooted = True
                    BULLET.Y_change = -0.8
        if event.type == pygame.KEYUP:
            PLAYER.X_change = 0
    PLAYER.playerMovement()
    eMovement()
    BULLET.shoot()
    collision()

    # pygame.draw.circle(SCREEN,(0,0,0),(int(BULLET.X)+ 25,int(BULLET.Y)),5)
    pygame.draw.line(SCREEN, (255, 0, 0), (0, BOUNDARY_HEIGHT), (SCREEN_WIDTH, BOUNDARY_HEIGHT), 10)
    if isGameOver():
        print('the game should pause now')
        SCREEN.blit(text.render("GAME OVER", True, (255, 0, 0)), (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        SCREEN.blit(text.render("FINAL SCORE :" + getPoints(), True, (255, 0, 0)), (SCREEN_WIDTH/2, (SCREEN_HEIGHT / 2)+30))
    else:
        score = text.render("SCORE : " + getPoints(), True, (255, 0, 0))
        SCREEN.blit(score, (0, 0))
    pygame.display.update()
