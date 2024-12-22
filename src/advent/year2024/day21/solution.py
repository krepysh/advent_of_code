from itertools import product, permutations


def find(keyboard, button):
    for r in range(len(keyboard)):
        for c in range(len(keyboard[0])):
            if keyboard[r][c] == button:
                return r, c
    raise ValueError(f"No key found '{button}'")


def minus(a, b) -> tuple[int, int]:
    return a[0] - b[0], a[1] - b[1]


def solve(keyboard, s: str):
    segments = []
    void_row, void_col = find(keyboard, " ")
    sr, sc = find(keyboard, "A")
    r, c = sr, sc

    def hover_to(button, r, c):
        target_pos = find(keyboard, button)
        dr, dc = minus(target_pos, (r, c))
        down = dr if dr > 0 else 0
        right = dc if dc > 0 else 0
        left = -dc if dc < 0 else 0
        up = -dr if dr < 0 else 0
        choices = []

        steps = f"{'<' * left}{'>' * right}{'v' * down}{'^' * up}"
        all_possible_steps = set(permutations(steps))
        if c + dc == void_col:
            if r == void_row:
                # we'are about to step on the void, on the left hand of us ups...
                all_possible_steps.remove(tuple(f"{'<' * left}{'v' * down}{'^' * up}"))
        if c == void_col:
            if r + dr == void_row:
                # we'are about to step on the void, it is above us...
                all_possible_steps.remove(tuple(f"{'v' * down}{'^' * up}{'<' * left}{'>' * right}"))
        for step in all_possible_steps:
            choices.append("".join(step) + "A")

        r, c = target_pos
        return (r, c), choices

    for button in s:
        (r, c), results = hover_to(button, r, c)
        segments.append(results)
    # all combinations of segments
    return ["".join(p) for p in product(*segments)]


dig_keyboard = [list("789"), list("456"), list("123"), list(" 0A")]
numpad = [
    [" ", "^", "A"],
    ["<", "v", ">"],
]
codes = open(0).read().splitlines()


total = 0
for code in codes:
    min_len = 1000
    for posibility in solve(dig_keyboard, code):
        for posibility2 in solve(numpad, posibility):
            for posibility3 in solve(numpad, posibility2):
                if len(posibility3) < min_len:
                    min_len = len(posibility3)
    total += int(code[:-1]) * min_len
    print(min_len)

print(total)

