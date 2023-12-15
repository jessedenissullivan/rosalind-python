from codons import mk_rev_trans_map
import sys

def calc_num_possible_rna(protein):
    m = mk_rev_trans_map()
    ret = 1
    for p in protein:
        ret *= len(m[p])
    ret *= len(m['Stop'])
    return ret % 1000000

if __name__=="__main__":
    a = open("answers/rosalind_mrna.txt", "w")
    sys.stdout = a
    with open("inputs/rosalind_mrna.txt") as f:
        protein = f.read().strip()
    print(calc_num_possible_rna(protein))
    a.close()