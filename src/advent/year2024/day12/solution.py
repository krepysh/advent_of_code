from collections import deque

grid = open(0).read().splitlines()

regions = []
seen = set()
rows = len(grid)
cols = len(grid)

for r_start in range(rows):
    for c_start in range(cols):
        region = []
        q = deque()
        q.append((r_start, c_start))
        char = grid[r_start][c_start]
        while q:
            r, c = q.pop()
            if (r, c,) in seen: continue
            region.append((r, c,))
            seen.add((r, c,))
            for new_r, new_c in ((r + 1, c,), (r - 1, c,), (r, c + 1,), (r, c - 1)):
                if 0 <= new_r < rows and 0 <= new_c < cols:
                    if (new_r, new_c,) in seen:
                        continue
                    if grid[new_r][new_c] == char:
                        q.append((new_r, new_c))
        if region:
            regions.append(region)


def get_region_perimetr(region: list[tuple[int, int]]):
    perimetr = 4 * len(region)
    for r, c in region:
        for nr, nc in ((r + 1, c,), (r - 1, c,), (r, c + 1,), (r, c - 1)):
            if (nr, nc) in region:
                perimetr -= 1
    return perimetr


total = 0
for r in regions:
    total += len(r) * get_region_perimetr(r)
print(total)
