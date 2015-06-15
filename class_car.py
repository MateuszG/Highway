import pygame


class Car(object):
    id = 0
    WIDTH = 228
    HEIGHT = 128
    speed_max = 60
    speed_min = 30
    slow_down_to = None
    speed_up_to = None
    weight_kg = 1000
    x = -200
    speed = 0
    postion_top = [x-200, 50]
    postion_bottom = [-200, 200]

    id_counted_cars = []
    image_car = pygame.image.load("data/car.png").convert()

    def create_car(self):
        """ Image size width = 228, height = 128 """
        return self.image_car

    def draw_car(self, screen, image_car_position):
        # if image_car_position[0] >= 1366:
        #     image_car_position[0] = image_car_position[0] % 1366 - 200
        return screen.blit(self.image_car, image_car_position)
