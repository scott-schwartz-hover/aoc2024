from utils import read_file

data = read_file("02")


def format_row(row):
    return list(map(int, row.split(" ")))


def is_safe(row):
    cur, *rest = row
    increasing = cur < rest[0]
    for n in rest:
        if increasing and n < cur:
            return False
        if not increasing and n > cur:
            return False
        if n == cur:
            return False
        diff = abs(cur - n)
        if diff > 3:
            return False
        cur = n
    return True


reports = list(map(format_row, data))


def p1():
    return sum([1 if is_safe(row) else 0 for row in reports])


# Brute force
def p2():
    res = 0
    for row in reports:
        lists_missing_one = [row[:i] + row[i + 1 :] for i in range(len(row))]
        for l in lists_missing_one:
            if is_safe(l):
                res += 1
                break
    return res


print(p1(), p2())
