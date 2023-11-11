from advent import read_input


operations = read_input('day10.txt')
# Stack of commands
operations = operations[::-1]

reper = [20, 60, 100, 140, 180, 220]

acc = 0
x = 1
i = 0
while operations:
    i += 1
    if i in reper:
        acc += x * i
    cmd = operations.pop()
    try:
        instruction, val = cmd.split()
    except ValueError:
        instruction = cmd
        val = 0
    if instruction == 'addx':
        # Add "second part" of addx instruction
        operations.append(f'x {val}')
    elif instruction == 'x':
        x += int(val)

print(acc)
