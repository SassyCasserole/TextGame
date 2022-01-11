from random import randint

MAX_SPEED = 100

class Movement:

    def get_next(self, x, y):
        # doesn't move
        return x, y


class RandomMovement(Movement):

    def __init__(self, movement_parameters):
        self.speed = movement_parameters['speed']
        self.limit_x = movement_parameters['limits']['x']
        self.limit_y = movement_parameters['limits']['y']

    def get_next(self, x, y):

        change_x = randint(0, MAX_SPEED)
        change_y = randint(0, MAX_SPEED)
        if change_x <= self.speed:
            offset_x = 1
        else:
            offset_x = 0
        if change_y <= self.speed:
            offset_y = 1
        else:
            offset_y = 0

        if bool(randint(0, 1)):
            offset_x = -offset_x

        if bool(randint(0, 1)):
            offset_y = -offset_y

        return x + offset_x, y + offset_y
