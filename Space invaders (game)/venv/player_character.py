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
            pygame.display.update()
        elif self.Y < 0:
            self.isShooted = False
            self.Y = 7 * (SCREEN_HEIGHT / 8) - 30

    def is_collided(self, Xmin, Ymin):
        Xmax = Xmin + 48
        Ymax = Ymin + 48

        if Xmin <= self.X and Xmax >= self.X and Ymin - self.Y == 0:
            print("collison occur")
            print("e Y",Ymin)
            print("b Y",self.Y)


BULLET = MyBullet()


def is_collided(a, b, c):
    pass
# if math.sqrt(math.pow(a-c.X , 2)+math.pow(b-c.Y, 2)) == 0:
#     print('collided')
# if c.X>=a and c.X<=a+48 and
