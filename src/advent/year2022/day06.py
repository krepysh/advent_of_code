def read_input():
    filename = 'day06.txt'
    with open(filename, 'r') as f:
        lines = f.readlines()
    lines = [l.strip() for l in lines]
    return lines


def is_start_of_packet_marker(w):
    for symb in w:
        if w.count(symb) != 1:
            return False
    return True

buffer = read_input()[0]

pos = 0
len_needed = 14
while pos < len(buffer):
    window = buffer[pos:pos + len_needed]
    for symb in window:
        if window.count(symb) != 1:
            pos += window.index(symb) + 1
            break
    if is_start_of_packet_marker(window):
        break
print(pos + len_needed)
