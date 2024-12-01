from typing import Tuple


def read_indput() -> Tuple[list[int], list[int]]:
    left, right = [], []
    with open("day01.txt") as fp:
        for line in fp.readlines():
            number_left, number_right = [int(n) for n in line.split()]
            left.append(number_left)
            right.append(number_right)
    return left, right


def calculate_distance(left: list[int], right: list[int]) -> int:
    left.sort()
    right.sort()
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
    part1 = calculate_distance(*read_indput())
    part2 = calculate_similarity_score(*read_indput())
    print(part2)
