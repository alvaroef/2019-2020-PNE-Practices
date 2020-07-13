from Client0 import Client


ip = "127.0.0.1"
port = 8080

# -- Create a client object
c = Client(ip, port)

# -- Print the IP and PORTs
print(c)

# -- Send a message to the server
c.debug_talk("Message 1---")
c.debug_talk("Message 2: Testing !!!")
