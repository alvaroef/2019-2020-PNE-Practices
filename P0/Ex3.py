from Seq0 import *


file = "../DNA Files/"
extension = ".txt"
dna = ["U5", "ADA", "FRAT1", "FXN"]

# The program goes around all components of the 'dna' list and prints the length of the codon
for gene in dna:
    seq = seq_read_fasta(file + gene + extension)
    print(f"Gene {gene} ---> Length: {seq_len(seq)}")