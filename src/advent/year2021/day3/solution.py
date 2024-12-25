from sympy.abc import epsilon

lines = open(0).read().split()
reports = [int(n, base=2) for n in lines]


l = len(lines[0])
gamma_rate = []
for p in range(l):
    if sum((r & 1 << p) > 0 for r in reports) > len(reports) / 2:
        gamma_rate.append(1)
    else:
        gamma_rate.append(0)

gamma_value = 0
epsilon_value = 0
for i, bit in enumerate(gamma_rate):
    gamma_value += bit << i
    epsilon_value += (0 if bit else 1) << i

# epsilon_value = ~ gamma_value
print(epsilon_value * gamma_value)