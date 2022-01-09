from pynput.keyboard import Listener
from command import UpCommand, LeftCommand, DownCommand, RightCommand, EmptyCommand, QuitCommand, UseCommand


class User:

    def __init__(self):
        self.input_command = None

    def on_press(self, key):
        try:
            char = key.char
        except AttributeError:
            self.input_command = EmptyCommand()
        else:
            if char == 'c':
                self.input_command = QuitCommand()
            elif char == 'q':
                self.input_command = QuitCommand()
            elif char == 'w':
                self.input_command = UpCommand()
            elif char == 'a':
                self.input_command = LeftCommand()
            elif char == 's':
                self.input_command = DownCommand()
            elif char == 'd':
                self.input_command = RightCommand()
            elif char == 'e':
                self.input_command = UseCommand()
            else:
                self.input_command = EmptyCommand()

        return False

    def get_input(self):
        with Listener(on_press=self.on_press, on_release=None) as listener:
            listener.join()
