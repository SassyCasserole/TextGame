import yaml
from positionable import Positionable


class Character(Positionable):

    def command_move(self, command):
        self.move(command.offset_x, command.offset_y)


class MainCharacter(Character):

    pass


class Characters:

    def __init__(self):
        self.MainCharacter = None
        self._characters_by_image = {}
        self._load_characters('characters.yaml')

    def get_character_from_char(self, char):
        assert len(char) == 1, char
        return self._characters_by_image[char]

    def _load_characters(self, filename):
        with open(filename, 'r') as f:
            chars = yaml.safe_load(f)

        for yaml_name, entry in chars.items():
            if yaml_name == 'main_character':
                self._characters_by_image[entry['image']] = MainCharacter(entry)
            else:
                self._characters_by_image[entry['image']] = Character(entry)


CHARACTERS = Characters()
