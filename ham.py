with open('inputs/rosalind_ham.txt') as f:
    lines = f.readlines()

dist = 0
for (c1, c2) in zip(lines[0], lines[1]):
    if c1 != c2: dist += 1

print(dist)