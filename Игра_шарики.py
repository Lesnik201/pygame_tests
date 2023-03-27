import pygame
from pygame.draw import *
from random import randint
import math

pygame.init()

FPS = 2
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

x, y, r = 0, 0, 0
score = 0


def new_ball():
    """Рисует новый шарик """
    global x, y, r
    x = randint(100, 1100)
    y = randint(100, 900)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)


def click(event):
    """Получение координат клика мышкой.
    Проверка попадания внутрь круга.
    Возвращает True или False"""
    global score
    mouth_x, mouth_y = event.pos
    leng = math.sqrt((mouth_x - x) ** 2 + (mouth_y - y) ** 2)
    if leng <= r:
        score += 10


def print_score(num_score):
    """Отображение количества очков"""
    font = pygame.font.Font(None, 30)
    text = font.render(f'Очки: {num_score}', True, (255, 255, 255))
    place = text.get_rect(center=(1150, 50))
    screen.blit(text, place)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event)

    new_ball()
    print_score(str(score))
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
