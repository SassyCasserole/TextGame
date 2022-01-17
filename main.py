from state import State


def main_loop():
    state = State()
    try:
        while True:
            state.update()
    except KeyboardInterrupt:
        exit(0)


if __name__ == '__main__':
    main_loop()
