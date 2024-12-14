import re

robots = []
STEPS = 100
H = 103
L = 101
quadrants = [0, 0, 0, 0]
for line in open(0).readlines():
    pos_x, pos_y, vel_x, vel_y = map(int, re.findall(r"-?\d+", line))
    robots.append((pos_x, pos_y, vel_x, vel_y,))
results = []
for robot in robots:
    posx, posy, velx, vely = robot
    posx = (posx + velx * STEPS) % L
    posy = (posy + vely * STEPS) % H
    results.append((posx, posy,))

X_MEDIUM = (L - 1) // 2
Y_MEDIUM = (H - 1) // 2
print(X_MEDIUM, Y_MEDIUM)
for posx, posy in results:
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

print(quadrants)
r = 1
for q in quadrants:
    r = q * r
print(r)