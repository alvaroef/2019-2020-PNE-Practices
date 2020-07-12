from Seq0 import *


file = "../DNA Files/"
extension = ".txt"
dna = ["U5", "ADA", "FRAT1", "FXN"]
bases = ['A', 'C', 'T', 'G']


gene = dna[0]
print(f"Gene {gene}:")
seq = seq_read_fasta(file + dna[0] + extension)[:20]
comp = seq_complement(seq)
print(f"Frag: {seq}")
print(f"Comp: {comp}")