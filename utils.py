from pathlib import Path


def read_file(name, *, do_strip=True):
    path = Path(f'/Users/scott.schwartz/code/aoc2024/inputs')
    if isinstance(name, int):
        name = f'{name:02d}'
    with open(path / name) as f:
        res = f.readlines()
    if do_strip:
        res = list(map(str.strip, res))
    return res
