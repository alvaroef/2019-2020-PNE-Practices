import http.client
import json

server = 'rest.ensembl.org'
end_p = '/info/ping'
params = '?content-type=application/json'
url = server + end_p + params

print()
print(f"Server: {server}")
print(f"URL: {url}")

# Connect with the server
conn = http.client.HTTPConnection(server)

try:
    conn.request("GET", end_p + params)

except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

# -- Read the response message from the server
r1 = conn.getresponse()

# -- Print the status line
print(f"Response received!: {r1.status} {r1.reason}\n")

# -- Read the response's body
data1 = r1.read().decode()

response = json.loads(data1)

ping = response['ping']

if ping == 1:
    print("PING OK! The database is running!")