from typing import Tuple


def read_input() -> Tuple[list[int], list[int]]:
    left, right = [], []
    with open("day01.txt") as fp:
        for line in fp.readlines():
            number_left, number_right = [int(n) for n in line.split()]
            left.append(number_left)
            right.append(number_right)
    return left, right


def calculate_distance(left: list[int], right: list[int]) -> int:
    distance = 0
    for number_left, number_right in zip(left, right):
        distance += abs(number_right - number_left)
    return distance


def calculate_similarity_score(left: list[int], right: list[int]) -> int:
    score = 0
    for left_number in left:
        score += left_number * right.count(left_number)
    return score


if __name__ == "__main__":
    left, right = read_input()
    left.sort()
    right.sort()
    part1 = calculate_distance(left, right)
    part2 = calculate_similarity_score(left, right)
    print(f"Part 1 answer: {part1}")
    print(f"Part 2 answer: {part2}")
