"""
Aplicações Distribuídas - Projeto 1 - coincenter_client.py
Números de aluno: 62269
"""

import sys
from coincenter_stub import *

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
    

def run_command(prompt, stub, id):
    #Manager
    if prompt[0] == "EXIT" and id == "0":
        stub.EXITG()
        stub.disconnect()
    elif prompt[0] == "ADD_ASSET":
        stub.ADD_ASSET(prompt[1], prompt[2], prompt[3], prompt[4])
    elif prompt[0] == "GET_ALL_ASSETS" and id == "0":
        stub.GET_ALL_ASSETS_G()
    elif prompt[0] == "REMOVE_ASSET":
        stub.REMOVE_ASSET()
    #Utilizador
    elif prompt[0] == "EXIT" and int(id) > 0:
        stub.EXITU()
        stub.disconect()
    elif prompt[0] == "GET_ALL_ASSETS_U" and int(id) > 0:
        stub.GET_ALL_ASSETS_U()
    elif prompt[0] == "GET_ASSETS_BALANCE":
        stub.GET_ASSETS_BALANCE()
    elif prompt[0] == "BUY":
        stub.BUY(prompt[1], prompt[2])
    elif prompt[0] == "SELL":
        stub.SELL(prompt[1], prompt[2])
    elif prompt[0] == "WITHDRAWM":
        stub.WITHDRAW(prompt[1])
    elif prompt[0] == "DEPOSIT":
        stub.DEPOSIT(prompt[1])
        
        
        
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
    client = CoinCenterStub(user_id,server_ip,server_port)
    try:
        while True:   
                if user_id == "0":
                    request = show_manager_menu()
                    if request[0] == "EXIT":
                        print("Exiting.")
                        run_command(client,user_id)
                        client.disconnect()
                        break
                    else:
                        run_command(client,user_id)
                        client.recv()
                else:
                    request = show_user_menu()
                    if request[0] == "EXIT":
                        print("Exiting.")
                        run_command(client,user_id)
                        client.close()
                        break
                    else:
                        client.send(request)
                        client.recv()
    except Exception as e:
        print(e)
        return "ERROR"
if __name__ == "__main__":
    main()