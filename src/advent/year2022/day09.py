from advent import read_input

SIZE = 400
s_x, s_y = SIZE // 2, SIZE - 1 - SIZE//2

lines = read_input('day09.txt')


class Point:
    def __init__(self, x=0, y=0, label=None):
        self.x = x
        self.y = y
        self.label = label

    def distance(self, other: 'Point'):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 1 / 2

    def vect_distance(self, other: 'Point'):
        return Point(self.x - other.x, self.y - other.y)

    def __repr__(self):
        return self.label


class Rope:
    def __init__(self, rope_len=2):
        self.segments = []
        for i in range(rope_len):
            self.segments.append(Point(label=str(rope_len - 1 - i)))
        self.head = self.segments[-1]
        self.head.label = 'H'
        self.tail = self.segments[0]

    def adjust_to_head(self):
        for i in range(len(self.segments) - 2, -1, -1):
            current = self.segments[i]
            closer_to_head = self.segments[i + 1]
            if closer_to_head.distance(current) > 1:
                vector = closer_to_head.vect_distance(current)
                if vector.x == 0 or vector.y == 0:
                    current.x = current.x + vector.x // 2
                    current.y = current.y + vector.y // 2
                else:
                    current.x = current.x + vector.x // abs(vector.x)
                    current.y = current.y + vector.y // abs(vector.y)

    def up(self):
        self.head.y += 1
        self.adjust_to_head()

    def down(self):
        self.head.y -= 1
        self.adjust_to_head()

    def right(self):
        self.head.x += 1
        self.adjust_to_head()

    def left(self):
        self.head.x -= 1
        self.adjust_to_head()


def print_rope(rope: Rope, size=SIZE):
    field = [['.'] * size for _ in range(size)]
    for point in rope.segments:
        try:
            field[s_y - point.y][point.x + s_x] = str(point)
        except IndexError:
            pass
    field[s_y][s_x] = 's'
    for line in field:
        print(''.join(line))
    print()


def print_visited(visted: set[tuple[int, int]], size=SIZE):
    field = [['.'] * size for _ in range(size)]
    for x, y in visted:
        try:
            field[s_y - y][x + s_x] = '#'
        except IndexError:
            pass
    field[s_y][s_x] = 's'
    for line in field:
        print(''.join(line))
    print()


rope = Rope(rope_len=10)
# print_rope(rope)
movements = {'R': rope.right, 'L': rope.left, 'U': rope.up, 'D': rope.down}
visited = set()
for move in lines:
    direction, num = move.strip().split()
    # print(f'== {direction} {num} ==\n')
    num = int(num)
    while num > 0:
        method_to_call = movements[direction]
        method_to_call()
        num -= 1
        visited.add((rope.tail.x, rope.tail.y))
    # print_rope(rope)

print_visited(visited)
print(len(visited))
