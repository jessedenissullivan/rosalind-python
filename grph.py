from Bio.SeqIO.FastaIO import SimpleFastaParser
from Bio import SeqIO
from Bio.Pathway.Rep.Graph import Graph
from itertools import product
from pprint import pprint
from graphviz import Digraph
from sys import argv

def prefix(s, k):
    return str(s.seq)[:k]
def suffix(s, k):
    return str(s.seq)[-k:]

def mk_overlap_graph(samples_path, k=3):
    with open(samples_path) as f:
        samples = list(SeqIO.parse(f, 'fasta'))
    g = Graph()
    for (s, t) in product(samples, samples):
        f.write(f"{s.id} {t.id}\n")
        try: g.add_node(s.id)
        except: pass
        try: g.add_node(t.id)
        except: pass
        if suffix(s, k) == prefix(t, k) and s.id != t.id:
            g.add_edge(s.id, t.id)
    with open("answer.txt", "w") as f:
        f.write(
            '\n'.join(
                f"{source} {target}"
                for (source, target) in g.edges(None)
            ) 
        )

if __name__ == "__main__":
    # assert len(argv) == 2, f"USAGE: python3.12 {argv[0]} <path to samples>"
    # samples_path = argv[1]
    samples_path = "inputs/rosalind_grph.txt"
    mk_overlap_graph(samples_path)