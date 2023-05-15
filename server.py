from socket import *
from threading import Thread


class Connection:
    def __init__(self, conn, addr, name):
        self.conn = conn
        self.addr = addr
        self.name = name

    def sendMessage(self, msg):
        self.conn.send(str.encode(msg))

class Server:
    def __init__(self):
        self.connections = []
        self.server_socket = socket(AF_INET, SOCK_STREAM)
        self.server_socket.bind(("127.0.0.1", 8002))

        self.server_socket.listen()
        print("Server started at post 8001")
        self.start()

    def start(self):
        received_msg = str.encode("Your message is received\n")
        while True:
            conn, addr = self.server_socket.accept()
            print(conn, addr) #test
            message_bytes = conn.recv(1024)
            name = message_bytes.decode("utf-8")
            
            conn.send(received_msg)
            connection = Connection(conn, addr, name)
            
            self.connections.append(connection)
            self.broadcast(name + " connected ...")

            th = Thread(target=self.connectionThread, args=(connection,))
            th.start()

    def broadcast(self, msg):
        for connection in self.connections:
            connection.sendMessage(msg)

    def connectionThread(self, connection):
        print("Thread started for " + str(connection.addr))
        connection.sendMessage("Welcome " + connection.name + " we hope you brought some pizza!")
        while True:
            msg = connection.conn.recv(1024).decode('utf-8')
            self.broadcast(connection.name + ": " + msg)


if __name__ == "__main__":
    server = Server()
