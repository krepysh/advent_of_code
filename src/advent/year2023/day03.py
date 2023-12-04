from advent import read_input


lines = read_input('day03.txt')


digits = [(0, 3), (5, 8)]


class Engine:
    def __init__(self, parts: list[str]):
        self.parts = parts
        self.len_line = len(self.parts[0])
        self.candidates = []

    def is_special_at_pos(self, x: int, line_num: int):
        if x < 0 or x >= self.len_line:
            return False
        if line_num < 0 or line_num >= len(self.parts):
            return False
        symb = self.parts[line_num][x]
        return symb != '.' and not symb.isdigit()

    def is_part_number(self, begin: int, end: int, line_num: int):
        for x in range(begin - 1, end + 1):
            if self.is_special_at_pos(x, line_num + 1) or self.is_special_at_pos(x, line_num - 1):
                return True
        return self.is_special_at_pos(begin - 1, line_num) or self.is_special_at_pos(end, line_num)

    def find_potential_parts(self):
        for line_num in range(len(self.parts)):
            begin = 0
            while begin < self.len_line:
                while begin < self.len_line and not self.parts[line_num][begin].isdigit():
                    begin += 1
                if begin >= self.len_line:
                    break
                end = begin
                while end + 1 < self.len_line and self.parts[line_num][end].isdigit():
                    end += 1
                self.candidates.append((begin, end, line_num))
                begin = end + 1

    def run(self):
        self.find_potential_parts()
        s = 0
        for begin, end, line_num in self.candidates:
            if self.is_part_number(begin, end, line_num):
                part = int(self.parts[line_num][begin:end])
                print(begin, end, line_num, part)
                s += part
        return s

engine = Engine(lines)

print(engine.run())
print(engine.is_part_number(0, 3, 4))
print(engine.parts[4][0:3])
