import socket as s
import sys

def create_tcp_server_socket(address, port, queue_size):
    sock = s.socket(s.AF_INET, s.SOCK_STREAM)
    sock.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1)
    sock.bind((address, port))
    sock.listen(queue_size)
    return sock

def create_tcp_client_socket():
    sock = s.socket(s.AF_INET, s.SOCK_STREAM)
    return sock

def receive_all(socket, length):
    #return socket.recv(length)
    data = ''
    while length > 0:
        packet = socket.recv(1024)
        length = len(length) - sys.getsizeof(packet)
        if not packet:
            return None
        data += data + packet
    return data
