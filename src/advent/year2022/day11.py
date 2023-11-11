from advent import read_input

lines = read_input('day11.txt', by_group=True)


class Monkey:
    def __init__(self, divisible_by, operation: str, if_true: int, if_false: int, items=None, ):
        self.items = items or []
        self.divisible_by = divisible_by
        self.operation = operation
        self.if_true = if_true
        self.if_false = if_false
        self.counter = 0

    def inspect(self):
        worry_level = self.items.pop(0)
        old = worry_level
        new = eval(self.operation)
        new = new // 3
        to_monkey = self.if_true if new % self.divisible_by == 0 else self.if_false
        self.counter += 1
        return new, to_monkey


def parse_monkey(group):
    starting_items = group[1].split(': ')[1].split(', ')
    starting_items = list(map(int, starting_items))
    divisible_by = int(group[3].lstrip('Test: divisible by '))
    operation = group[2].split('=')[1]
    if_true = int(group[4].lstrip('If true: throw to monkey '))
    if_false = int(group[5].lstrip('If false: throw to monkey '))

    return Monkey(divisible_by=divisible_by, operation=operation, if_true=if_true, if_false=if_false,
                  items=starting_items)


class Playground:
    def __init__(self):
        self.monkeys: list[Monkey] = []

    def run_round(self):
        for monkey in self.monkeys:
            while monkey.items:
                item, to_monkey = monkey.inspect()
                self.monkeys[to_monkey].items.append(item)

    def get_highest_scores(self):
        scores = [m.counter for m in self.monkeys]
        scores.sort(reverse=True)
        return scores[0] * scores[1]


playground = Playground()
for group in lines:
    playground.monkeys.append(parse_monkey(group))

for i in range(20):
    playground.run_round()

print(playground.get_highest_scores())
