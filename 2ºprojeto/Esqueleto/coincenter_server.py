from coincenter_skel import CoinCenterSkeleton
from net_server import NetServer
import select
import sys
import signal

server = None


def handle_shutdown(signum, frame):
    global server
    server.close()
    sys.exit(0)
    
def main():
    if len(sys.argv) != 3:
        print("Usage: python3 coincenter_server.py server_ip server_port")
        sys.exit(1)
    global server
    server_ip = sys.argv[1]
    server_port = int(sys.argv[2])

    net_server = NetServer(server_ip, server_port)
    skel = CoinCenterSkeleton()

    sockets = [net_server.server_socket]
    signal.signal(signal.SIGINT, handle_shutdown)

    while True:
        try:
            ready_to_read, _, _ = select.select(sockets, [], [])
            for sock in ready_to_read:
                if sock is net_server.server_socket:
                    client_sock, _ = net_server.accept()
                    sockets.append(client_sock)
                else:
                    try:
                        request = net_server.recv(sock)
                        if request[0] == 40 or request[0] == 90:
                            response = skel.handle_request(request)
                            net_server.send(sock, response)
                            sock.close()
                            sockets.remove(sock)
                            print("Client disconnected")
                        else:
                            response = skel.handle_request(request)
                            net_server.send(sock, response)
                    except Exception as e:
                        print(f"Error processing request: {e}")
                        print(request)

        except Exception as e:
            print("ERROR", e)
            exit(0)
                
if __name__ == "__main__":
    main()



