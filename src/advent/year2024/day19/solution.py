from functools import cache

top, bottom = open(0).read().split("\n\n")

patterns = top.split(", ")
designs = bottom.splitlines()


@cache
def num_ways(design: str):
    res = 0
    if not design:
        return 1
    for pattern in patterns:
        if design.startswith(pattern):
            res += num_ways(design.removeprefix(pattern))  # I was wrong using lstrip() here ...
    return res


print(sum(num_ways(d) for d in designs))
