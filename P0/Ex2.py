from Seq0 import *


dna = "U5.txt"
file = "../DNA Files/" + dna


seq = seq_read_fasta(file)
print(f"DNA file: {dna}")
print(f"The first bases are: {seq[:20]}")