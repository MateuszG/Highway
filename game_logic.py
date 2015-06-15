""" Game logic for loop """


def game_logic(pygame, x_coord, y_coord, x_speed, y_speed):
    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]

    # Move the object according to the speed vector.
    x_coord = x_coord + x_speed
    y_coord = y_coord + y_speed
    return(pygame, x, y, x_coord, y_coord)
