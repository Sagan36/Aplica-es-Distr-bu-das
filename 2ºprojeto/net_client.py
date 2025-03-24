"""
Aplicações Distribuídas - Projeto 1 - net_client.py
Números de aluno: 62269
"""
from sock_utils import *
import pickle
import struct
class NetClient:
    def __init__(self,host, port):
        """
        Construtor da conexão do cliente
        id - identificador do cliente
        host - endereço IP do servidor
        port - porta do servidor
        """
        self.client_s = create_tcp_client_socket(host, port)
        
    def send(self, data):
        """
        Envia dados para o servidor
        data - dados a serem enviados
        """
        
        m_pickle = pickle.dumps(data, -1)
        size = struct.pack('i',len(m_pickle))
        self.client_s.sendall(size)
        self.client_s.sendall(m_pickle)
        print(f"SEND: {data} with size {size}.")
        

    def recv(self):
        """
        Recebe dados do servidor
        """
        bytes = receive_all(self.client_s, 4)
        data = receive_all(self.client_s, struct.unpack('i',bytes)[0])
        print(f"RECEV: {pickle.loads(data)}")
    
    def close(self):
        """
        Fecha a socket do cliente
        """
        self.client_s.close()