from Seq1 import Seq

s_1 = Seq()
s_2 = Seq('ACTGA')
s_3 = Seq('Nonsense')

for i, j in enumerate([s_1, s_2, s_3]):
    print(f'Seq {i+1}: {j} (Length: {j.len()})')
    for b in ['A', 'C', 'T', 'G']:
        print(f' {b}: {j.count_base(b)}')
