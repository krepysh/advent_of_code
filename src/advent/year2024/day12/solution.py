from collections import deque

grid = open(0).read().split()

rows = len(grid)
cols = len(grid[0])

areas = []
seen = set()


def get_area(start_r, start_c):
    q = deque()
    q.append((start_r, start_c))
    char = grid[start_r][start_c]
    area = []
    while q:
        r, c = q.pop()
        if (r, c) in seen: continue
        area.append((r, c))
        seen.add((r, c))
        for nr, nc in ((r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)):
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] == char:
                    q.append((nr, nc))
    return area


for r in range(rows):
    for c in range(cols):
        if (r, c) not in seen:
            areas.append(get_area(r, c))


def get_price(area: list[tuple[int, int]]):
    square = len(area)
    perimeter = 4 * square
    for r, c in area:
        for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[r][c] == grid[nr][nc]:
                    perimeter -= 1
    return square * perimeter


def count_edges(area: list[tuple[int, int]]):
    edges = 0

    for r, c in area:
        north_n = r - 1, c
        west_n = r, c - 1
        north_west_n = r - 1, c - 1
        if north_n not in area:
            same_edge = (west_n in area) and (north_west_n not in area)
            if not same_edge:
                edges += 1
        south_n = r + 1, c
        south_west_n = r + 1, c - 1

        if south_n not in area:
            same_edge = west_n in area and south_west_n not in area
            if not same_edge:
                edges += 1

        if west_n not in area:
            same_edge = (north_n in area) and  north_west_n not in area
            if not same_edge:
                edges += 1

        east_n = r, c + 1
        north_east_n = r -1, c + 1
        if east_n not in area:
            same_edge = (north_n in area) and north_east_n not in area
            if not same_edge:
                edges += 1

    return edges


r = 0
for a in areas:
    r += count_edges(a) * len(a)

print(r)
