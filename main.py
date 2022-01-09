from state import State
from map import get_map


def do_one(state):
    state.screen.draw()
    state.user.get_input()
    input_command = state.user.input_command
    input_command.executive_action()

    if input_command:
        state.take_command(input_command)
    else:
        pass


def main_loop():
    state = State()
    state.add_map(get_map('map.txt'))
    try:
        while True:
            do_one(state)
    except KeyboardInterrupt:
        exit(0)


if __name__ == '__main__':
    main_loop()
