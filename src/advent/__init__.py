def read_input(fname: str, by_group=False) -> list[str]:
    filename = fname
    with open(filename, 'r') as f:
        lines = f.readlines()
    lines = [l.strip() for l in lines]
    if by_group:
        rv = [[]]
        for line in lines:
            if not line:
                rv.append([])
            else:
                rv[-1].append(line)
        lines = rv
    return lines
