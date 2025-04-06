import socket as s

def create_tcp_server_socket(address='localhost', port=9999, queue_size=1):
    """
    Cria um socket TCP servidor e o vincula ao endereço e porta especificados.
    """
    sock = s.socket(s.AF_INET, s.SOCK_STREAM)
    sock.bind((address, port))
    sock.listen(queue_size)
    return sock

def create_tcp_client_socket(address='localhost', port=9999):
    """
    Cria um socket TCP cliente e conecta-se ao servidor especificado pelo endereço e porta.
    """
    sock = s.socket(s.AF_INET, s.SOCK_STREAM)
    sock.connect((address,port))
    return sock

def receive_all(socket, size):
    """
    Recebe dados de um socket até que o número especificado de bytes seja recebido,
    fragmentando a mensagem.
    """
    data = b''
    while len(data) < size:
        pack = socket.recv(size - len(data))
        if not pack:
            return None
        data += pack
    return data

