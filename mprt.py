from Bio import ExPASy, SeqIO
import requests, re, sys

def mk_regex(motif):
    return motif.replace("{", "[^")\
                .replace("}", "]")

def test_motif(id, seq, motif):
    patt = mk_regex(motif)
    pos = " ".join(str(match.span()[0]+1) for match in re.finditer(f"(?=({patt}))", seq))
    if pos != "":
        print(id)
        print(pos)

def get_prot(uniprot_id):
    id = uniprot_id.split("_")[0]
    url = f"http://www.uniprot.org/uniprot/{id}.fasta"
    resp = requests.get(url)
    resp.raise_for_status()
    with open(f"seqs/{uniprot_id}.fasta", "w") as f:
        f.write(str(resp.content, "utf-8"))

def test_fasta(uniprot_id, motif):
    get_prot(uniprot_id)
    with open(f"seqs/{uniprot_id}.fasta") as handle:
        seq_record = SeqIO.read(handle, "fasta")
        test_motif(uniprot_id,
                   str(seq_record.seq), 
                   motif)
    return seq_record

if __name__=="__main__":
    f = open("answers/rosalind_mprt.txt", "w")
    sys.stdout = f
    motif = "N{P}[ST]{P}"
    with open("inputs/rosalind_mprt.txt") as f:
        for uniprot_id in f:
            seq_record = test_fasta(uniprot_id.strip(), motif)
    f.close()