filename = 'day01.txt'

with open(filename, 'r') as f:
    current = []
    calories = []
    for raw_line in f.readlines():
        raw_line = raw_line.strip()
        if not raw_line:
            calories.append(current)
            current = []
        else:
            current.append(int(raw_line))

top = [0] * 3
for item in map(sum, calories):
    if item > top[-1]:
        chii = len(top) - 1
        # some kind of insertion sort, but only for top elements
        top[chii] = item
        while chii > 0 and top[chii] > top[chii - 1]:
            top[chii], top[chii - 1] = top[chii - 1], top[chii]
            chii -= 1

print(top[0])
print(sum(top))
