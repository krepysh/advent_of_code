rows = 71
cols = 71
corrupted_bytes = 1024

grid = [[float("inf")] * cols for _ in range(rows)]
rows = len(grid)
cols = len(grid[0])
orig_grid = [row[:] for row in grid]

corrupteds = [tuple(map(int, line.split(","))) for line in open(0).read().splitlines()]


def simulate(grid, n_bytes: int):
    for i in range(n_bytes):
        c, r = corrupteds[i % len(corrupteds)]
        try:
            grid[r][c] = "#"
        except Exception:
            print(r, c)
            raise

    grid[0][0] = 0
    cells = [(0, 0)]

    for r, c in cells:
        current_value = grid[r][c]
        if r == c == rows - 1:
            return current_value
        for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] == "#":
                    continue
                elif grid[nr][nc] > current_value + 1:
                    grid[nr][nc] = current_value + 1
                    cells.append((nr, nc))
    return grid[rows - 1][cols - 1]


def bin_search(start, stop):
    while (stop - start) > 1:
        midle = (start + stop) // 2
        grid = [row[:] for row in orig_grid]
        if simulate(grid, midle) < float("inf"):
            start = midle
        else:
            stop = midle
    return stop


ans = bin_search(1, len(corrupteds))
print(ans)
print(*corrupteds[ans - 1], sep=",")
