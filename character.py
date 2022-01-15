import yaml
from positionable import Positionable
from errors import GameError


class Character(Positionable):

    def commanded_move(self, command):
        self.move(command.offset_x, command.offset_y)


class MainCharacter(Character):

    pass

class Characters:

    def __init__(self):
        self.MainCharacter = None
        self._characters_by_image = {}
        self._load_characters('characters.yaml', 'types.yaml')

    def get_character_from_char(self, char):
        assert len(char) == 1, char
        return self._characters_by_image[char]

    def _load_characters(self, char_filename, types_filename):
        with open(char_filename, 'r') as f:
            chars = yaml.safe_load(f)

        with open(types_filename, 'r') as f:
            types = yaml.safe_load(f)

        this_char_type_info = None
        for yaml_name, entry in chars.items():
            for type_name, type_info in types.items():
                if type_name == entry['type']:
                    this_char_type_info = type_info
            if not this_char_type_info:
                raise GameError("{} has no type (from {})".format(yaml_name, types))

            entry['type_info'] = this_char_type_info

            if yaml_name == 'main_character':
                self._characters_by_image[entry['image']] = MainCharacter(entry)
            else:
                self._characters_by_image[entry['image']] = Character(entry)


CHARACTERS = Characters()
