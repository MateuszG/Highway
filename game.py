""" Highway on Python3 """

from random import randint

import pygame
from class_car import Car
from colors import BLACK, WHITE
from dele import close_game
from draw_models import coursor
from game_events import check_events
from game_logic import game_logic
from init import start_engine

font, clock, screen, SCREEN_WIDTH, SCREEN_HEIGHT, DONE = start_engine(pygame)

# Define math
PI = 3.141592653
FRAMES_PER_SECOND = 30
# Define game
SCORE = 0

# Hide the mouse cursor
pygame.mouse.set_visible(0)

# Postion for keyboard curosr, Speed in Pixels per frame
x_speed = 0
y_speed = 0

# Current position
x_coord = SCREEN_WIDTH / 2
y_coord = SCREEN_HEIGHT / 2

# Get and set position of road
image_road = pygame.image.load("data/road.jpg").convert()
image_road_position = [0, 0]

# Get and set position of road
image_car = pygame.image.load("data/car.png").convert()
start_top_x = -200
start_top_y = 50
image_car_start_position = [start_top_x, start_top_y]

cars_list = []
cars_to_del_list = []
for count in range(2):
    new_car = Car()
    new_car.create_car()
    new_car.id = count
    new_car.x = count * 800 - new_car.WIDTH   # 300
    random_speed = randint(new_car.speed_min, new_car.speed_max)
    new_car.speed = random_speed / 3.6
    cars_list.append(new_car)

# To test
cars_list[0].speed = 60 / 3.6
cars_list[1].speed = 30 / 3.6
select_car = 0
SECUND = 0
FRAMES = -1
MIN_SPACE = 500
table_height = 0

# -------------------------------- Main Loop -------------------------------- #
while DONE is False:
    # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
    for event in pygame.event.get():  # User did something
        x_speed, y_speed, DONE = check_events(event, x_speed, y_speed, DONE)
    # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT

    # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
    pygame, x, y, x_coord, y_coord =\
        game_logic(pygame, x_coord, y_coord, x_speed, y_speed)

    # Count secound base from frames
    FRAMES = FRAMES + 1
    if FRAMES % FRAMES_PER_SECOND == 0:
        print ("############ Second ", SECUND, "############")
        SECUND = SECUND + 1
    # ms secounds

    MS_SECUND = (FRAMES % 30) * 0.03333

    for car in cars_list:
        # At end of road move car to list of cars to delete
        if car.x >= 1566:
            cars_list.remove(car)
            cars_to_del_list.append(car)
        else:
            # Count position and speed of cars
            if car.slow_down_to is None:
                pass
            else:
                # Phisics - Traffic Delayed
                # http://pl.wikipedia.org/wiki/Ruch_op%C3%B3%C5%BAniony
                if car.speed > car.slow_down_to:
                    # Slow down car until have correct speed of ahead car
                    # car.speed = car.speed - 1
                    car.speed = car.speed - (2.5 / 30)  # 2 m/s^2

            car.x = car.x + car.speed
            print ("Car ", car.id, "|Speed ", int(car.speed), "| X ",
                   int(car.x))

    # Add other cars to compared cars list
    for car in cars_list:
        for second_car in cars_list:

            # Get unique compared cars
            if car.id != second_car.id:

                if (
                    second_car.id not in car.id_counted_cars
                    and car.id not in second_car.id_counted_cars
                ):
                    car.id_counted_cars.append(second_car.id)
                    second_car.id_counted_cars.append(car.id)

                    # Car slow to speed of ahead car
                    if (car.x + car.WIDTH + MIN_SPACE >= second_car.x):
                        print ("STOP Car", car.id, "|Speed ", int(car.speed),
                               "| X ", int(car.x), "to speed",
                               int(second_car.speed))
                        print ("############ Second " + str(SECUND)
                               + str(MS_SECUND)[1:] + " ############")
                        car.slow_down_to = second_car.speed

    # Clear list with compared cars
    for car in cars_list:
        car.id_counted_cars = []

    # Delete car in list which is out of screen
    for car_to_del in cars_to_del_list:
        cars_to_del_list.remove(car_to_del)
        del car_to_del
    # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT

    # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT

    # Clear the screen and set the screen background
    screen.fill(WHITE)

    # Draw road
    screen.blit(image_road, image_road_position)

    # Draw car
    for car in cars_list:
        car.draw_car(screen, [car.x, start_top_y])

    # Render the text. "True" means anti-aliased text.
    # BLACK is the color. The variable BLACK was defined
    # above as a list of [0,0,0]
    # Note: This line creates an image of the letters,
    # but does not put it on the screen yet.
    TEXT = font.render("Highway simulation", True, BLACK)
    SCORE += 100
    SCORE_TEXT = font.render("Score: " + str(SCORE), True, BLACK)

    # Put the image of the text on the screen at 250x250
    screen.blit(
        TEXT, [int(SCREEN_WIDTH / 2), SCREEN_HEIGHT - SCREEN_HEIGHT + 500])
    screen.blit(SCORE_TEXT, [SCREEN_WIDTH - 200, SCREEN_HEIGHT - 50])

    for car in cars_list:
        Car_details = font.render(
            "Car" + str(car.id) + " Speed (m/s): " + str(car.speed), True,
            BLACK
        )
        table_height = table_height + 20
        # Put the image of the text on the screen at 250x250
        screen.blit(
            Car_details,
            [
                int(SCREEN_WIDTH / 2),
                SCREEN_HEIGHT - SCREEN_HEIGHT + 400 + table_height
            ]
        )
    table_height = 0

    # Add cursor
    coursor(screen, x, y)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

    # Limit to 25 frames per second
    clock.tick(FRAMES_PER_SECOND)
# -------------------------------- Main Loop -------------------------------- #

close_game(pygame)
