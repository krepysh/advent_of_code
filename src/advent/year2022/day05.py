def read_input():
    filename = 'day05.txt'
    with open(filename, 'r') as f:
        lines = f.readlines()
    sep = lines.index('\n')
    stacks, moves = lines[:sep], lines[sep+1:]
    moves = [l.strip() for l in moves]
    return stacks, moves


def parse_stacks(stacks_str: list[str]):
    labels = stacks_str[-1].split()
    stacks = {}
    for stack_num in labels:
        new_stack = []
        current_pos = stacks_str[-1].index(stack_num)
        for line in stacks_str[-2::-1]:
            try:
                crate = line[current_pos]
            except IndexError:
                crate = ' '
            if crate.isspace():
                break
            new_stack.append(crate)
        stacks[stack_num] = new_stack
    return stacks


def parse_moves(moves):
    rv = []
    for move in moves:
        move, to_num = move.split(' to ')
        move, from_num = move.split(' from ')
        _, amount = move.split('move ')
        amount = int(amount)
        rv.append((amount, from_num, to_num))
    return rv


stacks, moves = read_input()
stacks = parse_stacks(stacks)
for crate_amount, from_label, to_label in parse_moves(moves):
    tmp = []
    for i in range(crate_amount):
        tmp.append(stacks[from_label].pop())
    while tmp:
        stacks[to_label].append(tmp.pop())
out = ''.join([stacks[str(s_num)][-1] for s_num in range(1, len(stacks) + 1)])
print(out)
