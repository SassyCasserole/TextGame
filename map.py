def get_map(name):
    with open(name, 'r') as f:
        lines = f.readlines()

    newlines = []
    for line in lines:
        line.rstrip('\n')
        newlines.append(line)
    return newlines