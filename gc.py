input=""">Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT""".replace('\n',"")

import re

fasta=re.compile(r'>Rosalind_(\d+)([ACGT]+)')

def get_gc(seq):
    gc = 0
    tot = 0
    for c in seq:
        if c in ('G', 'C'):
            gc += 1
            tot += 1
        else:
            tot += 1
    return gc/tot
gc_content = { p.groups(1) : get_gc(p.groups(2))
    for p in fasta.finditer(input)
}
print(gc_content)