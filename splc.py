from Bio import SeqIO
from Bio.Seq import Seq
def splice(path):
    with open(path) as f:
        seqs = [asc for asc in SeqIO.parse(f,'fasta')]
    seq = str(seqs[0].seq)
    introns = [str(s.seq) for s in seqs[1:]]
    for i in introns:
        seq = seq.replace(i, "")
    print(Seq(seq).translate().strip("*"))


if __name__=="__main__":
    input = "inputs/rosalind_splc.txt"
    splice(input)