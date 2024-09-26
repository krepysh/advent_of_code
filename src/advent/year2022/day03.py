from typing import Iterable


def read_input():
    filename = 'day03.txt'
    with open(filename, 'r') as f:
        lines = f.readlines()
    lines = [l.strip() for l in lines]
    return lines


def get_priority(letter: str):
    base = 1 if letter.islower() else 27
    return base + ord(letter.lower()) - ord('a')


def get_priorities_sum(letters: Iterable[str]):
    return sum(map(get_priority, letters))


rucksacks = read_input()
part1 = 0
part2 = 0
for rucksack in rucksacks:
    half = len(rucksack) // 2
    first, second = rucksack[:half], rucksack[half:]
    in_both = set(first).intersection(second)
    part1 += get_priorities_sum(in_both)

for i in range(0, len(rucksacks), 3):
    group = rucksacks[i:i+3]
    badge = set(group[0]).intersection(group[1]).intersection(group[2])
    part2 += get_priorities_sum(badge)

print(part1)
print(part2)
