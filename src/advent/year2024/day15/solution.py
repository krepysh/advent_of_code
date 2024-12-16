grid, moves = open(0).read().split('\n\n')
moves = "".join(m.strip() for m in moves)
grid = [list(line.strip()) for line in grid.split()]

rows = len(grid)
cols = len(grid[0])

twice_grid = []
for r in range(rows):
    current = []
    for c in range(cols):
        if grid[r][c] == ".":
            current.append("..")
        elif grid[r][c] == "#":
            current.append("##")
        elif grid[r][c] == "O":
            current.append("[]")
        if grid[r][c] == "@":
            robot = r, c
            current.append("@.")
    current = list("".join(current))
    twice_grid.append(current)

directions = {">": (0, 1), "v": (1, 0), "<": (0, -1), "^": (-1, 0)}
grid = twice_grid
rows = len(grid)
cols = len(grid[0])

for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "@":
            robot = r, c
            break

for move in moves:
    dr, dc = directions[move]
    targets = [robot]
    go = True
    for r, c in targets:
        nr, nc = r + dr, c + dc
        if (nr, nc) in targets:
            continue
        item = grid[nr][nc]
        if item == "#":
            go = False
            break
        elif item == "[":
            targets.append((nr, nc))
            targets.append((nr, nc + 1))
            continue
        elif item == "]":
            targets.append((nr, nc))
            targets.append((nr, nc - 1))

    if go:
        # print(targets)
        # print("".join(twice_grid[tr][tc] for tr, tc in targets))
        # if dc != 0:
        #     robot, *targets = targets
        #     targets.sort(key=lambda x: x[1], reverse=dc == -1)
        #     targets.insert(0, robot)
        while targets:
            target_r, target_c = targets.pop()
            grid[target_r][target_c], grid[target_r + dr][target_c + dc] = grid[target_r + dr][target_c + dc], \
            grid[target_r][target_c]
            if not targets:
                robot = (target_r + dr, target_c + dc)
    # print(f"Robot: {robot}")
    # print(f"Move: {move}, go: {go}")
for row in grid:
    print("".join(row))

total = 0
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "[":
            total += 100 * r + c
print(total)
