import random
import datetime
from pygame import mixer
from characters_and_methods import *
from store_score_file import *
from user_details_file import *

INVALID_USER = True
while INVALID_USER:
    SCREEN.blit(backgroundImg, (0, 0))
    SCREEN.blit(text.render("ENTER USER NAME:", True, (255, 255, 0)), (SCREEN_WIDTH / 4, SCREEN_HEIGHT / 4 + 60))
    SCREEN.blit(text.render(USERNAME.get(), True, (0, 255, 0)), (SCREEN_WIDTH / 4, SCREEN_HEIGHT / 4 + 90))
    SCREEN.blit(text.render(USERNAME.error, True, (255, 0, 0)), (SCREEN_WIDTH / 4, SCREEN_HEIGHT / 4 + 120))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                USERNAME.delete()
            else:
                USERNAME.input(event.unicode)
            if event.key == pygame.K_RETURN and USERNAME.error == '':
                INVALID_USER = False

    pygame.display.update()

WELCOME_RUNNING = True
welcomeImg = pygame.image.load('src/images/welcome.png')
while WELCOME_RUNNING:
    SCREEN.blit(backgroundImg, (0, 0))
    SCREEN.blit(welcomeImg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            WELCOME_RUNNING = False

    pygame.display.update()

RUNNING = True
while RUNNING:
    SCREEN.blit(backgroundImg, (0, 0))
    SCREEN.blit(text.render('USER: ' + USERNAME.get(), True, (255, 255, 0)), (SCREEN_WIDTH - len(USERNAME) * 45, 0))
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
        date = datetime.datetime.now().date()
        user = USERNAME.get()
        score = getPoints()
        DATABASE.insertDB(user=user, score=int(score), date=date)

        SCREEN.blit(text.render(USERNAME.get(), True, (255, 255, 255)), (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 90))
        SCREEN.blit(text.render("GAME OVER", True, (255, 0, 0)), (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 50))
        SCREEN.blit(text.render("YOUR SCORE: " + getPoints(), True, (255, 0, 255)),
                    (SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 2) - 20))
        SCREEN.blit(text.render("MAX Score User: " + DATABASE.highScore()[0], True, (255, 255, 0)),
                    (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 10))
        SCREEN.blit(text.render("MAX Score: " + str(DATABASE.highScore()[1]), True, (255, 255, 0)),
                    (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 40))
        SCREEN.blit(text.render("(R) for retry", True, (0, 255, 0)), (SCREEN_WIDTH / 4, SCREEN_HEIGHT - 60))
        SCREEN.blit(text.render("(E) for Exit", True, (255, 0, 0)), (SCREEN_WIDTH / 4, SCREEN_HEIGHT - 30))

        GameOverProcedure()
    else:
        score = text.render("SCORE : " + getPoints(), True, (255, 0, 0))
        SCREEN.blit(score, (0, 0))
    pygame.display.update()
