disk_map = open(0).read().strip()

file_id = 0
fs = []
for pos in range(len(disk_map)):
    is_file = pos % 2 != 1
    len_blocks = int(disk_map[pos])
    for i in range(len_blocks):
        char = file_id if is_file else "."
        fs.append(char)
    if is_file:
        file_id += 1

head = 0
tail = len(fs) - 1
while tail - head > 0:
    if fs[head] != ".":
        head += 1
        continue
    elif fs[tail] == ".":
        tail -= 1
        continue
    else:
        fs[head], fs[tail] = fs[tail], fs[head]
        head += 1
        tail -= 1
check_sum = 0


print(sum(int(x) * i if x != "." else 0 for i, x in enumerate(fs)))
