from Seq0 import *


file = "../DNA Files/"
extension = ".txt"
dna = ["U5", "ADA", "FRAT1", "FXN"]
bases = ['A', 'C', 'T', 'G']


for gene in dna:
    seq = seq_read_fasta(file + gene + extension)
    print(f"Gene {gene}: {seq_count(seq)}")