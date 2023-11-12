from advent import read_input

signal_pairs = read_input('day13.txt', by_group=True)


def ensure_list(signal):
    if not isinstance(signal, list):
        signal = [signal]
    return signal


def check_signals(s1, s2):
    s1 = ensure_list(s1)
    s2 = ensure_list(s2)
    # print(s1, s2)
    for i1, i2 in zip(s1, s2):
        if isinstance(i1, int) and isinstance(i2, int):
            if i1 > i2:
                return False
            elif i1 < i2:
                return True
        else:
            res = check_signals(i1, i2)
            if res is not None:
                return res
    if len(s2) != len(s1):
        return len(s2) >= len(s1)


r = 0
for n, (s1, s2) in enumerate(signal_pairs):
    s1, s2 = eval(s1), eval(s2)
    print(n + 1, check_signals(s1, s2))
    r += (n + 1) * check_signals(s1, s2)
print('Part 1 sum:', r)
