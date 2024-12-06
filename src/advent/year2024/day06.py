gards = "^>v<"


def get_len_path(grid: list[list[str]]) -> int:
    res = 0
    visited = {}
    gards = "^>v<"
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] in gards:
                gard_position = i, j,
                gard_type = grid[i][j]
    cache = {}
    while (gard_position, gard_type) not in cache:
        visited[gard_position] = True
        cache[(gard_position, gard_type)] = True
        y, x = gard_position
        directions = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
        dy, dx = directions.get(gard_type)
        if not 0 <= y + dy < len(grid) or not 0 <= x + dx < len(grid[0]):
            break
        elif grid[y + dy][x + dx] == ".":
            grid[y][x] = "."
            gard_position = y + dy, x + dx
        else:
            gard_type = get_next(gard_type)
        grid[gard_position[0]][gard_position[1]] = gard_type
    return len(visited)


def get_next(gard_type):
    return gards[(gards.index(gard_type) + 1) % len(gards)]


if __name__ == "__main__":
    input_f = open(0).read().splitlines()
    grid = [list(l) for l in input_f]
    print(get_len_path(grid))
