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
            # ListSpecies
            elif first_argument == '/listSpecies':
                contents = f"""
                    <!DOCTYPE html> 
                    <html lang = "en">
                    <head>
                     <meta charset = "utf-8" >
                     <title>List of species in the browser</title >
                    </head >
                    <body  style="background-color:rgb(255,204,153)">
                     <h1 style="color:rgb(102, 0, 102);"> List of species in the genome database</h1>
                     <p style="color:rgb(102, 0, 102);"><b>The total number of species in ensembl is: 286</b></p>
                      """
                # now program starts, gets the requested limit and ...

                endpoint = 'info/species'
                params = '?content-type=application/json'
                request = endpoint + params

                try:
                    conn.request("GET", request)  # connection request

                except ConnectionRefusedError:  # exception for connection error
                    print("ERROR! Cannot connect to the Server")
                    exit()

                # Main program

                # -- Read the response message from the server
                response = conn.getresponse()

                # -- Read the response's body
                body = response.read().decode('utf_8')  # utf_8 to admit all characters in the response

                limit_list = []  # list to save all species within the limit
                body = json.loads(body)  # loads is a json method to read json response
                limit = body["species"]  # json.loads(species)

                for element in limit:  # iteration to get all the species within the limit
                    limit_list.append(element["display_name"])  # appends each element to the list

                    if len(limit_list) == 20:
                        contents += f"""<p>The  first 20 species are: </p>"""
                        for specie in limit_list:  # iteration to print all the species in the limit list
                            contents += f"""<p> - {specie} </p>"""
                contents += f"""<a href="/">Main page</a></body></html>"""  # link to return to main page

            # Define the content-type header:
            if 'json=1' in req_line:
                self.send_header('Content-Type', 'application/json')
                self.send_header('Content-Length', len(str.encode(contents)))

            else:
                self.send_header('Content-Type', 'text/html')
                self.send_header('Content-Length', len(str.encode(contents)))

            # The header is finished
            self.end_headers()

            # Send the response message
            self.wfile.write(str.encode(contents))

            return

        except (KeyError, ValueError, IndexError, TypeError):
            contents = Path('error.html').read_text()


# Main program (taken from previous practices)
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()
