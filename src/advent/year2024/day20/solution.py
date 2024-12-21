import heapq

grid = [list(line) for line in open(0).read().splitlines()]

rows = len(grid)
cols = len(grid[0])

rs = cs = re = ce = 0
walls = set()
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "S":
            rs, cs = r, c
        elif grid[r][c] == "E":
            re, ce = r, c
        elif grid[r][c] == "#":
            walls.add((r, c))
cheats = {}
i = 0


def get_price(grid):
    q = [(0, 0, True, rs, cs)]
    seen = set()
    while q:
        price, cheat_steps_remaining, cheatmode, r, c = heapq.heappop(q)
        if grid[r][c] == "E":
            return price
        if (r, c) in seen or grid[r][c] == "#" and cheat_steps_remaining == 0:
            continue
        seen.add((r, c))
        for dr, dc in ((1, 0), (- 1, 0), (0, 1), (0, - 1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if cheat_steps_remaining > 0:
                    heapq.heappush(q, (price + 1, cheat_steps_remaining - 1, False, nr, nc))
                elif grid[nr][nc] != "#":
                    heapq.heappush(q, (price + 1, 0, cheatmode, nr, nc))
                    if cheatmode:
                        heapq.heappush(q, (price + 1, 20, False, nr, nc))


full_price = get_price(grid)
print(full_price)
for (wr, wc) in walls:
    i += 1
    if i % 100 == 0:
        print(f"{i} / {len(walls)}")
    cheat_r, cheat_c = wr, wc
    price = get_price(grid)
    cheats[(cheat_r, cheat_c)] = price

res = 0
max_price = max(cheats.values())
print(full_price, max_price)

for (r, c), price in cheats.items():
    if full_price - price >= 10:
        res += 1

print(res)
