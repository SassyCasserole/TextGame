from coordinate import Coordinate
from errors import GameError
from text import InfoText

class Positionable:

    COLLISION_LIST = []

    def __init__(self, entry):
        self._coordinate = Coordinate(None, None)
        self._coordinate_history = [self._coordinate]
        self._attempted_coordinate_history = [self._coordinate]
        self.name = entry['name']
        self.image = entry['image']
        self._collision_list = entry['collision']
        self._id = entry['id']
        self._help_text = InfoText(entry['text'], entry['text_priority'])

    def interact(self, command):
        return self._help_text

    @property
    def collisions(self):
        return self._collision_list

    def collides(self, positionable):
        if self._id in positionable.collisions:
            he_thinks_i_collide = True
        else:
            he_thinks_i_collide = False

        if positionable._id in self.collisions:
            i_think_he_collides = True
        else:
            i_think_he_collides = False

        if i_think_he_collides != he_thinks_i_collide:
            raise GameError("Improper Collision Settings for self {} and other {}", self._id, positionable._id)

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

    @x.setter
    def x(self, val):
        self._coordinate.x = val

    @property
    def last_x(self):
        return self._coordinate_history[-1].x

    @property
    def y(self):
        return self._coordinate.y

    @y.setter
    def y(self, val):
        self._coordinate.y = val

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
