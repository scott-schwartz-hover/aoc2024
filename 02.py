from utils import read_file

data = read_file("02")


def format_row(row):
    return list(map(int, row.split(" ")))


reports = list(map(format_row, data))


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


def lists_missing_one(row):
    return [row[:i] + row[i + 1 :] for i in range(len(row))]


def p1():
    return sum([1 if is_safe(row) else 0 for row in reports])


# Brute force
def p2():
    return sum(
        [1 if any(is_safe(l) for l in lists_missing_one(row)) else 0 for row in reports]
    )


print(p1(), p2())
