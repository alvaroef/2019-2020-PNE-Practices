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
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')  # green request line

        req_line = self.requestline.split(' ')  # splits the request line (by the spaces)

        arguments = (req_line[1]).split("?")

        first_argument = arguments[0]  # sets the first argument

        contents = Path('Error.html').read_text()  # no argument --> error form
        self.send_response(404)

        # Main
        try:

            # Index
            if first_argument == "/":  # return an HTML page with the forms for accessing to all the previous services

                contents = Path('index.html').read_text()  # contents displayed in index.html
                self.send_response(200)