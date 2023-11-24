import operator
from advent import read_input


lines = read_input('day21.txt')
monkeys = {}
for line in lines:
    monkey_name, expression = line.split(': ')
    if expression.isdigit():
        expression = int(expression)
    monkeys[monkey_name] = expression


def evaluate_expression(expression: str | int):
    if not isinstance(expression, str):
        return expression
    left_name, op, right_name = expression.split()
    left = evaluate_expression(monkeys[left_name])
    right = evaluate_expression(monkeys[right_name])
    bin_ops = {'+': operator.add, '-': operator.sub, '/': operator.truediv, '*': operator.mul}
    return bin_ops[op](left, right)


# Part 1
print(evaluate_expression(monkeys['root']))
