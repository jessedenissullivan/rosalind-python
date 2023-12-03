import re
input="CCGAGAATTCTTTCAAGAGAATTCGGAGAATTTCAAGAGAATTAGCAGAGAATTAGGAGAATTGAGAATTGAGGAGAATTGGAGAATTCGAGAATTACCTGAGAATTGAGAATTGCGAGAATTCAATACATGAGAATTAGAGAATTAAGAGAATTGTGAGAATTCTGAGAGAATTTTCGAGAATTGAGAATTACTGGGAGAATTCGGAGAATTGAGAATTGATGAGAATTAGAGAATTGATGGGAGAATTTCTGAGAATTGAGAATTTGGAGAATTTAATGTATAGAGAATTCATAGAGAATTGAGAATTGAGAATTGAGAATTGGTGAGAATTAGAGAATTGAGAATTGAGAGAATTTATGTAGACCATGAGAATTGAGAATTGTGTCCTTTGAGAATTAAAGAGAATTGAGAATTTCGCGGAGAATTGAGAATTGGAGAATTAAGAGAATTTGAGAATTGGAGAATTCCTGGCTACAGCGGGAGAATTTATGAGAATTGAGAATTGAGAATTCGCTTTATAAGGGAGAATTGAGAATTCCGAAGGAGAATTAGCCCAGAGAATTTAGTGGGGAGAATTACTCTCTTGAGAATTGGAGAATTGAGAATTGGAGAATTTTGAGCGAGAGAATTGACGAGAATTGGAGAATTGAGAGAATTCGACTCGGTGAGAATTGGGAGAATTGGAACCGAGAATTCCCGGGAGAATTGAGAATTGAGAATTGAGAATTTATCAGAGAATTTGAGAATTCTGAGAATTGAGAATTCGGAGAATTACGAGAATTGAGAATTCTCGAGAATTGGAGAATTATTTACGAGAATTTGGGAGAATTTGAGAATTGAGAGAATTGAGAATTCAGTGTGAGAATTTGGAGAATTGTTCTCGCTCCATGAGAATTGAGAATTTATGAGAATTGAGAATT"
patt=re.compile(r"(?=GAGAATTGA)")
for i in patt.finditer(input):
    print(i.span()[0]+1, end=" ")
print()