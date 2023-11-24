import operator
from advent import read_input

lines = ['root: pppw + sjmn', 'dbpl: 5', 'cczh: sllz + lgvd', 'zczc: 2', 'ptdq: dvpt / humn', 'dvpt: 3', 'lfqf: 4', 'humn: 5', 'ljgn: 2', 'sjmn: drzm * dbpl', 'sllz: 4', 'pppw: cczh / lfqf', 'lgvd: ljgn * ptdq', 'drzm: hmdt - zczc', 'hmdt: 32']
# lines = read_input('day21.txt')
monkeys = {}
for line in lines:
    monkey_name, expression = line.split(': ')
    if expression.isdigit():
        expression = int(expression)
    monkeys[monkey_name] = expression

def evaluate_expression(expression: str | int, monkeys):
    if not isinstance(expression, str):
        return expression
    left_name, op, right_name = expression.split()
    left = evaluate_expression(monkeys[left_name], monkeys)
    right = evaluate_expression(monkeys[right_name], monkeys)
    bin_ops = {'+': operator.add, '-': operator.sub, '/': operator.truediv, '*': operator.mul}
    return bin_ops[op](left, right)


# Part 1
print(evaluate_expression(monkeys['root'], monkeys))

humn_old = monkeys['humn']
# Part 2
left_name, _, right_name = monkeys['root'].split(' ')
# print(evaluate_expression(monkeys[left_name]), evaluate_expression(monkeys[right_name]))
monkeys['humn']
# print(evaluate_expression(monkeys[left_name]), evaluate_expression(monkeys[right_name]))
where_it_used = {}
for monkey_name, expression in monkeys.items():
    if isinstance(expression, str):
        left_name, op, right_name = expression.split()
        if left_name in where_it_used or right_name in where_it_used:
            raise ValueError
        where_it_used[left_name] = monkey_name
        where_it_used[right_name] = monkey_name

reversed_tree = {}
reversed_ops = {'-': '+', '+': '-', '*': '/', '/': '*'}
monkeys['humn'] = ''
left, op, right = monkeys['root'].split()
monkeys[left] = monkeys[right] = 150
print(left, op, right)
def reverse_monkey(target):
    if not isinstance(monkeys[target], str):
        return monkeys[target]
    parent = where_it_used[target]
    old_expression = monkeys[parent]
    if not isinstance(old_expression, str):
        return old_expression
    left, op, right = old_expression.split(' ')
    if target == left:
        new_expr = f'{parent} {reversed_ops[op]} {right}'
    else:
        if op == '/':
            new_expr = f'{left} {op} {parent}'
        else:
            new_expr = f'{parent} {reversed_ops[op]} {left}'
    return new_expr
to_process = ['humn']
while to_process:
    target = to_process.pop()
    new_expr = reverse_monkey(target)
    if isinstance(new_expr, str):
        left, op, right = new_expr.split(' ')
        if left not in reversed_tree:
            to_process.append(left)
        if right not in reversed_tree:
            to_process.append(right)
    reversed_tree[target] = new_expr
    print(reversed_tree)

print(evaluate_expression(reversed_tree['humn'], reversed_tree))