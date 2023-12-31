from advent import read_input

lines = read_input('day18.txt')

lava_droplet = [[[False] * 20 for i in range(20)] for _ in range(20)]
visited = set()


def get_coords(s):
    coords = []
    for coord in s:
        x, y, z = coord.split(',')
        coords.append(tuple(map(int, (x, y, z))))
    return coords


def fill_droplet(droplet, coord):
    x, y, z = coord
    droplet[x][y][z] = True


def count_neighbours(in_droplet, coord, air=None):
    n = 0
    x, y, z = coord
    neib_coords = (x - 1, y, z), (x + 1, y, z), (x, y - 1, z), (x, y + 1, z), (x, y, z - 1), (x, y, z + 1)
    for nx, ny, nz in neib_coords:
        try:
            is_bubble = ((nx, ny, nz) not in air) if air else False
            val = in_droplet[nx][ny][nz] or is_bubble
        except IndexError:
            val = 0
        n += val
    return n


lava = get_coords(lines)
for c in lava:
    fill_droplet(lava_droplet, c)
start = (19, 19, 19)
to_visit = [start]
while to_visit:
    # traverse accross cube, and add to variable visited all coords accessible from start
    current = to_visit.pop()
    if current in visited:
        continue
    x, y, z = current
    neib_coords = (x - 1, y, z), (x + 1, y, z), (x, y - 1, z), (x, y + 1, z), (x, y, z - 1), (x, y, z + 1)
    for nx, ny, nz in neib_coords:
        try:
            val = lava_droplet[nx][ny][nz]
            if not val and val not in visited:
                to_visit.append((nx, ny, nz))
        except:
            pass
    visited.add(current)

sum_of_neib_count_with_bubbles = sum([count_neighbours(lava_droplet, c) for c in lava])
sum_of_neib_count = sum([count_neighbours(lava_droplet, c, visited) for c in lava])

part1 = len(lava) * 6 - sum_of_neib_count_with_bubbles
part2 = len(lava) * 6 - sum_of_neib_count
print(part1)
print(part2)
