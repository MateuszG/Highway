""" Function which control game """
import pygame


def check_events(event, x_speed, y_speed, DONE):
    if (event.type == pygame.QUIT) or ((event.type == pygame.KEYDOWN)
       and (event.key == pygame.K_ESCAPE)):  # If user clicked close
        DONE = True  # Flag that we are done so we exit this loop
    if event.type == pygame.KEYDOWN:
        print("User pressed a key.")
    if event.type == pygame.KEYUP:
        print("User let go of a key.")
    if event.type == pygame.MOUSEBUTTONDOWN:
        print("User pressed a mouse button")
    if ((event.type == pygame.KEYDOWN)
       and (event.key == pygame.K_RETURN)):  # If user clicked close
        print("Game started")

    # User pressed down on a key
    if event.type == pygame.KEYDOWN:
        # Figure out if it was an arrow key. If so
        # adjust speed.
        if event.key == pygame.K_LEFT:
            x_speed = -10
        if event.key == pygame.K_RIGHT:
            x_speed = 10
        if event.key == pygame.K_UP:
            y_speed = -10
        if event.key == pygame.K_DOWN:
            y_speed = 10

    # User let up on a key
    if event.type == pygame.KEYUP:
        # If it is an arrow key, reset vector back to zero
        if event.key == pygame.K_LEFT:
            x_speed = 0
        if event.key == pygame.K_RIGHT:
            x_speed = 0
        if event.key == pygame.K_UP:
            y_speed = 0
        if event.key == pygame.K_DOWN:
            y_speed = 0
    return (x_speed, y_speed, DONE)
