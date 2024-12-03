import re

with open("day03.txt", "r") as fp:
    program = fp.read()

commands = re.findall("(mul\(\d+,\d+\)|do\(\)|don't\(\))", program)


def run_mul_command(cmd: str) -> int:
    a, b = re.search("mul\((\d+),(\d+)\)", cmd).groups()
    a, b = int(a), int(b)
    return a * b


filtered_commands = []
on = True
part_2 = True
s = 0
for cmd in commands:
    if cmd.startswith('mul'):
        if on:
            filtered_commands.append(cmd)
            s += run_mul_command(cmd)
    elif cmd.startswith('do('):
        on = True
    elif part_2 and cmd.startswith('don'):
        on = False

print(s)
