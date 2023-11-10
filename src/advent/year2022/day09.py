from advent import read_input


lines = read_input('day09.txt')


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance(self, other: 'Point'):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 1/2

    def vect_distance(self, other: 'Point'):
        return Point(self.x - other.x, self.y - other.y)


class Rope:
    def __init__(self, len=2):
        self.segments = []
        for _ in range(2):
            self.segments.append(Point())
        self.head = self.segments[-1]
        self.tail = self.segments[0]

    def adjust_to_head(self):
        if self.head.distance(self.tail) > 1:
            vector = self.head.vect_distance(self.tail)
            if vector.x == 0 or vector.y == 0:
                self.tail.x = self.tail.x + vector.x // 2
                self.tail.y = self.tail.y + vector.y // 2
            else:
                self.tail.x = self.tail.x + vector.x // abs(vector.x)
                self.tail.y = self.tail.y + vector.y // abs(vector.y)

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


rope = Rope()
movements = {'R': rope.right, 'L': rope.left, 'U': rope.up, 'D': rope.down}
visited = set()
for move in lines:
    direction, num = move.strip().split()
    num = int(num)
    while num > 0:
        method_to_call = movements[direction]
        method_to_call()
        num -= 1
        visited.add((rope.tail.x, rope.tail.y))

print(len(visited))
