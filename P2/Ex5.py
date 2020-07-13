from Client0 import Client
from Seq1 import Seq


# -- Parameters of the server to talk to
ip = "127.0.0.1"
port = 8080

file = "../DNA Files/"
extension = ".txt"
dna = 'U5'

# -- Create a client object
c = Client(ip, port)

# -- Print the IP and PORTs
print(c)

# -- Read the Gene from a file
s = Seq().read_fasta(file + dna + extension)

# -- Send the Gene
c.debug_talk(f"Sending {dna} Gene to the server...")
c.debug_talk(str(s))
