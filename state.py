from user import User
from overworld import Overworld
from command import MovementCommand, UseCommand


class State:

    def __init__(self):
        self.command_history = []
        self.overworld = Overworld()
        self.user = User()

    def take_command(self, command):
        self.command_history.append(command)
        self.overworld.current_screen.reset()
        self.overworld.current_screen.update()

        if isinstance(command, MovementCommand):
            self.overworld.current_screen.attempt_move(self.overworld.mc, command)
            self.overworld.current_screen.set_center(self.overworld.mc.x, self.overworld.mc.y)
        elif isinstance(command, UseCommand):
            self.overworld.current_screen.use_action(self.overworld.mc)
        else:
            pass

    def update(self):
        self.overworld.current_screen.draw()
        self.user.get_input()
        input_command = self.user.input_command
        input_command.executive_action()

        if input_command:
            self.take_command(input_command)
        else:
            pass

