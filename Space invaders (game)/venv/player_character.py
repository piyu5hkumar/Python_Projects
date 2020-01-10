import math
from defaults import *


class MyPlayer:
    # player
    playerImg = pygame.image.load('src/player1.png')  # .convert()  don't convert it
    X = SCREEN_WIDTH / 2
    Y = 7 * SCREEN_HEIGHT / 8
    X_change = 0

    def player_movement(self):
        self.X += self.X_change
        '''
            remember we have to stop it at 0,
            if we do it at screenwidth then it will first go out of screen
            and the come back at 0
        '''
        if self.X < 0:
            self.X = 0

        '''
            remember we have to stop it at screenwidth - 48,
            if we do it at screenwidth then it will first go out of screen
            and the come back at screenwidth-48
        '''
        if self.X > SCREEN_WIDTH - 48:
            self.X = SCREEN_WIDTH - 48
        # blit means draw
        SCREEN.blit(self.playerImg, (self.X, self.Y))


PLAYER = MyPlayer()


class MyBullet:
    bulletImg = pygame.image.load('src/bullet.png')  # .convert() 10*30
    X = 0
    Y = 7 * (SCREEN_HEIGHT / 8) - 30
    isShooted = False
    Y_change = 0

    def shoot(self):
        if self.isShooted and self.Y >= 0:
            self.Y += self.Y_change
            # print('bullet at', self.Y)
            SCREEN.blit(self.bulletImg, (self.X + 20, self.Y))
            # pygame.display.update()
        elif self.Y < 0:
            self.isShooted = False
            self.Y = 7 * (SCREEN_HEIGHT / 8) - 30


BULLET = MyBullet()

font = pygame.font.Font('freesansbold.ttf', 32)


def is_collided(A, B):
    global font
    distance = math.sqrt(math.pow(A[0] - B[0], 2) + math.pow(A[1] - B[1], 2))
    score = font.render(str(distance), True, (255, 255, 255))
    scoreX = font.render("x gap = " + str(A[0] - B[0]), True, (255, 255, 255))
    bulletX = font.render("bullet x = " + str(B[0]), True, (255, 255, 255))
    enemyX = font.render("enemy x = " + str(A[0]), True, (255, 255, 255))
    SCREEN.blit(score, (0, 0))
    SCREEN.blit(scoreX, (0, 20))
    SCREEN.blit(bulletX, (0, 40))
    SCREEN.blit(enemyX, (0, 60))
    pygame.draw.line(SCREEN, (255, 0, 0), (A[0], A[1]), (B[0], B[1]))
    if math.ceil(distance) == 24:
        print("distance is ", distance)
        return True
    else:
        return False
