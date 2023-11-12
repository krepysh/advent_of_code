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

visited = set()
heap = [(0, start)]
while True:
    current_dist, current_coord = heapq.heappop(heap)
    if current_coord == end:
        print('Part 1, distance:', current_dist)
        break
    if current_coord in visited:
        continue
    for neib in get_neighbours(*current_coord):
        heapq.heappush(heap, (current_dist + 1, neib))
    visited.add(current_coord)
