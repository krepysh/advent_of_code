import contextlib


def check_grid_pos(puzzle, x, y):
    res = 0
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if dx == dy == 0:
                continue
            for step in range(1, 4):
                x_pos = x + step * dx
                y_pos = y + step * dy
                with contextlib.suppress(IndexError):
                    char = puzzle[y_pos][x_pos]
                if x_pos < 0 or y_pos < 0 or char != "XMAS"[step]:
                    break
                if char == "S" and step == 3:
                    res += 1
    return res


def part1_xmas_solution(puzzle):
    res = 0
    for x in range(len(puzzle[0])):
        for y in range(len(puzzle)):
            if puzzle[y][x] == "X":
                res += check_grid_pos(puzzle, x, y)
    return res


def is_opposite(ch1, ch2):
    return (ch1 == "M" and ch2 == "S") and (ch1 == "S" and ch2 == "M")


def check_grid_pos_m_as(puzzle, x, y):
    p = puzzle
    chars = [p[y - 1][x - 1], p[y - 1][x + 1], p[y + 1][x + 1], p[y + 1][x - 1]]
    chars = "".join(chars)
    return chars in ["SSMM", "SMMS", "MMSS", "MSSM"]


def part2_x_mas_solution(puzzle):
    res = 0
    for x in range(1, len(puzzle[0]) - 1):
        for y in range(1, len(puzzle) - 1):
            if puzzle[y][x] == "A":
                res += check_grid_pos_m_as(puzzle, x, y)
    return res


if __name__ == "__main__":
    puzzle_input = open(0).readlines()
    puzzle = [list(row) for row in puzzle_input]
    result = part1_xmas_solution(puzzle)
    print(f"Total occurrences of XMAS: {result}")
    print(f"Total occurences of X-MAS: {part2_x_mas_solution(puzzle)}")
