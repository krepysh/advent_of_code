import heapq

grid = open(0).read().splitlines()

rows = len(grid)
cols = len(grid[0])

sr = sc = er = ec = 0

for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "S":
            sr, sc = r, c
        elif grid[r][c] == "E":
            er, ec = r, c

heap = [(0, sr, sc, 0, 1, ((sr, sc),))]

prices = []
i = 0
lowest_price = {(sr, sc, 0, 1): 0}
best_paths = set()
while heap:
    price, r, c, dr, dc, path = heapq.heappop(heap)
    if grid[r][c] == "E":
        prices.append((price, path))
    if price > lowest_price.get((r, c, dr, dc), float("inf")):
        continue
    lowest_price[(r, c, dr, dc)] = price

    if grid[r + dr][c + dc] != "#":
        heapq.heappush(heap, (price + 1, r + dr, c + dc, dr, dc, path + ((r + dr, c + dc,),)))
    # turn right:
    heapq.heappush(heap, (price + 1000, r, c, dc, -dr, path))
    # turn back:
    # turn left:
    heapq.heappush(heap, (price + 1000, r, c, -dc, dr, path))

for price, path in prices:
    if price == prices[0][0]:
        best_paths.update(path)

print(len(best_paths))
