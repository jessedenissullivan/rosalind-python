map = {
    "A" : 'A',
    "T" : 'U',
    "G" : 'G',
    "C" : 'C',
}
with open("inputs/rosalind_rna.txt") as f:
    input = f.read()
print("".join([map[x] for x in input if x in map]))