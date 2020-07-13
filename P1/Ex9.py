from Seq1 import Seq

file = "../DNA Files/"
extension = ".txt"
dna = ["U5", "ADA", "FRAT1", "FXN", 'RNU6']

s = Seq()

s.read_fasta(file + dna[0] + extension)

print(f'Seq: {s} (Length: {s.len()})')
print(f' Bases: {s.count()}')
print(f'Reverse: {s.reverse()}')
print(f' Comp: {s.complement()}')
