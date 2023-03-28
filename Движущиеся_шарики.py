import pygame
from pygame.draw import *
import random

pygame.init()

FPS = 60
WINDOW_SIZE = (1980, 1000)
screen = pygame.display.set_mode(WINDOW_SIZE)

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


balls = []


class Ball:
    def __init__(self):
        self.x = random.randint(100, 1880)
        self.y = random.randint(100, 900)
        self.r = random.randint(10, 100)
        self.color = COLORS[random.randint(0, 5)]
        self.move_x, self.move_y = [random.randint(-10, 10) for i in range(2)]

    def draw(self):
        circle(screen, self.color, (self.x, self.y), self.r)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    if len(balls) < 30:
        balls.append(Ball())
    for ball in balls:
        if WINDOW_SIZE[0]-ball.r <= ball.x or ball.x <= 0+ball.r:
            ball.move_x = 0 - ball.move_x
        if WINDOW_SIZE[1]-ball.r <= ball.y or ball.y <= 0+ball.r:
            ball.move_y = 0 - ball.move_y
        ball.x += ball.move_x
        ball.y += ball.move_y
        ball.draw()

    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
