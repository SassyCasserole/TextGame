from random import randint
from enum import Enum

MAX_SPEED = 100


def _get_unidirectional_offset(speed):
    absolute_offset = randint(0, MAX_SPEED)
    if absolute_offset <= speed:
        offset = 1
    else:
        offset = 0
    return offset


class Movement:

    def get_next(self, x, y):
        # doesn't move
        return x, y

    def _get_bidirectional_offset(self, speed):
        if bool(randint(0, 1)):
            offset = -_get_unidirectional_offset(speed)
        else:
            offset = _get_unidirectional_offset(speed)
        return offset


class RandomMovement(Movement):

    def __init__(self, movement_parameters):
        self.speed = movement_parameters['speed']
        self.limit_x = movement_parameters['limits']['x']
        self.limit_y = movement_parameters['limits']['y']

    def get_next(self, x, y):
        offset_x = self._get_bidirectional_offset(self.speed)
        offset_y = self._get_bidirectional_offset(self.speed)
        return x + offset_x, y + offset_y


class PaceMovement(Movement):

    def __init__(self, movement_parameters):
        self.speed = movement_parameters['speed']
        if movement_parameters['direction'] == 'up':
            self.horizontal_direction = False
        else:
            self.horizontal_direction = True
        self.limit = movement_parameters['limit']
        self._initial_x = None
        self._initial_y = None
        self._max = None
        self._path = Path(None, None, self.speed)

    def get_next(self, x, y):
        if not self._initial_x:
            self._initial_x = x
            self._initial_y = y
            if self.horizontal_direction:
                self._path.minimum = self._initial_x - self.limit
                self._path.maximum = self._initial_x + self.limit
            else:
                self._path.minimum = self._initial_y - self.limit
                self._path.maximum = self._initial_y + self.limit
        if self.horizontal_direction:
            new_x = self._path.get_next(x)
            new_y = y
        else:
            new_x = x
            new_y = self._path.get_next(y)

        return new_x, new_y


class PathDirection(Enum):

    FORWARD = 1
    BACKWARD = 2


class Path:

    def __init__(self, minimum, maximum, speed):
        self.minimum = minimum
        self.maximum = maximum
        self.speed = speed
        self._direction = PathDirection.FORWARD
        self._recent = []
        self._max_len_recent = 5

    def _get_next(self, pos):
        if self._direction == PathDirection.FORWARD:
            pos += _get_unidirectional_offset(self.speed)
        else:
            pos -= _get_unidirectional_offset(self.speed)
        return pos

    def _toggle_direction(self):
        if self._direction == PathDirection.FORWARD:
            self._direction = PathDirection.BACKWARD
        else:
            self._direction = PathDirection.FORWARD

    def _is_stuck(self, pos):
        self._recent.append(pos)
        if len(self._recent) >= self._max_len_recent:
            # shift
            self._recent = self._recent[1:-1]

            self._recent.append(pos)
        print(self._direction)
        print(self._recent)

        for recent_pos in self._recent:
            if recent_pos == pos:
                return True
            else:
                return False

    def get_next(self, pos):
        new_pos = self._get_next(pos)
        if new_pos >= self.maximum or new_pos <= self.minimum or self._is_stuck(new_pos):
            self._toggle_direction()
            new_pos = self._get_next(pos)

        return new_pos
