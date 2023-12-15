from Bio import SeqIO
from Bio.Seq import Seq
import sys
def find_restriction_sites(seq):
    ret = set()
    strand = seq.seq
    for start in range(len(strand)):
        for size in range(4,12+1):
            candidate = strand[start:start+size]
            if candidate == candidate.reverse_complement():
                ret.add((start+1, len(candidate)))
    return ret


if __name__=="__main__":
    path = "inputs/rosalind_revp.txt"
    with open("answers/rosalind_revp.txt", "w") as f:
        sys.stdout = f
        with open(path) as f:
            seq = SeqIO.read(f,'fasta')
        for (start, length) in sorted(find_restriction_sites(seq), key=lambda x: x[0]):
            if length >= 4 and length <= 12:
                print(start, length, sep="\t")