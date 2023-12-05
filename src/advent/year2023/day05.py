import re

from advent import read_input


def extract_list_int(s):
    if isinstance(s, list):
        s = s[0]
    return list(map(int, re.findall('\d+', s)))


def apply_map(value: int, current_map: list[tuple[int, int, int]]):
    for dst_start, src_start, range_len in current_map:
        if src_start <= value < src_start + range_len:
            return dst_start + (value - src_start)
    return value


def apply_map_to_collection(seeds: list[int], current_map: list[tuple[int, int, int]]):
    rv = []
    for value in seeds:
        rv.append(apply_map(value, current_map))
    return rv


def apply_map_to_intervals(intervals_seeds: list[tuple[int, int]], current_map: list[tuple[int, int, int]]):
    rv = []
    map_dst_start, map_src_start, range_len = current_map
    for int_start, int_end in intervals_seeds:
        intersection_begin = max(int_start, map_src_start)
        intersection_end = min(int_end, map_src_start + range_len)
        if intersection_end > intersection_begin:
            rv.append((intersection_begin, intersection_end))


seeds, *raw_maps = read_input('day05.txt', by_group=True)
maps = []
for r_map in raw_maps:
    current_map = []
    for triplet in r_map[1::]:
        map_values = extract_list_int(triplet)
        trio_int = (map_values[0], map_values[1], map_values[2])  # ensure that all tuples are 3-length
        current_map.append(trio_int)
    maps.append(current_map)
seeds = extract_list_int(seeds)

intervals_seeds = []
for i in range(0, len(seeds), 2):
    intervals_seeds.append((seeds[i], seeds[i] + seeds[i+1]))
print(intervals_seeds)




for current_map in maps:
    seeds = apply_map_to_collection(seeds, current_map)
    intervals_seeds = apply_map_to_intervals(intervals_seeds, current_map)

print(min(seeds))
