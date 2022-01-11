class Command:

    def __init__(self):
        pass

    def executive_action(self):
        pass


class ActionCommand(Command):

    def __init__(self):
        super(ActionCommand, self).__init__()


class UseCommand(ActionCommand):

    def __init__(self):
        super(Command, self).__init__()


class MovementCommand(Command):

    def __init__(self):
        super(MovementCommand, self).__init__()


class NullMovementCommand(Command):

    def __init__(self):
        super(NullMovementCommand, self).__init__()
        self.offset_x = 0
        self.offset_y = 0


class UpCommand(MovementCommand):

    def __init__(self):
        super(UpCommand, self).__init__()
        self.offset_x = 0
        self.offset_y = 1


class LeftCommand(MovementCommand):

    def __init__(self):
        super(LeftCommand, self).__init__()
        self.offset_x = -1
        self.offset_y = 0


class DownCommand(MovementCommand):

    def __init__(self):
        super(DownCommand, self).__init__()
        self.offset_x = 0
        self.offset_y = -1


class RightCommand(MovementCommand):

    def __init__(self):
        super(RightCommand, self).__init__()
        self.offset_x = 1
        self.offset_y = 0


class EmptyCommand(Command):

    def __init__(self):
        super(EmptyCommand, self).__init__()


class QuitCommand(Command):

    def __init__(self):
        super(QuitCommand, self).__init__()

    def executive_action(self):
        print("Bye!")
        super(QuitCommand, self).executive_action()
        quit(0)