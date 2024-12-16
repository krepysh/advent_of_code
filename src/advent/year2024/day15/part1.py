grid, moves = open(0).read().split('\n\n')
moves = "".join(m.strip() for m in moves)
grid = [list(line.strip()) for line in grid.split()]

rows = len(grid)
cols = len(grid)

for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "@":
            robot = r, c
            break

directions = {">": (0, 1), "v": (1, 0), "<": (0, -1), "^": (-1, 0)}

for move in moves:
    dr, dc = directions[move]
    for i in range(1, 100):
        r_bot, c_bot = robot
        r = robot[0] + i * dr
        c = robot[1] + i * dc
        item = grid[r][c]
        if item == "#":
            break
        elif item == "O":
            continue
        elif item == ".":
            if i > 1:
                grid[r][c], grid[r_bot + dr][c_bot + dc] = grid[r_bot + dr][c_bot + dc], grid[r][c]
            grid[r_bot + dr][c_bot + dc], grid[r_bot][c_bot] = grid[r_bot][c_bot], grid[r_bot + dr][c_bot + dc]
            robot = r_bot + dr, c_bot + dc
            break
    # print(f"Move: {move}")
    # for row in grid:
    #     print("".join(row))
total = 0
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "O":
            total += 100 * r + c
print(total)
