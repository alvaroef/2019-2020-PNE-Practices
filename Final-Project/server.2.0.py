import http.server
import socketserver
import termcolor
from pathlib import Path
import json

# Define the Server's port, IP and bases
PORT = 8099
IP = "127.0.0.1"
bases = ['A', 'C', 'T', 'G']

server = 'rest.ensembl.org'  # sever used
parameters = '?content-type=application/json'  # json parameters
conn = http.client.HTTPConnection(server)  # http connection to the server

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
