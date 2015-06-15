""" Models definition """
import pygame
from colors import BLACK, BLUE, GREEN, RED, WHITE


def draw_street(screen, x, y):
    pygame.draw.ellipse(screen, BLACK, [35 + x, 0 + y, 25, 25])
    pygame.draw.ellipse(screen, BLACK, [23 + x, 20 + y, 50, 50])
    pygame.draw.ellipse(screen, BLACK, [0 + x, 65 + y, 100, 100])


def coursor(screen, x, y):
    # Head
    pygame.draw.ellipse(screen, BLACK, [1 + x, y, 10, 10], 0)


def draw_car_model(screen, x, y):
    # Whells - Back
    pygame.draw.ellipse(screen, BLACK, [x, y, 10, 10], 0)
    pygame.draw.ellipse(screen, BLACK, [x, y + 25, 10, 10], 0)

    # Whells - Front
    pygame.draw.ellipse(screen, BLACK, [50 + x, y, 10, 10], 0)
    pygame.draw.ellipse(screen, BLACK, [50 + x, y + 25, 10, 10], 0)
