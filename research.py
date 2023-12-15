from Bio.Data.CodonTable import standard_dna_table
from Bio import SeqIO
from pprint import pprint
import re
rev_tbl = {}
for (k,v) in standard_dna_table.forward_table.items():
    if v in rev_tbl:
        rev_tbl[v].add(k)
    else:
        rev_tbl[v] = set([k])

with open("inputs/rosalind_orf.txt") as f:
    acs = SeqIO.read(f, 'fasta')
targ = "MLLGSFRLIPKETLIQVAGSSPCNLS"
patt = "".join(map(lambda x: f'({"|".join(rev_tbl[x])})', targ))
matcher = re.compile(patt)
pprint(patt)
print((str(acs.seq)))
print((str(acs.seq.reverse_complement())))
pprint(matcher.search(str(acs.seq)))
pprint(matcher.search(str(acs.seq.reverse_complement())))
