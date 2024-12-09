grid = [list(line) for line in open(0).read().splitlines()]

by_type = {}
for y in range(len(grid)):
    for x in range(len(grid[0])):
        cell = grid[y][x]
        if cell not in ".#":
            by_type[cell] = by_type.get(cell) or []
            by_type[cell].append((y, x))


def is_in_grid(point: tuple[int, int]):
    return 0 <= point[0] < len(grid) and 0 <= point[1] < len(grid[0])


antinodes = set()
for antenna in by_type:
    coords = by_type[antenna]
    for i in range(len(coords)):
        for j in range(len(coords)):
            if i == j: continue
            y1, x1 = coords[i]
            y2, x2 = coords[j]
            antinodes.add((y1, x1))
            antinodes.add((y2, x2))
            dx = x2 - x1
            dy = y2 - y1
            k = 1
            while True:
                first = y2 + k * dy, x2 + k * dx
                secon = y1 - k * dy, x1 - k * dx

                first_in = is_in_grid(first)
                second_in = is_in_grid(secon)
                if not (first_in or second_in):
                    break
                elif first_in:
                    antinodes.add(first)
                elif second_in:
                    antinodes.add(secon)
                k += 1
print(len(antinodes))
#
# for y in range(len(grid)):
#     for x in range(len(grid[0])):
#         cell = grid[y][x]
#         if cell == "#" and (y,x) not in antinodes:
#             cell = "!"
#         print(cell, end="")
#     print()
# print((sum([len(by_type[k]) for k in by_type])))