from bullet_file import *
import random
import math
from pygame import mixer


class MyPlayer:

    def __init__(self):
        self.playerImg = pygame.image.load('src/images/player.png')  # .convert()  don't convert it
        self.X = SCREEN_WIDTH / 2
        self.Y = 7 * SCREEN_HEIGHT / 8
        self.X_change = 0
        self.BULLET = MyBullet('src/images/bullet.png')

    def playerMovement(self):
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

    def shoot(self):
        if self.BULLET.isShooted and self.BULLET.Y >= 0:
            self.BULLET.Y += self.BULLET.Y_change
            SCREEN.blit(self.BULLET.img, (self.BULLET.X + 20, self.BULLET.Y))
        elif self.BULLET.Y < 0:
            self.BULLET.isShooted = False
            self.BULLET.Y = 7 * (SCREEN_HEIGHT / 8) - 30


PLAYER = MyPlayer()


class MyEnemy:
    def __init__(self, enemy_number):
        self.img = pygame.image.load('src/images/enemy' + str(enemy_number) + '_48x48.png')
        self.X = random.randint(0, SCREEN_WIDTH - 50)
        self.Y = 1 * SCREEN_HEIGHT / 8
        self.X_change = 0.3
        self.Y_change = 50
        self.BULLET = MyBullet('src/images/enemy_fire.png')
        self.isShooted = False
        self.flag = 0
        self.vertices = list()
        # print(self.enemyImg)

    def enemyMovement(self):
        if self.X < 0:
            self.X = 0
            self.X_change = 0.3
            self.Y += self.Y_change
        if self.X > SCREEN_WIDTH - 48:
            self.X = SCREEN_WIDTH - 48
            self.X_change = - 0.3
            self.Y += self.Y_change
        if self.Y + 48 >= BOUNDARY_HEIGHT:
            global GAMEOVER
            GAMEOVER = True

        self.X += self.X_change
        SCREEN.blit(self.img, (self.X, self.Y))

    def calculate_points(self, p1, p2):
        all = list()
        factor = 0.1
        x1, y1 = p1[0], p1[1]
        x2, y2 = p2[0], p2[1]

        m = (y2 - y1) / (x2 - x1)
        xnew, ynew = x1, y1
        i = 1
        while ynew <= y2:
            all.append((int(xnew), int(ynew)))
            ynew = i * factor + y1
            xnew = (ynew - y2) / m + x2
            i += 1
            # print(xnew, ynew)
        return all

    def shoot(self):
        if self.isShooted == False and random.randint(1, 1000) == 5:
            self.isShooted = True
            p1 = (self.X + 24, self.Y + 48)
            p2 = (PLAYER.X + 24, SCREEN_HEIGHT)
            self.vertices = self.calculate_points(p1, p2)
        else:
            if self.flag < self.vertices.__len__():
                self.BULLET.X = self.vertices[self.flag][0] - 8
                self.BULLET.Y = self.vertices[self.flag][1] - 8
                SCREEN.blit(self.BULLET.img, (self.BULLET.X, self.BULLET.Y))
                self.flag += 1
            else:
                self.vertices = list()
                self.flag = 0
                self.isShooted = False


ENEMYS = list()

for i in range(1, 5):
    e = MyEnemy(i)
    ENEMYS.append(e)


def eMovement():
    for e in ENEMYS:
        # '''
        # for debugging purposes
        # pygame.draw.circle(SCREEN, (255, 255, 255), [int(e.X), int(e.Y + 48)], 5)
        # '''
        e.enemyMovement()


def eFire():
    for e in ENEMYS:
        e.shoot()


def enemyHit():
    global POINTS
    for e in ENEMYS:
        if isCollidedEnemy((e.X + 24, e.Y + 24), (PLAYER.BULLET.X + 25, PLAYER.BULLET.Y)):
            collisionSound = mixer.Sound('src/music/invaderkilled.wav')
            collisionSound.play()
            PLAYER.BULLET.isShooted = False
            PLAYER.BULLET.Y = 7 * (SCREEN_HEIGHT / 8) - 30
            # print("collison")
            e.X = 48
            e.Y = 1 * SCREEN_HEIGHT / 8
            e.X_change = 0.3
            global POINTS
            POINTS += 1


def isCollidedEnemy(A, B):
    # global text
    distance = math.sqrt(math.pow(A[0] - B[0], 2) + math.pow(A[1] - B[1], 2))
    '''
    #for debugging purposes
    score = text.render(str(distance), True, (255, 255, 255))
    scoreX = text.render("x gap = " + str(A[0] - B[0]), True, (255, 255, 255))
    bulletX = text.render("bullet x = " + str(B[0]), True, (255, 255, 255))
    enemyX = text.render("enemy x = " + str(A[0]), True, (255, 255, 255))
    SCREEN.blit(score, (0, 0))
    SCREEN.blit(scoreX, (0, 20))
    SCREEN.blit(bulletX, (0, 40))
    SCREEN.blit(enemyX, (0, 60))
    pygame.draw.line(SCREEN, (255, 0, 0), (A[0], A[1]), (B[0], B[1]))
    # '''
    if math.ceil(distance) == 24:
        # print("distance is ", distance)
        return True
    else:
        return False


def PlayerHit():
    for e in ENEMYS:
        if isCollidedPlayer((e.BULLET.X + 8, e.BULLET.Y + 8), (PLAYER.X + 24, PLAYER.Y + 24)):
            # print('player hit')
            global GAMEOVER
            GAMEOVER = True


def isCollidedPlayer(A, B):
    distance = math.sqrt(math.pow(A[0] - B[0], 2) + math.pow(A[1] - B[1], 2))
    # pygame.draw.line(SCREEN, (0, 0, 255), (A[0], A[1]), (B[0], B[1]))
    if math.ceil(distance) == 32:
        return True
    else:
        return False


def getPoints():
    return str(POINTS)


def isGameOver():
    return GAMEOVER


def GameOverProcedure():
    if not hasattr(GameOverProcedure, "played"):
        GameOverProcedure.played = False

    for e in ENEMYS:
        e.Y = -100
        e.X_change = 0
        e.flag = float('inf')
        e.vertices = list()
        e.BULLET.Y

    if GameOverProcedure.played == False:
        shipBlastSound = mixer.Sound('src/music/explosion.wav')
        shipBlastSound.play()
        GameOverProcedure.played = True


def retry():
    global GAMEOVER
    GAMEOVER = False

    global POINTS
    POINTS = 0

    global ENEMYS
    ENEMYS = list()
    for i in range(1, 5):
        e = MyEnemy(i)
        ENEMYS.append(e)

    GameOverProcedure.played = False
    # global PLAYER
    # PLAYER = MyPlayer()
