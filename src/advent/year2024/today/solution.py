code = "029A"


class Robot:
    def __init__(self, keyboard=None):
        self.keyboard = keyboard or [
            [" ", "^", "A"],
            ["<", "v", ">"],
        ]
        self.rows = len(self.keyboard)
        self.cols = len(self.keyboard[0])
        self.void_row, col = self.find(" ")
        self.current_position = self.find("A")

    def get_current(self):
        r, c = self.current_position
        return self.keyboard[r][c]

    def find(self, button):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.keyboard[r][c] == button:
                    return r, c
        raise ValueError(f"No key found '{button}'")

    def get_sequence_to(self, button):
        target_position = self.find(button)
        row, col = self.current_position
        dr, dc = self.minus(target_position, self.current_position)
        down = dr if dr > 0 else 0
        right = dc if dc > 0 else 0
        left = -dc if dc < 0 else 0
        up = -dr if dr < 0 else 0
        if self.void_row == row and left != 0:
            path = f"{'^' * up}{'v' * down}{'<' * left}A"

        else:
            path = f"{'<' * left}{'v' * down}{'^' * up}{'>' * right}A"

        assert self.current_position == target_position
        return path

    def minus(self, a, b) -> tuple[int, int]:
        return a[0] - b[0], a[1] - b[1]

    def get_shortest_path_to(self, targets:str):
        res = []
        for target in targets:
            res.append(self.get_sequence_to(target))
        return "".join(res)



dig_keyboard = [list("789"), list("456"), list("123"), list(" 0A")]
dig_robot = Robot(keyboard=dig_keyboard)
rad_robot = Robot()
cold_robot = Robot()
codes = open(0).read().splitlines()
res = 0
for code in codes:
    seq = cold_robot.get_shortest_path_to(rad_robot.get_shortest_path_to(dig_robot.get_shortest_path_to(code)))
    print(seq)
    print(f"{len(seq)} * {int(code[:-1])}")
    res += len(seq) * int(code[:-1])
print(res)
