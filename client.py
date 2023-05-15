from socket import *
from threading import Thread


class Client():
    def __init__(self):
        self.client_socket = socket(AF_INET, SOCK_STREAM)
        self.client_socket.connect(("127.0.0.1", 8002))
        self.observer = None

        # Start a thread that will be reading from the server
        th = Thread(target=self.getMessage)
        th.start()

    def sendMessage(self, msg):
        msg_bytes = str.encode(msg)
        self.client_socket.send(msg_bytes)

    def getMessage(self):
        while True:
            server_msg_bytes = self.client_socket.recv(1024)
            server_msg = server_msg_bytes.decode("utf-8")
            # print(server_msg) #test
            if self.observer is not None:
                self.observer.message_received(server_msg)



if __name__ == "__main__":
    client = Client()