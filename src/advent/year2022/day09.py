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


head, tail = Point(), Point()
visited = set()
for move in lines:
    direction, num = move.strip().split()
    num = int(num)
    while num > 0:
        if direction == 'R':
            head.x += 1
        elif direction == 'L':
            head.x -= 1
        elif direction == 'U':
            head.y += 1
        elif direction == 'D':
            head.y -= 1
        num -= 1
        if head.distance(tail) > 1:
            vector = head.vect_distance(tail)
            if vector.x == 0 or vector.y == 0:
                tail.x = tail.x + vector.x // 2
                tail.y = tail.y + vector.y // 2
            else:
                tail.x = tail.x + vector.x // abs(vector.x)
                tail.y = tail.y + vector.y // abs(vector.y)
        visited.add((tail.x, tail.y))

print(len(visited))
