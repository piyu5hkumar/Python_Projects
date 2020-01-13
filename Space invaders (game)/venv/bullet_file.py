from defaults import *


class MyBullet:
    def __init__(self, imgFile):
        self.img = pygame.image.load(imgFile)  # .convert() 10*30
        self.X = 0
        self.Y = 7 * (SCREEN_HEIGHT / 8) - 30
        self.isShooted = False
        self.Y_change = 0
        self.error = ''
