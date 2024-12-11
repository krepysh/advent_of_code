from functools import cache

stones = [int(s) for s in "814 1183689 0 1 766231 4091 93836 46".split()]

@cache
def get_stones_num(stones, n):
    new_stones = []
    for stone in stones:
        length = len(str(stone))
        if stone == 0:
            new_stones.append(1)
        elif length % 2 == 0:
            new_stones.append(int(str(stone)[0:length//2]))
            new_stones.append(int(str(stone)[length//2:]))
        else:
            new_stones.append(stone * 2024)
    n = n - 1
    if n == 0:
        return len(new_stones)
    return sum(get_stones_num((s,), n) for s in new_stones)


print(get_stones_num(tuple(stones), 75))