import pygame
from pygame.draw import *

pygame.init()

FPS = 30

screen = pygame.display.set_mode((800, 800))

# Head
rect(screen, 'pink', (0, 0, 800, 800))
circle(screen, 'yellow', (400, 400), 200)
circle(screen, (0, 0, 0), (400, 400), 200, 3)

# Eyes
circle(screen, (255, 0, 0), (300, 350), 40)
circle(screen, (255, 0, 0), (500, 350), 30)
circle(screen, (0, 0, 0), (300, 350), 40, 2)
circle(screen, (0, 0, 0), (500, 350), 30, 2)
circle(screen, (0, 0, 0), (300, 350), 20)
circle(screen, (0, 0, 0), (500, 350), 15)

# Brows
polygon(screen, (0, 0, 0), [(360, 350), (372, 330),
                            (213, 230), (200, 250)])
polygon(screen, (0, 0, 0), [(600, 250), (612, 270),
                            (462, 340), (450, 320)])

# Mouth
rect(screen, (0, 0, 0), (300, 500, 200, 40))
clock = pygame.time.Clock()
finished = False

while not finished:
    pygame.display.flip()
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
