"""
Aplicações Distribuídas - Projeto 1 - sock_utils.py
Número de aluno: 62269
"""
import socket as s

def create_tcp_server_socket(address='localhost', port=9999, queue_size=1):
    """
    Cria a socket do servidor tcp.
    address - endereço IP do servidor
    port - porta do servidor
    queue_size - tamanho da fila de espera
    """

    sock = s.socket(s.AF_INET, s.SOCK_STREAM)
    sock.bind((address, port))
    sock.listen(queue_size)
    return sock

    
def create_tcp_client_socket(address='localhost', port=9999):
    """
    Cria a socket do cliente tcp.
    address - endereço IP do servidor
    port - porta do servidor
    """
    
    sock = s.socket(s.AF_INET, s.SOCK_STREAM)
    sock.connect((address,port))
    return sock

def receive_all(socket, size):
    data = b''
    while len(data) < size:
        pack = socket.recv(size - len(data))
        if not pack:
            return None
        data += pack
    return data