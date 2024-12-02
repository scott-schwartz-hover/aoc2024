from typing import Counter
from utils import read_file

data = read_file('01')

pairs = [int(s) for pair in data for s in pair.split('  ')]

left, right = sorted(pairs[::2]), sorted(pairs[1::2])

# Part 1
print(sum([abs(l - r) for l, r in zip(left, right)]))

# Part 2
print(sum([id * Counter(right)[id] for id in left]))
