import operator
from advent import read_input


lines = read_input('day21.txt')
monkeys = {}
for line in lines:
    monkey_name, expression = line.split(': ')
    if expression.isdigit():
        expression = int(expression)
    monkeys[monkey_name] = expression

bin_ops = {'+': operator.add, '-': operator.sub, '/': operator.truediv, '*': operator.mul}


def evaluate_expression(expression: str | int):
    if not isinstance(expression, str):
        return expression
    left_name, op, right_name = expression.split()
    left = evaluate_expression(monkeys[left_name])
    right = evaluate_expression(monkeys[right_name])
    return bin_ops[op](left, right)


# Part 1
print(evaluate_expression(monkeys['root']))


# Part 2
import sympy

humn = sympy.Symbol('x')

done = {'humn': humn}

todo = [(k, v) for k, v in monkeys.items()]
for monkey_name, expr in todo:
    if monkey_name in done:
        continue
    if not isinstance(expr, str):
        done[monkey_name] = sympy.Integer(expr)
        continue
    left, op, right = expr.split()
    if left in done and right in done:
        if monkey_name == 'root':
            print(sympy.solve(done[left] - done[right])[0])
            break
        done[monkey_name] = bin_ops[op](done[left], done[right])
    else:
        # As we don't have values for monkeys in expr, try to process it later
        todo.append((monkey_name, expr))

