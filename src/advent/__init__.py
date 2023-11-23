from typing import Callable, Optional


def read_input(fname: str, by_group=False, convert_to: Optional[Callable] = None) -> list[str]:
    def convert(some):
        return convert_to(some) if convert_to else some
    filename = fname
    with open(filename, 'r') as f:
        lines = f.readlines()
    lines = [convert(l.strip()) for l in lines]
    if by_group:
        rv = [[]]
        for line in lines:
            if not line:
                rv.append([])
            else:
                rv[-1].append(line)
        lines = rv
    return lines
