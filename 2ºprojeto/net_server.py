"""
Aplicações Distribuídas - Projeto 1 - net_server.py
Números de aluno: 62269
"""
from sock_utils import *
import pickle
import struct

class NetServer:
    def __init__(self, host, port):
        """
        Construtor da conexão do servidor
        host - endereço IP do servidor
        port - porta do servidor
        """
        self.host = host
        self.port = port
        self.server_s = create_tcp_server_socket(host,port)
            
    def accept(self):
        """
        Aceita um cliente
        """
        return self.server_s.accept()
    
    def recv(self, client_socket):
        """
        Recebe dados do cliente
        client_socket - socket do cliente
        """
        bytes = receive_all(client_socket, 4)
        data = receive_all(client_socket, struct.unpack('i',bytes)[0])
        msg = pickle.loads(data)
        print(f"RECEV: {msg}")
        return msg
    
    def send(self, client_socket, data):
        """
        Mandar dados para o cliente
        client_socket - socket do cliente
        data - dados a serem enviados
        """
        try:
            msg_pickled = pickle.dumps(data, -1)
            msg_bytes = struct.pack('i', len(msg_pickled))
            client_socket.sendall(msg_bytes)
            client_socket.sendall(msg_pickled)
            print(f"SEND: {data} with size {msg_bytes}")
        except:
            print("NOK")


    def close(self):
        """
        Fecha a socket do servidor
        """
        self.server_s.close()