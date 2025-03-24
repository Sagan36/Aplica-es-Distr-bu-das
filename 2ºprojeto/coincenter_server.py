"""
Aplicações Distribuídas - Projeto 1 - coincenter_server.py
Números de aluno: 62269
"""

import sys
import signal
from net_server import *
from coincenter_data import *

### código do programa principal ###
server = None

def handle_shutdown(signum, frame):
    global server
    server.close()
    sys.exit(0)

def main():
    """
    Inicializa o servidor e processa os pedidos do cliente
    """
    if len(sys.argv) != 3:
        print("Usage: python3 coincenter_server.py server_ip server_port")
        sys.exit(1)
    
    global server

    server_ip = sys.argv[1]
    server_port = int(sys.argv[2])

    server = NetServer(server_ip, server_port)

    signal.signal(signal.SIGINT, handle_shutdown)
    #Estes dois loops são estritamente necessários pois como queremos que o servidor 
    #esteja sempre ligado este deverá sempre estar conectado com a client_socket, assim ter um 
    #loop somente pare esta necessidade, sendo o outro loop ser para o servidor receber o 
    #request do client sempre que este faz o pedido e não infinitamente.
    try:
        while True:
            (conn_sock, (server_ip,server_port)) = server.accept()
            while True:
                request = server.recv(conn_sock)
                if request[0] == "EXIT":
                    break
                else:
                    processed_request = ClientController.process_request(request)
                server.send(conn_sock, processed_request)
    except:
        return "ERROR"
if __name__ == "__main__":
    main()
