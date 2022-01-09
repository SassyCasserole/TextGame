from user import User
from screen import Screen
from command import MovementCommand, UseCommand


class State:

    def __init__(self):
        self.user = User()
        self.screen = Screen()
        self.mc = None
        self.command_history = []

    def take_command(self, command):
        self.command_history.append(command)
        self.screen.reset()
        if isinstance(command, MovementCommand):
            self.screen.attempt_move(self.mc, command)
            self.screen.set_center(self.mc.x, self.mc.y)
        elif isinstance(command, UseCommand):
            self.screen.use_action(self.mc)
        else:
            pass

    def add_map(self, lines):
        self.mc = self.screen.add_map(lines)
        self.screen.set_center(self.mc.x, self.mc.y)
