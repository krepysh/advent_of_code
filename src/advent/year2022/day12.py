import heapq

from advent import read_input


maze = read_input('day12.txt')

for row_num in range(len(maze)):
    for j in range(len(maze[0])):
        symb = maze[row_num][j]
        if symb == 'S':
            start = row_num, j
        elif symb == 'E':
            end = row_num, j


def val(i, j):
    symb = maze[i][j]
    if symb == 'S':
        symb = 'a'
    elif symb == 'E':
        symb = 'z'
    return ord(symb)


def sane(y, x) -> bool:
    return y in range(len(maze)) and x in range(len(maze[0]))


def get_neighbours(i, j):
    neibs = []
    for y, x in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
        if sane(y, x):
            if val(y, x) - val(i, j) < 2:
                neibs.append((y, x))
    return neibs


def get_distance(start, end):
    """Return min distance, or -1 if path not found.

    Dijkstra algorythm.
    """
    visited = set()
    heap = [(0, start)]
    while True:
        if not heap:
            return -1
        current_dist, current_coord = heapq.heappop(heap)
        if current_coord == end:
            return current_dist
        if current_coord in visited:
            continue
        for neib in get_neighbours(*current_coord):
            heapq.heappush(heap, (current_dist + 1, neib))
        visited.add(current_coord)


print('Part 1, distance:', get_distance(start, end))

distances = []
row_num = 0
for row_num in range(len(maze)):
    for j in range(len(maze[0])):
        if maze[row_num][j] == 'a':
            dist = get_distance((row_num, j), end)
            if dist > 0:
                heapq.heappush(distances, dist)

print('Part 2, min ditance:', heapq.nsmallest(1, distances)[0])
