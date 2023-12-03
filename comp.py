map = {
    "A" : 'T',
    "T" : 'A',
    "G" : 'C',
    "C" : 'G',
}
with open("inputs/rosalind_revc.txt") as f:
    input = f.read()
input="AAAACCCGGT"
print("".join([map[x] for x in reversed(input) if x in map]))