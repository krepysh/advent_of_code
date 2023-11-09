def read_input(fname: str) -> list[str]:
    filename = fname
    with open(filename, 'r') as f:
        lines = f.readlines()
    lines = [l.strip() for l in lines]
    return lines
