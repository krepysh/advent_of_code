from advent import read_input

lines = read_input('day14.txt')

filled = set()

coordinates = []
for line in lines:
    current = []
    # line looks like: 498,4 -> 498,6 -> 496,6
    coord_pairs = line.split(' -> ')
    for pair in coord_pairs:
        rock_x, rock_y = pair.split(',')
        current.append((int(rock_x), int(rock_y)))
    coordinates.append(current)


def my_range(start: int, stop: int):
    start, stop = (stop, start + 1) if stop < start else (start, stop + 1)
    return range(start, stop)


for rock_formation in coordinates:
    for i in range(1, len(rock_formation)):
        start_x, start_y = rock_formation[i - 1]
        end_x, end_y = rock_formation[i]

        for x in my_range(start_x, end_x):
            for y in my_range(start_y, end_y)   :
                filled.add((x, y))

# y coord of the lowest rock, everything underneath of it is the abyss
start_of_tar_tar_tarary = max([c[1] for c in filled])
floor = start_of_tar_tar_tarary + 2


def is_empty(x, y):
    if y == floor:
        return False
    if (x, y) in filled:
        return False
    return True


def simulation_round(field: set[tuple[int, int]]):
    x, y = 500, 0
    while True:
        if not is_empty(x, y):
            return False
        y = y + 1
        if is_empty(x, y):
            pass
        elif is_empty(x - 1, y):
            x = x - 1
        elif is_empty(x + 1, y):
            x = x + 1
        else:
            field.add((x, y - 1))
            return True


i = 0
while simulation_round(filled):
    i += 1

print(i)
