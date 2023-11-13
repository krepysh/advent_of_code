from advent import read_input

lines = read_input('day15.txt')

exclusion_zones = []


def extract_coord(s: str):
    cords = s.split(' at ')[1]
    x, y = cords.split(', ')
    x = int(x.split('=')[1])
    y = int(y.split('=')[1])
    return x, y


def manhattan_distance(sensor_pos, beacon_pos):
    return abs(sensor_pos[0] - beacon_pos[0]) + abs(sensor_pos[1] - beacon_pos[1])


for line in lines:
    sensor_part, beacon_part = line.split(':')
    sensor_pos = extract_coord(sensor_part)
    beacon_pos = extract_coord(beacon_part)
    distance = manhattan_distance(sensor_pos, beacon_pos)
    exclusion_zones.append((sensor_pos, distance))

line_y = 11

busy = []
for center, distance in exclusion_zones:
    dist_to_line = abs(center[1] - line_y)
    half_width = distance - dist_to_line
    if half_width < 0:
        # any of points on line is in exclusion zone
        continue
    busy.append((center[0] - half_width, center[0] + half_width))


def merge_intervals(busy):
    sorted_intervals = sorted(busy)
    merged = [sorted_intervals[0]]
    for i in range(1, len(sorted_intervals)):
        current_start, current_end = merged[-1]
        if current_end >= sorted_intervals[i][0]:
            merged[-1] = (current_start, max(current_end, sorted_intervals[i][1]))
        else:
            merged.append(sorted_intervals[i])
    print(sorted_intervals)
    print(merged)
    return merged


busy = merge_intervals(busy)
res = sum([i[1] - i[0] for i in busy])
print(res)


# part 2
def l2(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2) ** (1/2)


for i in range(len(exclusion_zones)):
    for j in range(i + 1, len(exclusion_zones)):
        z1_center, z1_distance = exclusion_zones[i]
        z2_center, z2_distance = exclusion_zones[j]
        d = manhattan_distance(z2_center, z1_center)
        if d - z1_distance - z2_distance == 2:
            ratio = l2(z1_center, (0, 0)) / l2(z1_center, z2_center)
            print(z1_center[0] + (z1_center[0] - z2_center[0])*ratio, z1_center[1] + (z1_center[1] - z2_center[1]) * ratio)