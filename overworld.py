import os
from screen import Screen


class Overworld:

    def __init__(self):
        self.mc = None
        self._maps_dir = 'maps'
        self._initial_map_name = 'initial.txt'
        self.screens = []
        self.current_screen = Screen()
        self.add_initial_map()
        self.add_expansion_maps()

    def add_initial_map(self):
        initial_map = self.get_initial_map()
        mc = self.current_screen.add_map(initial_map)
        assert mc, mc
        self.mc = mc
        self.current_screen.set_center(mc.x, mc.y)
        self.screens.append(self.current_screen)

    def add_expansion_maps(self):
        for expansion_map in self.get_expansion_maps():
            screen = Screen()
            mc = screen.add_map(expansion_map)
            assert not mc, mc
            self.screens.append(screen)


    def get_expansion_maps(self):
        maps = []
        for file in os.listdir(self._maps_dir):
            if file.endswith('.txt'):
                if file != self._initial_map_name:
                    new_map = self.get_map(file)
                    maps.append(new_map)
        return maps

    def get_initial_map(self):
        return self.get_map(self._initial_map_name)

    def get_map(self, name):
        with open(os.path.join(self._maps_dir, name), 'r') as f:
            lines = f.readlines()

        newlines = []
        for line in lines:
            line.rstrip('\n')
            newlines.append(line)
        return newlines
