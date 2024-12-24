from collections import defaultdict

top, bottom = open(0).read().split("\n\n")


def simulate(bit_num=0):
    wires = defaultdict()
    gates = {}

    for line in top.strip().split("\n"):
        wire, state = line.split(": ")
        wires[wire] = int(0)
        if wire == f"y{str(bit_num).rjust(2, '0')}": # conditionally adds a leading zero e.g. y06 but y22
            wires[wire] = 1

    for line in bottom.strip().split("\n"):
        # x00 AND y00 -> z00
        condition, output = line.split(" -> ")
        condition = tuple(condition.split())
        gates[output] = condition

    def calc(wire1, op, wire2):
        if wires.get(wire1) is None:
            wires[wire1] = calc(*gates[wire1])
        if wires.get(wire2) is None:
            wires[wire2] = calc(*gates[wire2])
        if op == "AND":
            return wires[wire1] & wires[wire2]
        if op == "OR":
            return wires[wire1] | wires[wire2]
        if op == "XOR":
            return wires[wire1] ^ wires[wire2]

    output = []
    for k in gates:
        if k[0] == "z":
            val = calc(*gates[k])
            wires[k] = val
            output.append(f'{k}: {wires[k]}')

    bits = [0] * len(output)

    for line in output:
        wire, val = line.split(": ")
        wire_number = int(wire[1:])
        bits[wire_number] = val

    # print(int("".join(bits[::-1]), base=2))
    return int("".join(bits[::-1]), base=2)


for i in range(45):
    """The idea here is to find "failing" bits, by adding two numbers, where only one bit set to 1.
    It's not a general approach, but it what I'd do with physical adder in order to debug it.
    Then, let's say  for bit number 6, I searched for x06, y06, z06 in the input file, draw a scheme,
    and find problems.
    x06 and y06 are both connected to XOR and AND gate
    z06 should be connected to XOR gate
    """

    val = simulate(i)
    if val != 2 ** i:
        print(i, f"val: {val}, should be: {2 ** i}")

changed = ["fdv", "dbp", "z15", "ckj", "kdf", "z23", "rpp", "z39"] # manual search

changed.sort()
print(",".join(changed))
