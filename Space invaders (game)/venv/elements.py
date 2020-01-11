import math
import random
from pygame import mixer
from defaults import *

GAMEOVER = False
text = pygame.font.Font('freesansbold.ttf', 32)
POINTS = 0


class MyPlayer:

    def __init__(self):
        self.playerImg = pygame.image.load('src/player.png')  # .convert()  don't convert it
        self.X = SCREEN_WIDTH / 2
        self.Y = 7 * SCREEN_HEIGHT / 8
        self.X_change = 0

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


PLAYER = MyPlayer()


class MyPlayerBullet:
    def __init__(self):
        self.bulletImg = pygame.image.load('src/bullet.png')  # .convert() 10*30
        self.X = 0
        self.Y = 7 * (SCREEN_HEIGHT / 8) - 30
        self.isShooted = False
        self.Y_change = 0

    def shoot(self):
        if self.isShooted and self.Y >= 0:
            self.Y += self.Y_change
            # print('bullet at', self.Y)
            SCREEN.blit(self.bulletImg, (self.X + 20, self.Y))
            # pygame.display.update()
        elif self.Y < 0:
            self.isShooted = False
            self.Y = 7 * (SCREEN_HEIGHT / 8) - 30


PLAYERBULLET = MyPlayerBullet()


class MyEnemyBullet:
    def __init__(self):
        self.img = pygame.image.load('src/enemy_fire.png')
        self.X = 0
        self.Y = 0
        self.isShooted = False

class MyEnemy:
    def __init__(self, enemy_number):
        self.img = pygame.image.load('src/enemy' + str(enemy_number) + '_48x48.png')
        self.X = random.randint(0, SCREEN_WIDTH - 50)
        self.Y = 1 * SCREEN_HEIGHT / 8
        self.X_change = 0.3
        self.Y_change = 50
        self.BULLET = MyEnemyBullet()
        self.isShooted = False
        self.flag = 0
        self.vertices = list()
        # print(self.enemyImg)
    def calculate_points(self,p1,p2):
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
            print(xnew, ynew)
        return all


    def shoot(self):
        if self.isShooted == False:
            self.isShooted = True
            p1 = (self.X + 24,self.Y + 48)
            p2 = (PLAYER.X + 24, SCREEN_HEIGHT)
            self.vertices = self.calculate_points(p1,p2)
        else :
            if self.flag < self.vertices.__len__():
                SCREEN.blit(self.BULLET.img, (self.vertices[self.flag][0] - 8, self.vertices[self.flag][1] - 8))
                self.flag += 1
            else:
                self.vertices = list()
                self.flag = 0
                self.isShooted = False

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
            print('game over')
            for e in ENEMYS:
                e.Y = -100
                e.X_change = 0
            global GAMEOVER
            GAMEOVER = True
            shipBlastSound = mixer.Sound('src/music/explosion.wav')
            shipBlastSound.play()
        self.X += self.X_change
        SCREEN.blit(self.img, (self.X, self.Y))

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
def collision():
    global POINTS
    for e in ENEMYS:
        if isCollided((e.X + 24, e.Y + 24), (PLAYERBULLET.X + 25, PLAYERBULLET.Y)):
            collisionSound = mixer.Sound('src/music/invaderkilled.wav')
            collisionSound.play()
            PLAYERBULLET.isShooted = False
            PLAYERBULLET.Y = 7 * (SCREEN_HEIGHT / 8) - 30
            # print("collison")
            e.X = 48
            e.Y = 1 * SCREEN_HEIGHT / 8
            e.X_change = 0.3
            POINTS += 1

def getPoints():
    return str(POINTS)


def isCollided(A, B):
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
    '''
    if math.ceil(distance) == 24:
        # print("distance is ", distance)
        return True
    else:
        return False



def isGameOver():
    return GAMEOVER

