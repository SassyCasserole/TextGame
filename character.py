from positionable import Positionable
from text import HelpText


class Character(Positionable):

    def command_move(self, command):
        self.move(command.offset_x, command.offset_y)


class Space(Character):

    def __init__(self, x, y):
        self.image = SPACE_CHAR
        super(Space, self).__init__(x, y)


class Wall(Character):

    def __init__(self, x, y):
        self.image = WALL_CHAR
        super(Wall, self).__init__(x, y)

    def interact(self, character):
        return HelpText.WALL_TEXT.value


class MainCharacter(Character):

    def __init__(self, x, y):
        self.image = MC_CHAR
        super(MainCharacter, self).__init__(x, y)


class ComputerCharacter(Character):

    COLLISION_LIST = []

    def __init__(self, x, y):
        self.image = COMPUTER_CHAR
        super(ComputerCharacter, self).__init__(x, y)

    def interact(self, character):
        return HelpText.LOVE_TEXT.value


class BabeCharacter(Character):

    def __init__(self, x, y):
        self.image = BABE_CHAR
        super(BabeCharacter, self).__init__(x, y)

    def interact(self, character):
        return HelpText.BABE_TEXT.value


class Fake(Character):

    COLLISION_LIST = []

    def __init__(self, x, y):
        self.image = SPACE_CHAR
        super(Fake, self).__init__(x, y)

# collisions

Wall.COLLISION_LIST = [MainCharacter]
MainCharacter.COLLISION_LIST = [BabeCharacter, Wall]
BabeCharacter.COLLISION_LIST = [MainCharacter]

# string character definitions
SPACE_CHAR = ' '
WALL_CHAR = 'X'
MC_CHAR = '@'
COMPUTER_CHAR = '='
BABE_CHAR = '&'

# mapping
CHAR_TO_CHARACTER_MAPPING = {SPACE_CHAR: Space,
                             WALL_CHAR: Wall,
                             MC_CHAR: MainCharacter,
                             COMPUTER_CHAR: ComputerCharacter,
                             BABE_CHAR: BabeCharacter}
