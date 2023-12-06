import itertools
import re

from advent import read_input


def extract_list_int(s):
    if isinstance(s, list):
        s = s[0]
    return list(map(int, re.findall('\d+', s)))


times, distances = read_input('day06.txt')
times = extract_list_int(times.replace(' ', ''))
distances = extract_list_int(distances.replace(' ', ''))

wins = []
for t, d in zip(times, distances):
    count_win_strategies = 0
    for x in range(t):
        if x * (t - x) > d:
            count_win_strategies += 1
    wins.append(count_win_strategies)

res = 1
for w in wins:
    res *= w
print(res)
