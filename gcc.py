with open("inputs/rosalind_gc.txt") as f:
    input=f.read().replace('\n',"")

import re
from pprint import pprint

fasta=re.compile(r'>(Rosalind_\d+)([ACGT]+)')

def get_gc(seq):
    gc = 0
    tot = 0
    for c in seq:
        if c in ('G', 'C'):
            gc += 1
            tot += 1
        else:
            tot += 1
    return (gc/tot) * 100

max = 0
max_id = 0
for p in fasta.finditer(input):
    gcc = get_gc(p.group(2))
    if gcc  > max:
        max = gcc
        max_id = p.group(1)

print(max_id)
print(max)
