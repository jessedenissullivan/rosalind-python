from Bio import SeqIO
from Bio.Data.CodonTable import standard_dna_table
import re, sys
from pprint import pprint
start_codon = "ATG"
stop_codons = ("TGA", "TAG", "TAA")
map_acid = {

}
def get_potential_proteins(path):
    candiate_proteins = set([])
    with open(path) as f:
        acs = SeqIO.read(f, 'fasta')
    for (strand, orientation) in [(acs.seq, "forward"), (acs.seq.reverse_complement(), "rev")]:
        for fr in range(0,3):
            candiate_proteins.update(find_proteins(strand[fr:], orientation, fr))
            
    return candiate_proteins

def find_proteins(asc, orientation, frame):
    ret = set()
    seq = str(asc)
    for start in re.finditer(start_codon, seq):
        for codon in re.finditer(r"\w{3}", seq[start.start():]):
            if codon.group() in stop_codons:
                candidate = asc[start.start():start.start()+codon.end()]
                candidate = candidate[:(len(candidate)//3)*3]
                assert len(candidate) % 3 == 0, f"Candidate is not a multiple of 3: {len(candidate)} % 3 == {len(candidate) % 3}"
                protein = candidate.translate().strip("*")
                print(f"({orientation}, {frame}): {protein} >= {candidate}")
                if candidate == "": breakpoint()
                ret.add(protein)
                break
    return ret

if __name__=="__main__":
    path = "inputs/rosalind_orf.txt"
    answers = "answers/rosalind_orf.txt"
    f = open(answers, "w")
    # sys.stdout = f
    proteins = set()
    for protein in get_potential_proteins(path):
        proteins.add(protein)
    print("-"*80)
    for p in proteins:
        print(p)
        pass
    f.close()