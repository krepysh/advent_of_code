from advent import read_input


universe = read_input('day11.txt')


def expand_universe(u):
    empty_cols = []
    empty_rows = []
    single_empty_row = ['.'] * len(u[0])
    u = [list(row) for row in u]
    for i in range(len(u[0])):
        if all([row[i] == '.' for row in u]):
            empty_cols.append(i)
    for i, row in enumerate(u):
        if row == single_empty_row:
            empty_rows.append(i)
    for i in empty_cols:
        for row in u:
            row.insert(i, '.')
    for i in empty_rows:
        u.insert(i, ['.'] * len(u[0]))
    return u


universe = expand_universe(universe)
for row in universe:
    print(''.join(row))
galaxies: list[tuple[int, int]] = []

for y_num in range(len(universe)):
    for x_num in range(len(universe[0])):
        if universe[y_num][x_num] == '#':
            galaxies.append((y_num, x_num))


dist_sum = 0


def get_shortest_distance(universe: list[list[str]], param: tuple[int, int], param1: tuple[int, int]):
    """Dijkstra algorythm we don't need here."""
    return abs(param[0] - param1[0]) + abs(param[1] - param1[1])


for first_gal in range(len(galaxies)):
    for second_gal in range(first_gal + 1, len(galaxies)):
        dist_sum += get_shortest_distance(universe, galaxies[first_gal], galaxies[second_gal])

print(dist_sum)
