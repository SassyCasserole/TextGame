from coordinate import Coordinate
from text import InfoText
from movement import Movement, RandomMovement, PaceMovement


class Positionable:

    COLLISION_LIST = []

    def __init__(self, entry):
        self._coordinate = Coordinate(None, None)
        self._coordinate_history = [self._coordinate]
        self._attempted_coordinate_history = [self._coordinate]
        self.name = entry['name']
        self.image = entry['image']
        self._type = entry['type']
        self._type_info = entry['type_info']
        if self._type_info['collision_types'][0] == 'all':
            self._short_circuit_all_collides = True
        else:
            self._short_circuit_all_collides = False

        if self._type_info['collision_types'][0] == 'none':
            self._short_circuit_none_collides = True
        else:
            self._short_circuit_none_collides = False

        self._movement = self.get_movement(entry)
        self._help_text = InfoText(entry['text'], entry['text_priority'])

    @staticmethod
    def get_movement(entry):
        try:
            movement_dict = entry['movement']
        except KeyError:
            movement = Movement()
        else:
            if movement_dict['type'] == 'random':
                movement = RandomMovement(movement_dict)
            elif movement_dict['type'] == 'pace':
                movement = PaceMovement(movement_dict)
            else:
                movement = None
        return movement

    def talk(self, command):
        return self._help_text

    @property
    def collisions(self):

        return

    def _i_collide(self, their_type):
        if self._short_circuit_none_collides:
            return False
        elif self._short_circuit_all_collides:
            return True
        else:
            return their_type in self._type_info['collision_types']

    @property
    def type(self):
        return self._type

    def collides(self, positionable):
        return self._i_collide(positionable.type)

    def undo_move(self):
        self._coordinate_history.pop()
        new_x = self.last_x
        new_y = self.last_y
        self._coordinate = Coordinate(new_x, new_y)
        self._coordinate_history.append(self._coordinate)
        self._attempted_coordinate_history.append(self._coordinate)

    def commanded_move(self, command):
        pass

    def move_self(self):
        self.accept_movement()

    def accept_movement(self):
        x, y = self._movement.get_next(self.x, self.y)
        self.x = x
        self.y = y

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
        return "I am {} look like {} at {}".format(type(self).__name__, self.image, self._coordinate)
