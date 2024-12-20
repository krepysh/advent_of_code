import heapq

grid = [list(line) for line in open(0).read().splitlines()]

rows = len(grid)
cols = len(grid[0])

rs = cs = re = ce = 0
obs = set()
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "S":
            rs, cs = r, c
            obs.add((r,c))
        elif grid[r][c] == "E":
            re, ce = r, c
        elif grid[r][c] == "#":
            obs.add((r, c))
cheats = {}
i = 0


def get_path_len_with_path(grid):
    q = [(rs, cs, 0, ((rs, cs), ))]
    seen = set()
    while q:
        r, c, price, path = heapq.heappop(q)
        if grid[r][c] == "E":
            # print(price)
            break
        if (r, c) in seen:
            continue
        seen.add((r, c))
        for dr, dc in ((1, 0), (- 1, 0), (0, 1), (0, - 1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] != "#":
                    heapq.heappush(q, (nr, nc, price + 1, path + ((nr, nc),)))
    return price, path


def get_price(grid):
    q = [(rs, cs, 0,)]
    seen = set()
    while q:
        r, c, price = heapq.heappop(q)
        if grid[r][c] == "E":
            # print(price)
            break
        if (r, c) in seen:
            continue
        seen.add((r, c))
        for dr, dc in ((1, 0), (- 1, 0), (0, 1), (0, - 1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] != "#":
                    heapq.heappush(q, (nr, nc, price + 1,))
    return price

full_price, full_path = get_path_len_with_path(grid)
print(full_price)
for tmp_remove in obs:
    i += 1
    if i % 1000 == 0:
        print(f"{i} / {len(obs)}")
    cheat_r, cheat_c = tmp_remove
    grid[cheat_r][cheat_c] = "."
    price = get_price(grid)
    cheats[(cheat_r, cheat_c)] = price
    grid[cheat_r][cheat_c] = "#"

res = 0
max_price = max(cheats.values())
print(full_price, max_price)

for (r, c) in cheats.keys():
    price = cheats[(r,c)]
    if max_price - price >= 100:
        res += 1

print(res)