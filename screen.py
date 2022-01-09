from character import CHARACTERS, MainCharacter
from positionable import Coordinate
from errors import CollisionError, GameError
from priority_display_queue import PriorityDisplayQueue
from text import HelpText, LOWEST_PRIORITY


class Cell(Coordinate):

    def __init__(self, x, y):
        self.stack = []
        super().__init__(x, y)

    def add_positionable(self, character):
        self.stack.append(character)

    def remove_positionable(self, character):
        self.stack.remove(character)

    def remove_top(self):
        return self.stack.pop()

    def remove_all(self):
        self.stack = []

    def get_image(self):
        try:
            im = self.stack[-1].image
        except IndexError:
            # hack
            im = '.'
        return im


class ScreenList(list):

    pass


class Row(ScreenList):
    def apply(self, method, positionable=None):
        if positionable:
            return self.__getitem__(positionable.x).__getattribute__(method)(positionable)
        else:
            return self.__getitem__(positionable.x).__getattribute__(method)()

    def get_image(self, minimum, maximum):
        image = ''.join([i.get_image() for i in self[minimum:maximum]])
        image += '\n'
        return image


class Column(ScreenList):
    def apply(self, method, positionable=None):
        return self.__getitem__(positionable.y).apply(method.__name__, positionable)

    def get_image(self, min_x, max_x, min_y, max_y):
        my_subset = self[min_y:max_y]
        return ''.join([i.get_image(min_x, max_x) for i in my_subset])


class Screen:

    def __init__(self):
        self.grid = Column([])
        self._display_queue = PriorityDisplayQueue(HelpText.CONTROLS_TEXT.value)
        self.center_x = NotImplemented
        self.center_y = NotImplemented
        self.map_height = NotImplemented
        self.map_width = NotImplemented

    def will_collide(self, positionable):
        collides = False
        for existing_positionable in self.grid[positionable.y][positionable.x].stack:
            if positionable.collides(existing_positionable):
                collides = True
                break
        return collides

    def attempt_move(self, positionable, command):
        try:
            self.move(positionable, command)
        except CollisionError:
            pass

    def move(self, positionable, command):
        self.grid.apply(Cell.remove_positionable, positionable)
        positionable.command_move(command)

        if self.will_collide(positionable):
            positionable.undo_move()
            self.grid.apply(Cell.add_positionable, positionable)
            raise CollisionError(positionable)

        self.grid.apply(Cell.add_positionable, positionable)

    def get_subset_image(self, width, height):
        half_width = round(width/2)
        min_x = self.center_x - half_width
        max_x = self.center_x + half_width

        half_height = round(height / 2)
        min_y = self.center_y - half_height
        max_y = self.center_y + half_height
        if min_x < 0:
            min_x = 0
        if min_y < 0:
            min_y = 0
        if max_x > self.map_width:
            max_x = 0
        if max_y > self.map_height:
            max_y = 0
        return self.grid.get_image(min_x, max_x, min_y, max_y)

    def get_current_image(self):
        return self.get_subset_image(50, 20)

    def set_center(self, x, y):
        self.center_x = x
        self.center_y = y

    def draw(self):
        print(self.get_current_image())
        print(self._display_queue.highest().text)

    def add_map(self, lines):
        val = None
        # make a grid big enough
        # assumed to be rectangular
        self.map_height = len(lines)
        self.map_width = len(lines[0])
        for i in range(0, self.map_height):
            row = Row([Cell(i, j) for j in range(0, self.map_width)])
            self.grid.append(row)

        # instantiate objects within cells
        # based on the given map
        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                if char == '\n':
                    pass
                else:
                    character = CHARACTERS.get_character_from_char(char)
                    character.x = x
                    character.y = y

                    self.grid.apply(Cell.add_positionable, character)
                    print(character)
                    if isinstance(character, MainCharacter):
                        val = character
        if not val:
            raise GameError("No Main Character")
        return val

    def get_nearby(self, x, y):
        nearby_stack = []
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                nearby_stack.extend(self.grid[j][i].stack)
        return nearby_stack

    def use_action(self, character):
        current_priority = LOWEST_PRIORITY
        top_interaction = None

        nearby_chars = self.get_nearby(character.x, character.y)

        for other_character in nearby_chars:
            interaction = other_character.interact(character)
            if interaction.priority <= current_priority:
                current_priority = interaction.priority
                top_interaction = interaction

        self._display_queue.add(top_interaction)

    def reset(self):
        self._display_queue.reset()
        self._display_queue.add(HelpText.CONTROLS_TEXT.value)
