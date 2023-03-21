import pygame
from pygame.draw import *

pygame.init()

FPS = 30

screen = pygame.display.set_mode((1000, 1000))

rect(screen, "gray", (0, 0, 1000, 600))

# Moon
circle(screen, (255, 255, 255), (850, 150), 95)

ellipse(screen, (97, 131, 133), (600, 240, 800, 100))  # cloud 3
ellipse(screen, (30, 50, 50), (450, 360, 650, 100))  # cloud 4

# House
rect(screen, (56, 35, 15), (50, 360, 550, 700))
rect(screen, (92, 67, 43), (90, 360, 60, 240))
rect(screen, (92, 67, 43), (220, 360, 60, 240))
rect(screen, (92, 67, 43), (350, 360, 60, 240))
rect(screen, (92, 67, 43), (480, 360, 60, 240))

# Roof
rect(screen, (30, 30, 30), (370, 220, 20, 110))
polygon(screen, (0, 0, 0), [(0, 360), (100, 290), (540, 290), (660, 360)])
rect(screen, (30, 30, 30), (140, 210, 20, 110))
ellipse(screen, (43, 68, 69), (80, 170, 700, 100))  # cloud 2
ellipse(screen, (97, 131, 133), (430, 120, 550, 100))  # cloud 1
rect(screen, (30, 30, 30), (180, 160, 35, 170))
rect(screen, (30, 30, 30), (500, 220, 20, 110))

# Balcony
rect(screen, (43, 30, 30), (0, 605, 650, 70))
rect(screen, (43, 30, 30), (30, 520, 600, 30))
rect(screen, (43, 30, 30), (10, 550, 20, 70))  # First pillar
rect(screen, (43, 30, 30), (630, 550, 20, 70))  # Last pillar
rect(screen, (43, 30, 30), (90, 550, 40, 70))
rect(screen, (43, 30, 30), (220, 550, 40, 70))
rect(screen, (43, 30, 30), (350, 550, 40, 70))
rect(screen, (43, 30, 30), (500, 550, 40, 70))

# Windows
rect(screen, (24, 31, 20), (120, 800, 100, 120))
rect(screen, (24, 31, 20), (270, 800, 100, 120))
rect(screen, 'yellow', (420, 800, 100, 120))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
