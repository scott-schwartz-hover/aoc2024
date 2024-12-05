import re
from utils import read_file

matrix = [list(row) for row in read_file("04")]

def count_row(row):
    pattern = r"(?=(XMAS|SAMX))"
    matches = re.findall(pattern, ''.join(row))
    return len(matches)


# # Part 1
def p1():
    total = 0
    rows, cols = len(matrix), len(matrix[0])
    # rows
    total += sum([count_row(row) for row in matrix])
    # columns
    columns = [col for col in zip(*matrix)]
    total += sum([count_row(column) for column in columns])
    # diagonals
    diagonals = []
    # top left -> bottom right
    for row in range(rows - 3):
      for col in range(cols - 3):
        diagonals.append([matrix[row + i][col + i] for i in range(4)])
    # top right -> bottom left
    for row in range(rows - 3):
      for col in range(3, cols):
        diagonals.append([matrix[row + i][col - i] for i in range(4)])
    total += sum([count_row(diagonal) for diagonal in diagonals])
    return total


print(p1())
