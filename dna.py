with open("inputs/rosalind_dna.txt") as f:
    input = f.read()
cnt = {}
for c in input:
    if not c in cnt: cnt[c] = 0
    cnt[c] += 1
print(cnt['A'], cnt['C'],cnt['G'],cnt['T'])
