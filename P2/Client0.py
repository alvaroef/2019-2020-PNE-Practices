class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    @staticmethod
    def ping():
        print('OK!')
