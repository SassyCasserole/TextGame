from enum import Enum


class InfoText:

    def __init__(self, text, priority):
        self.text = text
        self.priority = priority

    def __repr__(self):
        return "Info Text {} at priority {}".format(self.text, self.priority)


CONTROLS_TEXT_PRIORITY = 95
LOWEST_PRIORITY = 100


class HelpText(Enum):

    CONTROLS_TEXT = InfoText('Press Q or C to exit. Use WASD to move. Press E to use.', CONTROLS_TEXT_PRIORITY)
