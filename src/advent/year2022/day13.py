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


signals = []
r = 0
for n, (s1, s2) in enumerate(signal_pairs):
    s1, s2 = eval(s1), eval(s2)
    signals.append(s1)
    signals.append(s2)
    print(n + 1, check_signals(s1, s2))
    r += (n + 1) * check_signals(s1, s2)
print('Part 1 sum:', r)


# part 2
def count_pos(s):
    pos = 0
    for s2 in signals:
        if s != s2:
            pos += check_signals(s, s2)
    return pos


sorted_signals = sorted(signals, key=count_pos, reverse=True)
divider1 = sorted_signals.index([[2]]) + 1
divider2 = sorted_signals.index([[6]]) + 1
print("Part 2 positions:", divider2, divider1)
print("Part 2 multiplication:", divider2 * divider1)
