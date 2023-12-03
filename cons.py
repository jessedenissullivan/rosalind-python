from Bio.SeqIO.FastaIO import SimpleFastaParser
from pprint import pprint
from sys import argv
def mk_consensus(samples_path):
    with open(samples_path) as f:
        samples = [ sample for sample in SimpleFastaParser(f) ]
    length = len(samples[0][1])
    bases = ['A', 'T', 'C', 'G']
    matrix = { b : [0]*length for b in bases }
    consensus = { i : { b : 0 for b in bases } for i in range(length) }
    for sample in samples:
        for i in range(length):
            b = sample[1][i]
            matrix[b][i] += 1
            consensus[i][b] += 1

    consensus_string = ''.join(
        max(bs.items(), key=lambda x: x[1])[0] for (p, bs) in consensus.items()
    )
    matrix_string = '\n'.join(
        '{}: {}'.format(
            k,
            ' '.join(map(str, v))
        ) for (k,v) in matrix.items()
    )
    print(consensus_string)
    print(matrix_string)

if __name__ == "__main__":
    assert len(argv) == 2, "USAGE: python cons.py <path to samples>"
    samples_path = argv[1]
    mk_consensus(samples_path)