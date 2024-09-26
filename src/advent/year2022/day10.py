from advent import read_input


lines = read_input('day10.txt')
# Stack of commands
operations = lines[::-1]

reper = [20, 60, 100, 140, 180, 220]

acc = 0
x = 1
i = 0
current_row = []
rows = []
while operations:
    # part 2
    beam_pos = (i) % 40
    pixel = '#' if beam_pos - 1 <= x <= beam_pos + 1 else '.'
    current_row.append(pixel)
    if len(current_row) > 39:
        rows.append(current_row)
        current_row = []
    i += 1
    # part 1
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

for row in rows:
    print(''.join(row))