from enum import Enum


class InfoText:

    def __init__(self, text, priority):
        self.text = text
        self.priority = priority

    def __repr__(self):
        return "Info Text {} at priority {}".format(self.text, self.priority)


CONTROLS_TEXT_PRIORITY = 95
LOVE_TEXT_PRIORITY = 50
WALL_TEXT_PRIORITY = 90
LOWEST_PRIORITY = 100
BABE_TEXT_PRIORITY = 50


class HelpText(Enum):

    CONTROLS_TEXT = InfoText('Press Q or C to exit. Use WASD to move. Press E to use.', CONTROLS_TEXT_PRIORITY)
    LOVE_TEXT = InfoText('I Love You, Erin!', LOVE_TEXT_PRIORITY)
    WALL_TEXT = InfoText('Ouch, thats a wall!', WALL_TEXT_PRIORITY)
    NULL_TEXT = InfoText('', LOWEST_PRIORITY)
    BABE_TEXT = InfoText('Hi! My name is Cassandra, what is your name?', BABE_TEXT_PRIORITY)

