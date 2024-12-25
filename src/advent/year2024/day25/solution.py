all_items = [line.split() for line in open(0).read().split('\n\n')]

keys, locks = [], []


def parse(item):
    key = tuple(row.count("#") - 1 for row in zip(*item[1:]))
    return key


for item in all_items:
    parsed = parse(item)
    if item[0] == "#####":
        locks.append(parsed)
    elif item[0] == ".....":
        keys.append(parsed)

res = 0
for key in keys:
    for lock in locks:
        if all(a + b < 5 for a, b in zip(key, lock)):
            res += 1
print(res)
