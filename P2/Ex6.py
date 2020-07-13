from Client0 import Client
from Seq1 import Seq


# -- Parameters of the server to talk to
ip = "127.0.0.1"
port = 8080

file = "../DNA Files/"
extension = ".txt"
dna = 'FRAT1'

# -- Create a client object
c = Client(ip, port)

# -- Print the IP and PORTs
print(c)

# -- Read the Gene from a file
s = Seq().read_fasta(file + dna + extension)

# -- Send the Gene
c.debug_talk(f"Sending {dna} Gene to the server...")
c.debug_talk(str(s))

bases = str(s)

# -- Print the Gene on the console
print(f"Gene {dna}: {bases}")

length = 10

c.talk(f"Sending {dna} Gene to the server, in fragments of {length} bases...")

for i in range(5):

    frag = bases[i*length:(i+1)*length]

    print(f"Fragment {i+1}: {frag}")

    c.talk(f"Fragment {i+1}: {frag}")
