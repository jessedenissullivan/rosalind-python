from sys import argv
from Bio import SeqIO
def generate_substrings(s):
    length = len(s)
    for size in range(length, 0, -1):
        for start in range(length - size + 1):
            yield str(s.seq)[start:start+size]
def lcsm(fasta_path):
    with open(fasta_path) as f:
        samples = list(SeqIO.parse(f, 'fasta'))
    sample = samples[0]
    for ss in generate_substrings(sample):
        if all([ss in str(s.seq) for s in samples[1:]]):
            return ss
        
if __name__=="__main__":
    print(lcsm(argv[1]))