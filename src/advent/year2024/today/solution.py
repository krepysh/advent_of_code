base = 16777216


def random(start):
    secret = start
    secret = secret ^ (secret * 64)
    secret = secret % base
    secret = secret ^ (secret // 32)
    secret = secret % base
    secret = secret ^ (secret * 2048)
    secret = secret % base
    return secret


res = 0
pattern_to_profit = {}
for start in open(0):
    start = int(start)
    monkey = [start % 10]
    seen = set()
    for i in range(2000):
        start = random(start)
        monkey.append(start % 10)
        if len(monkey) >= 5:
            a, b, c, d, e = monkey
            monkey.pop(0)
            diffs = (b - a, c - b, d - c, d - e)
            if diffs in seen:
                continue
            seen.add(diffs)
            pattern_to_profit[diffs] = pattern_to_profit.get(diffs, 0) + e

print(max(pattern_to_profit.items(), key=lambda x: x[1]))
