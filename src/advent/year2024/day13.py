import re

from z3 import Int, Optimize, sat


def read_input():
    results = []
    triplet = []
    with open("day13.txt", "r") as fp:
        for line in fp.read().splitlines():
            if line == "":
                results.append(triplet)
                triplet = []
            else:
                pair = [int(d) for d in re.findall("\d+", line)]
                triplet.append(pair)
        results.append(triplet)
    return results



def find_lowest_price(a_vals: tuple[int, int], b_vals: tuple[int, int], prize_coords: tuple[int, int]):
    a = Int('a')
    b = Int('b')
    opt = Optimize()

    opt.add(a * a_vals[0] + b * b_vals[0] == 10000000000000 + prize_coords[0])
    opt.add(a * a_vals[1] + b * b_vals[1] == 10000000000000 + prize_coords[1])
    opt.add(0 <= a)
    # opt.add(a <= 100)
    opt.add(0 <= b)
    # opt.add(b <= 100)
    opt.minimize(3 * a + b)
    if opt.check() == sat:
        m = opt.model()
        return 3 * m[a].as_long() + m[b].as_long()
    else:
        return 0


if __name__ == "__main__":
    res = 0
    for triplet in read_input():
        res += find_lowest_price(*triplet)
    print(res)
