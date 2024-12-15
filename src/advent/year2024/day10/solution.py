from collections import deque

grid = [list(map(int, line.strip())) for line in open(0).readlines()]

rows = len(grid)
cols = len(grid[0])

trailheads = []

for r in range(rows):
    for c in range(cols):
        if grid[r][c] == 0:
            trailheads.append((r, c,))


def get_score(head_r, head_c):
    q = deque()
    q.append((head_r, head_c,))
    nines = set()
    score = 0
    while q:
        cur_r, cur_c = q.pop()
        for r, c in ((cur_r + 1, cur_c), (cur_r - 1, cur_c), (cur_r, cur_c + 1), (cur_r, cur_c - 1)):
            if 0 <= r < rows and 0 <= c < cols:
                if grid[r][c] == grid[cur_r][cur_c] + 1:
                    if grid[r][c] == 9:
                        nines.add((r, c))
                        score += 1
                        continue
                    else:
                        q.append((r, c,))
    return score


print(sum(get_score(*head) for head in trailheads))
