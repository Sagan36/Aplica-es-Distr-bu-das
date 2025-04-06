from sock_utils import *
import pickle
import struct

class NetServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = create_tcp_server_socket(host,port)

    def accept(self):
        """
        Aceita uma conexão de um cliente e retorna o socket do cliente e o endereço.
        """
        client_socket, client_address = self.server_socket.accept()
        return client_socket, client_address
    
    
    def recv(self, client_socket):
        """
        Recebe dados do cliente, desserializa os dados e retorna a mensagem.
        """
        bytes = receive_all(client_socket, 4)
        data = receive_all(client_socket, struct.unpack('i',bytes)[0])
        msg = pickle.loads(data)
        print(f"RECEV: {msg}")
        return msg
    
    def send(self, client_socket, data):
        """
        Manda dados para o cliente, serializa os dados e envia a mensagem.
        """
        msg_pickled = pickle.dumps(data, -1)
        msg_bytes = struct.pack('i', len(msg_pickled))
        client_socket.sendall(msg_bytes)
        client_socket.sendall(msg_pickled)
        print(f"SEND: {data} with size {msg_bytes}")
        
    def close(self):
        """
        Fecha o socket do servidor.
        """
        self.server_socket.close()