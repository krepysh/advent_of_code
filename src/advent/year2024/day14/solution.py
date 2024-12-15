import re

robots = []
STEPS = 100
H = 103
L = 101
X_MEDIUM = (L - 1) // 2
Y_MEDIUM = (H - 1) // 2
for line in open(0).readlines():
    pos_x, pos_y, vel_x, vel_y = map(int, re.findall(r"-?\d+", line))
    robots.append((pos_x, pos_y, vel_x, vel_y,))
results = []


def print_grid(results):
    grid = [[0]*L for _ in range(H)]
    for x, y in results:
        grid[y][x] += 1
    for row in grid:
        print("".join([str(c) if c != 0 else "." for c in row]))

min_factor = float("inf")
best_iteration = None

for s in range(10000):
    quadrants = [0, 0, 0, 0]
    results = []
    for robot in robots:
        posx, posy, velx, vely = robot
        posx = (posx + velx * s) % L
        posy = (posy + vely * s) % H
        results.append((posx, posy,))
        if posx == X_MEDIUM or posy == Y_MEDIUM:
            continue
        elif posx < X_MEDIUM:
            if posy < Y_MEDIUM:
                quadrants[0] += 1
            else:
                quadrants[2] += 1
        else:
            if posy < Y_MEDIUM:
                quadrants[1] += 1
            else:
                quadrants[3] += 1
    safety_factor = quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]
    if safety_factor < min_factor:
        min_factor = safety_factor
        best_iteration = s
        print(s, quadrants)
        print_grid(results)
