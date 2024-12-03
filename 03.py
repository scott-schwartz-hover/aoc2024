from operator import mul
import re
from utils import read_file


data = "".join(read_file("03"))


def p1():
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    matches = re.findall(pattern, data)
    return sum(eval(match) for match in matches)


def p2():
    pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)"
    matches = re.findall(pattern, data)
    enabled = True
    s = 0
    for match in matches:
        if match == "do()":
            enabled = True
        elif match == "don't()":
            enabled = False
        elif enabled:
            res = eval(match)
            s = sum((s, res))
    return s


print(p1())
print(p2())
