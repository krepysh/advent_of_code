disk_map = open(0).read().strip()
# disk_map = "2333133121414131402"

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


def compress(fs, fragment_files=True):
    if fragment_files:
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
    return fs

check_sum = 0
print(sum(int(x) * i if x != "." else 0 for i, x in enumerate(compress(fs))))


# part 2
file_id = 0
start = 0

files = {}
blanks = []

for pos in range(len(disk_map)):
    is_file = pos % 2 != 1
    len_blocks = int(disk_map[pos])
    if is_file:
        files[file_id] = [start, len_blocks]
        max_file_id = file_id
        file_id += 1
    else:
        if len_blocks > 0:
            blanks.append([start, len_blocks])
    start += len_blocks

while file_id > 0:
    file_id -= 1
    for i, blank in enumerate(blanks):
        if files[file_id][0] < blank[0]:
            break
        if files[file_id][1] <= blank[1]:
            files[file_id][0] = blank[0]
            blank[0] = blank[0] + files[file_id][1]
            blank[1] = blank[1] - files[file_id][1]
            break

res = 0
for file_id, (start, num_blocks) in files.items():
    for i in range(num_blocks):
        res += file_id * (start + i)
print(res)