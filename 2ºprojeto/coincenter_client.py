"""
Aplicações Distribuídas - Projeto 1 - coincenter_client.py
Números de aluno: 62269
"""

import sys
from net_client import *

### código do programa principal ###



def show_manager_menu():
    """
    Controlo do menu do manager
    """
    print("Manager Menu")
    print("1. Add new asset")
    print("2. Remove asset")
    print("3. View all assets")
    print("4. Exit")
    try:
        choice = input("command >")
        valid_commands = ["ADD_ASSET", "GET_ALL_ASSETS", "REMOVE_ASSET", "EXIT"]
        checker = choice.split(";")
        if checker[0] not in valid_commands:
            return print("ERROR")
        return checker
    except:
        print("ERROR")
        return "ERROR"

    
    
    
def show_user_menu():
    print("User Menu:")
    print("1. View all assets")
    print("2. Check asset balance")
    print("3. Buy asset")
    print("4. Sell asset")
    print("5. Deposit funds")
    print("6. Withdraw funds")
    print("7. Exit")
    try:
        choice = input("command >")
        valid_commands = ["ADD_ASSET", "GET_ALL_ASSETS", "REMOVE_ASSET", 
                    "GET_ASSETS_BALANCE", "BUY", "SELL", "DEPOSIT", "WITHDRAW", "EXIT"]
        checker = choice.split(";")
        if checker[0] not in valid_commands:
            return print("ERROR")
        return checker
    except:
        print("ERROR")
        return "ERROR"
    
    
    
def main():
    """
    Inicializa o cliente e processa os pedidos do utilizador
    """
    if len(sys.argv) != 4:
        print("Usage: python3 coincenter_client.py user_id server_ip server_port")
        sys.exit(1)
    user_id = str(sys.argv[1])
    server_ip = sys.argv[2]
    server_port = int(sys.argv[3])
    client = NetClient(user_id,server_ip,server_port)
    try:
        while True:   
                if user_id == "0":
                    request = show_manager_menu()
                    if request == "EXIT":
                        print("Exiting.")
                        request.append(user_id)
                        client.send(request)
                        client.close()
                        break
                    else:
                        request.append(user_id)
                        client.send(request)
                        client.recv()
                else:
                    request = show_user_menu()
                    if request == "EXIT":
                        request.append(user_id)
                        client.send(request)
                        print("Exiting.")
                        client.close()
                        break
                    else:
                        request.append(user_id)
                        client.send(request)
                        client.recv()       
    except:
        return "ERROR"
if __name__ == "__main__":
    main()