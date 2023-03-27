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
star_coords = [randint(0, 900), randint(100, 800)]
diff_star_x = 5
diff_star_y = -5


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
        print_score(score_choice, center=(ball_x, ball_y-ball_r), ball=True, font_size=40)
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


def star(star_x, star_y):
    polygon(screen, 'yellow', ((star_x + 10, star_y), (star_x + 20, star_y - 30), (star_x, star_y - 50),
                               (star_x + 30, star_y - 50), (star_x + 40, star_y - 95), (star_x + 50, star_y - 50),
                               (star_x + 80, star_y - 50), (star_x + 60, star_y - 30), (star_x + 70, star_y),
                               (star_x + 40, star_y - 20)))


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

    if 1120 <= star_coords[0] or star_coords[0] <= 0:
        diff_star_x = 0 - diff_star_x
    if 900 <= star_coords[1] or star_coords[1] <= 95:
        diff_star_y = 0 - diff_star_y
    star_coords[0] += diff_star_x
    star_coords[1] += diff_star_y
    star(star_coords[0], star_coords[1])

    new_ball()
    print_score(str(score))
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
