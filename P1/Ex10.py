from Seq1 import Seq

file = "../DNA Files/"
extension = ".txt"
dna = ["U5", "ADA", "FRAT1", "FXN", 'RNU6']
bases = ['A', 'T', 'C', 'G']

for i in dna:
    s = Seq().read_fasta(file + i + extension)

    c = s.count()

    ll = [v for v in c.values()]

    m = max(ll)

    print(f'Gene {i}: Most frequent Base: {bases[ll.index(m)]}')
