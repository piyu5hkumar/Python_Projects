import random
from player_character import *

# enemy

e1 = pygame.image.load('src/enemy1_48x48.png')
e1X = 48
e1Y = 1 * SCREEN_HEIGHT / 8
e1X_change =  0.1
e1Y_change = 0


def enemy(x, y):
    SCREEN.blit(e1, (x, y))


WELCOME_RUNNING = True
wecomeImg = pygame.image.load('src/welcome.png')
while WELCOME_RUNNING:
    SCREEN.blit(backgroundImg, (0, 0))
    SCREEN.blit(wecomeImg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            WELCOME_RUNNING = False

    pygame.display.update()

RUNNING = True
while RUNNING:

    # screen.fill((0, 0, 0))
    SCREEN.blit(backgroundImg, (0, 0))

    # SCREEN.blit(bullet,(SCREEN_WIDTH/2,))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                PLAYER.X_change = -0.3
            if event.key == pygame.K_RIGHT:
                PLAYER.X_change = 0.3
            if event.key == pygame.K_SPACE:
                if BULLET.isShooted == False:
                    BULLET.X = PLAYER.X
                    BULLET.isShooted = True
                    BULLET.Y_change = -0.5
        if event.type == pygame.KEYUP:
            PLAYER.X_change = 0

    PLAYER.player_movement()
    if e1X < 0:
        e1X = 0
        e1X_change = 0.1
        e1Y_change = 15
        e1Y += e1Y_change
    if e1X > SCREEN_WIDTH - 48:
        e1X = SCREEN_WIDTH - 48
        e1X_change = -0.1
        e1Y_change = 11
        e1Y += e1Y_change

    e1X += e1X_change
    enemy(e1X, e1Y)

    pygame.draw.circle(SCREEN, (255, 255, 255), [int(e1X + 24), int(e1Y + 24)], 15)
    BULLET.shoot()
    pygame.draw.circle(SCREEN, (0, 0, 0), [int(BULLET.X + 25), int(BULLET.Y)], 5)
    if is_collided((e1X + 24, e1Y + 24), (BULLET.X + 25, BULLET.Y)):
        print("collison")
        e1X = random.randint(0,SCREEN_WIDTH - 48)
    pygame.display.update()
