targets, equations = [], []
for line in open(0).readlines():
    target, equation = line.split(": ")
    targets.append(int(target))
    equations.append(list(map(int, equation.split())))


def is_feasible(target, equation: list[int]):
    if len(equation) == 1:
        return equation[0] == target
    first, second = equation[:2]
    return is_feasible(target, [first + second] +  equation[2::]) or is_feasible(target, [first * second] + equation[2::]) or is_feasible(target, [int(f"{first}{second}")] + equation[2::])


res = 0
for target, equation in zip(targets, equations):
    res += target * is_feasible(target, equation)

print(res)
