import pygame

p1 = (800, 0)
p2 = (0, 600)
pygame.init()
screen = pygame.display.set_mode([800, 600])

fire = pygame.image.load('enemy_fire.png')
def get_vertex(p1, p2):
    print('h1')
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
        xnew = (ynew - y2)/m + x2
        i += 1
        print(xnew, ynew)
    return all


vertices = get_vertex(p1, p2)
length = vertices.__len__()
i=0
print(vertices)
while True:
    screen.fill((0, 0, 0))
    # screen.blit(fire,(0-16,0-16))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    # pygame.draw.line(screen, (255, 0, 0), p1, p2)

    # pygame.draw.circle(screen, (100 , 100, 255), v, 3)
    if i < length:
        screen.blit(fire, (vertices[i][0]-8,vertices[i][1]-8))
    i+=1
    pygame.display.update()
