from Seq0 import *


file = "../DNA Files/"
extension = ".txt"
dna = ["U5", "ADA", "FRAT1", "FXN"]
bases = ['A', 'C', 'T', 'G']


for gene in dna:
    seq = seq_read_fasta(file + gene + extension)

    # -- Dictionary with the values
    d = seq_count(seq)

    # -- Create a list with all the values
    ll = [v for v in d.values()]

    # -- Calculate the maximum
    m = max(ll)

    # -- Print the base
    print(f"Gene {gene}: Most frequent Base: {bases[ll.index(m)]}")