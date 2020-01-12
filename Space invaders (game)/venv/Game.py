import random
from pygame import mixer
from characters_and_methods import *

CLOCK = pygame.time.Clock()
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

    # SCREEN.fill((0, 0, 0))
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
                if PLAYER.BULLET.isShooted == False:
                    bulletSound = mixer.Sound('src/music/shoot.wav')
                    bulletSound.play()
                    PLAYER.BULLET.X = PLAYER.X
                    PLAYER.BULLET.isShooted = True
                    PLAYER.BULLET.Y_change = -0.8
            if event.key == pygame.K_r and isGameOver() == True:
                retry()
            if event.key == pygame.K_e and isGameOver() == True:
                RUNNING = False
        if event.type == pygame.KEYUP:
            PLAYER.X_change = 0
    PLAYER.playerMovement()
    eMovement()
    eFire()
    PLAYER.shoot()
    enemyHit()
    PlayerHit()

    # pygame.draw.circle(SCREEN,(0,0,0),(int(PLAYER.BULLET.X)+ 25,int(PLAYER.BULLET.Y)),5)
    pygame.draw.line(SCREEN, (255, 0, 0), (0, BOUNDARY_HEIGHT), (SCREEN_WIDTH, BOUNDARY_HEIGHT), 10)
    if isGameOver():
        SCREEN.blit(text.render("GAME OVER", True, (255, 255, 0)), (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        SCREEN.blit(text.render("FINAL SCORE :" + getPoints(), True, (255, 0, 255)),
                    (SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 2) + 30))
        SCREEN.blit(text.render("(R) for retry", True, (0, 255, 0)), (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 60))
        SCREEN.blit(text.render("(E) for Exit", True, (255, 0, 0)), (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 90))
        GameOverProcedure()
    else:
        score = text.render("SCORE : " + getPoints(), True, (255, 0, 0))
        SCREEN.blit(score, (0, 0))
    pygame.display.update()
