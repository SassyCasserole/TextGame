from coordinate import Coordinate
from errors import GameError
from text import HelpText


class Positionable:

    COLLISION_LIST = []

    def __init__(self, x, y):
        self._coordinate = Coordinate(x, y)
        self._coordinate_history = [self._coordinate]
        self._attempted_coordinate_history = [self._coordinate]

    def collides(self, positionable):
        if type(self) in positionable.COLLISION_LIST:
            he_thinks_i_collide = True
        else:
            he_thinks_i_collide = False

        if type(positionable) in self.COLLISION_LIST:
            i_think_he_collides = True
        else:
            i_think_he_collides = False

        if i_think_he_collides != he_thinks_i_collide:
            raise GameError("Improper Collision Settings.")

        return i_think_he_collides

    def undo_move(self):
        self._coordinate_history.pop()
        new_x = self.last_x
        new_y = self.last_y
        self._coordinate = Coordinate(new_x, new_y)
        self._coordinate_history.append(self._coordinate)
        self._attempted_coordinate_history.append(self._coordinate)

    @property
    def x(self):
        return self._coordinate.x

    @property
    def last_x(self):
        return self._coordinate_history[-1].x

    @property
    def y(self):
        return self._coordinate.y

    @property
    def last_y(self):
        return self._coordinate_history[-1].y

    def move(self, offset_x, offset_y):
        new_x = self._coordinate.x + offset_x
        new_y = self._coordinate.y - offset_y
        self._coordinate = Coordinate(new_x, new_y)
        self._coordinate_history.append(self._coordinate)
        self._attempted_coordinate_history.append(self._coordinate)

    def __repr__(self):
        return "I am {} at {}".format(type(self).__name__, self._coordinate)

    def interact(self, character):
        return HelpText.NULL_TEXT.value
