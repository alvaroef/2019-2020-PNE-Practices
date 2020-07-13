from Client0 import Client
from Seq1 import Seq


# -- Parameters of the server to talk to
ip = "127.0.0.1"
port = 8080

file = "../DNA Files/"
extension = ".txt"
dna = 'FRAT1'

# -- Create a client object
c1 = Client(ip, port)
c2 = Client(ip, port+1)
# -- Print the IP and PORTs
print(c1)
print(c2)
# -- Read the Gene from a file
s = Seq().read_fasta(file + dna + extension)

bases = str(s)

# -- Print the Gene on the console
print(f"Gene {dna}: {bases}")

length = 10

c1.talk(f"Sending {dna} Gene to the server, in fragments of {length} bases...")
c1.talk(f"Sending {dna} Gene to the server, in fragments of {length} bases...")

for i in range(10):

    frag = bases[i*length:(i+1)*length]

    print(f"Fragment {i+1}: {frag}")

    msg = f"Fragment {i+1}: {frag}"

    if i % 2:
        c2.talk(msg)
    else:
        c1.talk(msg)
