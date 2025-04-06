from sock_utils import *
import pickle
import struct

class NetClient:
    def __init__(self, host, port):
        """
        Inicializa o NetClient com o host e a porta fornecidos.
        
        Parâmetros:
        host (str): O host do servidor.
        port (int): A porta do servidor.
        """
        self.host = host
        self.port = port
        self.client_socket = create_tcp_client_socket(self.host, self.port)
     
    def send(self, data):
        """
        Envia dados para o servidor, serializando os dados e enviando a mensagem.

        """
        m_pickle = pickle.dumps(data, -1)
        size = struct.pack('i', len(m_pickle))
        
        self.client_socket.sendall(size)
        self.client_socket.sendall(m_pickle)
        
        print(f"SEND: {data} with size {size}.")

    def recv(self):
        """
        Recebe dados do servidor.
        Desserializa os dados e retorna a mensagem.
        """
        bytes = receive_all(self.client_socket, 4)
        data = receive_all(self.client_socket, struct.unpack('i', bytes)[0])
        print(f"RECEV: {pickle.loads(data)}")
        return pickle.loads(data)
    
    def close(self):
        """
        Fecha o socket do cliente.
        """
        self.client_socket.close()