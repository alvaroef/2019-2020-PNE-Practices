from Client0 import Client


ip = "127.0.0.1"
port = 8080

# -- Create a client object
c = Client(ip, port)

# -- Test the ping method
c.ping()

# -- Print the IP and PORTs
print(f"IP: {c.ip}, {c.port}")
