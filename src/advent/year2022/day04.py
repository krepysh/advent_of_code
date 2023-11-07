def read_input():
    filename = 'day04.txt'
    with open(filename, 'r') as f:
        lines = f.readlines()
    lines = [l.strip() for l in lines]
    return lines


lines = read_input()
intervals = [l.split(',') for l in lines]


def prepare_single(interval: str):
    interval = interval.split('-')
    interval = int(interval[0]), int(interval[1])
    return interval


def prepare_pair(pair) -> tuple[tuple[int, int], tuple[int, int]]:
    p1, p2 = pair
    return prepare_single(p1), prepare_single(p2)


def is_nested(r1: tuple[int, int], r2: tuple[int, int]) -> bool:
    return r1[0] <= r2[0] and r1[1] >= r2[1]


part1 = 0
for interval in intervals:
    first, second = prepare_pair(interval)
    if is_nested(first, second) or is_nested(second, first):
        part1 += 1

print(part1)
