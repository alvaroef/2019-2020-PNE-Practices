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
        global full_name
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
                        contents += f"""<p>The species are: </p>"""
                        for specie in limit_list:  # iteration to print all the species in the limit list
                            contents += f"""<p> - {specie} </p>"""
                contents += f"""<a href="/">Main page</a></body></html>"""  # link to return to main page

            # Karyotype
            elif first_argument == '/karyotype':  # part3, returns the names of the cromosomes of the chosen species

                contents = f"""<!DOCTYPE html>
                                            <html lang = "en">
                                            <head>
                                                <meta charset = "utf-8">
                                                 <title> Karyotype </title >
                                            </head >
                                            <body  style="background-color:rgb(255,204,153)">
                                            """

                try:
                    # Get the arguments after the ?
                    get_value = arguments[1]

                    # We get the seq index and name
                    specie = get_value.split('?')  # splits by the ?
                    specie_method, name_sp = specie[0].split("=")  # splits by the =

                    full_name = ""  # we initialize the variable to keep doble or more word names
                    for n in range(0, len(name_sp)):
                        if name_sp[n] == "+":
                            full_name += "%20"
                        else:
                            full_name += name_sp[n]  # in case its a one word species
                    if full_name == 'human' or full_name == 'cat' or full_name == 'mouse':
                        endpoint = 'info/assembly/'
                        params = '?content-type=application/json'
                        request = endpoint + full_name + params

                        try:
                            conn.request("GET", request)  # connection request

                        except ConnectionRefusedError:  # exception for connection error
                            print("ERROR! Cannot connect to the Server")
                            exit()

                        # Main program of karyotype
                        response = conn.getresponse()

                        # -- Read the response's body
                        body = response.read().decode("utf-8")  # utf_8 to admit all characters in the response
                        body = json.loads(body)  # loads is a json method to read json response
                        karyotype_data = body["karyotype"]  # list to save all the names

                        full_name = full_name.replace("%20", " ")
                        contents += f"""<h2 style="color:rgb(102, 0, 102);"> 
                                                The names of the {full_name} chromosomes are:</h2> """

                        for chromosome in karyotype_data:  # iteration to print all the chromosomes names
                            contents += f"""<p> - {chromosome} </p>"""

                        contents += f"""<a href="/">Main page </a></body></html>"""  # link to return to main page
                    else:
                        contents = f"""
                            <!DOCTYPE html> 
                            <html lang="en"> 
                                <head>
                                    <meta charset="UTF-8">
                                    <title>Error</title>
                                </head>
                                <body style="background-color:rgb(255,204,153)">
                                    <h1>ERROR</h1>
                                    <h2>'{full_name}' not found</h2>
                                    <p> Selected specie's {full_name} karyotype information is not available </p>
                                    <p><a href="/karyotype?Specie={full_name}">
                                    Check if your specie is in our database</a><br><br>
                                    <p> Introduce a specie in the database to find its karyotype </p>
                                    <a href="/"> Main page </a> </p>
                                    </body>
                                    </html>"""

                except KeyError:  # exception in case no value or an incorrect format value is inputed
                    contents = f"""
                                    <!DOCTYPE html> 
                                    <html lang="en"> 
                                        <head>
                                            <meta charset="UTF-8">
                                            <title>Error</title>
                                        </head>
                                        <body style="background-color:rgb(255,204,153)">
                                            <h1>ERROR</h1>
                                            <p> Selected specie's karyotype information is not available </p>
                                            <p><a href="/karyotype?Specie={full_name}">
                                            Check if your specie is in our database</a><br><br>
                                            <p> Introduce a specie in the database to find its karyotype </p>
                                            <a href="/"> Main page </a> </p>
                                            </body>
                                            </html>"""
            # Chromosome length

            elif first_argument == "/chromosomeLength":

                try:
                    # We get the arguments that go after the ?, it will get us the SPECIE&CHROMOSOME
                    pair = arguments[1]

                    # We have to separate both the species name and the chromo index inputed
                    pairs = pair.split('&')  # splits by the &
                    specie_name, specie = pairs[0].split("=")  # having pair[0] as the species name

                    chromosome_index, chromosome = pairs[1].split("=")  # having pair[1] as the species name

                    # html form for when no chromosome index is inputed
                    contents = f"""<!DOCTYPE html>
                                        <html lang = "en">
                                        <head>
                                         <meta charset = "utf-8" >
                                         <title>ERROR</title >
                                        </head>
                                        <body  style="background-color:rgb(255,204,153)">
                                        <p>ERROR INVALID VALUE</p>
                                        <p> Introduce a valid integer value for chromosome of this species</p>
                                        <a href="/">Main page</a></body></html>"""

                    full_name = ""  # we initialize the variable to keep doble or more word names
                    for n in range(0, len(specie)):
                        if specie[n] == "+":
                            full_name += "%20"
                        else:
                            full_name += specie[n]  # in case its a one word species
                    if full_name == 'human' or full_name == 'cat' or full_name == 'mouse':
                        endpoint = 'info/assembly/'
                        params = '?content-type=application/json'
                        request = endpoint + full_name + params

                        try:
                            conn.request("GET", request)  # connection request
                        except ConnectionRefusedError:  # exception for connection error
                            print("ERROR! Cannot connect to the Server")
                            exit()

                        # Main program
                        response = conn.getresponse()

                        # -- Read the response's body
                        body = response.read().decode('utf-8')  # utf_8 to admit all characters in the response
                        body = json.loads(body)  # loads is a json method to read json response

                        chromosome_data = body["top_level_region"]  # list to save all the chromosomes
                        specie = specie.replace("+", " ")

                        for chromosomes in chromosome_data:
                            if chromosomes["name"] == str(chromosome):
                                length = chromosomes["length"]
                                contents = f"""<!DOCTYPE html>
                                                <html lang = "en"><head>
                                                <meta charset = "utf-8" >
                                                <title> Length Chromosome</title >
                                                </head ><body  style="background-color:rgb(255,204,153)">
                                                <h2 style="color:rgb(102, 0, 102);"> 
                                                The length of the '{chromosome}' {specie} chromosome is: {length}</h2>
                                                <a href="/"> Main page</a"""
                    else:
                        contents = f"""
                                <!DOCTYPE html> 
                                <html lang="en"> 
                                    <head>
                                        <meta charset="UTF-8">
                                        <title>Error</title>
                                    </head>
                                    <body style="background-color:rgb(255,204,153)">
                                        <h1>ERROR</h1>
                                        <h2>'{full_name}' not found</h2>
                                        <p> Selected specie's {full_name} karyotype information is not available </p>
                                        <p><a href="/karyotype?Specie={full_name}">
                                        Check if your specie is in our database</a><br><br>
                                        <p> Introduce a specie in the database to find its karyotype </p>
                                        <a href="/"> Main page </a> </p>
                                        </body>
                                        </html>"""
                except KeyError:
                    contents = f"""<!DOCTYPE html> 
                                        <html lang="en"> 
                                            <head>
                                                <meta charset="UTF-8">
                                                <title>Error</title>
                                            </head>
                                            <body style="background-color:rgb(255,204,153)">
                                                <h1>ERROR</h1>
                                                <p> Selected specie's cromosome length information is not available </p>
                                                <p><a href="/karyotype?Specie={full_name}">
                                                Check if your specie is in our database</a><br><br>
                                                <p> Introduce a specie in the database 
                                                (with a proper chromosome) to find its length information </p>
                                                <a href="/"> Main page </a> </p>
                                                </body>
                                                </html>"""
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