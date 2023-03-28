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

ball_x, ball_y, ball_r = 0, 0, 0
score = 0


def new_ball():
    """Рисует новый шарик """
    global ball_x, ball_y, ball_r
    ball_x = randint(100, 1100)
    ball_y = randint(100, 900)
    ball_r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (ball_x, ball_y), ball_r)


def click(event):
    """Получение координат клика мышкой.
    Проверка попадания внутрь круга.
    """
    global score
    mouse_x, mouse_y = event.pos
    leng = math.sqrt((mouse_x - ball_x) ** 2 + (mouse_y - ball_y) ** 2)
    score_choice = 0
    if leng <= ball_r:
        if ball_r <= 50:
            score_choice = 30
        else:
            score_choice = 10
        print_score(score_choice, center=(ball_x, ball_y - ball_r), ball=True, font_size=40)
    score += score_choice


def print_score(num_score, center=(1100, 50), ball=False, font_size=30):
    """Отображение количества очков"""
    string = f'Очки: {num_score}'
    if ball:
        string = f'+{num_score}'
    font = pygame.font.Font(None, font_size)
    text = font.render(string, True, (255, 255, 255))
    place = text.get_rect(center=center)
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
