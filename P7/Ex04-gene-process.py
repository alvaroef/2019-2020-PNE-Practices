import termcolor
import json
import http.client
from Seq1 import Seq


genes = {
    'FRAT1': 'ENSG00000165879',
    'ADA': 'ENSG00000196839',
    'FXN': 'ENSG00000165060',
    'RNU6_269P': 'ENSG00000212379',
    'MIR633': 'ENSG00000207552',
    'TTTY4C': 'ENSG00000228296',
    'RBMY2YP': 'ENSG00000227633',
    'FGFR3': 'ENSG00000068078',
    'KDR': 'ENSG00000128052',
    'ANK2': 'ENSG00000145362',
}

bases = ['A', 'C', 'T', 'G']

server = 'rest.ensembl.org'
end_p = '/sequence/id/'
params = '?content-type=application/json'

name = input('Choose a gene:')

request = end_p + genes[name] + params
url = server + request

conn = http.client.HTTPConnection(server)

try:
    conn.request("GET", request)

except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

# -- Read the response message from the server
r1 = conn.getresponse()

# -- Print the status line
print(f"Response received!: {r1.status} {r1.reason}\n")

# -- Read the response's body
data1 = r1.read().decode()

# -- Create a variable with the data,
# -- form the JSON received
gene = json.loads(data1)

termcolor.cprint("Gene", 'green', end="")
print(f": {name}")
termcolor.cprint("Description", 'green', end="")
print(f": {gene['desc']}")

gene_str = gene['seq']

# -- Create the object sequence from the string
s = Seq(gene_str)

s_len = s.len()
count_a = s.count_base('A')
per_a = "{:.1f}".format(100 * count_a / s_len)
count_c = s.count_base('C')
per_c = "{:.1f}".format(100 * count_c / s_len)
count_g = s.count_base('G')
per_g = "{:.1f}".format(100 * count_g / s_len)
count_t = s.count_base('T')
per_t = "{:.1f}".format(100 * count_t / s_len)

termcolor.cprint("Total length", 'green', end="")
print(f": {s_len}")

termcolor.cprint("A", 'blue', end="")
print(f": {count_a} ({per_a}%)")
termcolor.cprint("C", 'blue', end="")
print(f": {count_c} ({per_c}%)")
termcolor.cprint("G", 'blue', end="")
print(f": {count_g} ({per_g}%)")
termcolor.cprint("T", 'blue', end="")
print(f": {count_t} ({per_t}%)")

# -- Dictionary with the values
d = s.count()

# -- Create a list with all the values
ll = list(d.values())

# -- Calculate the maximum
m = max(ll)

# -- Print the base
termcolor.cprint("Most frequent Base", 'green', end="")
print(f": {bases[ll.index(m)]}")
