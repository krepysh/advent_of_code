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


def in_order(start: int, stop: int):
    return (stop, start + 1) if stop < start else (start, stop + 1)


for rock_formation in coordinates:
    for i in range(1, len(rock_formation)):
        start_x, start_y = rock_formation[i - 1]
        end_x, end_y = rock_formation[i]

        for x in range(*in_order(start_x, end_x)):
            for y in range(*in_order(start_y, end_y)):
                filled.add((x, y))

# y coord of the lowest rock, everything underneath of it is the abyss
start_of_tar_tar_tarary = max([c[1] for c in filled])


def simulation_round(field: set[tuple[int, int]]):
    x, y = 500, 0
    while y < start_of_tar_tar_tarary:
        y = y + 1
        if (x, y + 1) not in field:
            pass
        elif (x - 1, y + 1) not in field:
            x = x - 1
        elif (x + 1, y + 1) not in field:
            x = x + 1
        else:
            field.add((x, y))
            return True
    return False


i = 0
while simulation_round(filled):
    i += 1

print(i)
