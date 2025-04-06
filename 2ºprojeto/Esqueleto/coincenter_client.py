from coincenter_stub import CoinCenterStub
import sys

def is_valid_command(command):
    list_commads = ["ADD_ASSET", "GET_ALL_ASSETS", "REMOVE_ASSET", "EXIT", "GET_ASSETS_BALANCE", "BUY", "SELL", "DEPOSIT", "WITHDRAW"]
    if command[0].upper() in list_commads:
        return True
    else:
        return False



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
        checker = choice.split(";")
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
        checker = choice.split(";")
        return checker
    except:
        print("ERROR")
        return "ERROR"
 
 
 
    
def main():
    if len(sys.argv) != 4:
        print("Usage: python3 coincenter_client.py user_id server_ip server_port")
        sys.exit(1)

    user_id = int(sys.argv[1])
    server_ip = sys.argv[2]
    server_port = int(sys.argv[3])

    stub = CoinCenterStub(user_id,server_ip,server_port)

    while True:
        if user_id == 0:
            command = show_manager_menu()

            if is_valid_command(command):
                response = stub.handle_command(command)
                if response[0] == 41:
                    print("bye bye")
                    break
            else:
                print("invalid command")
        else:
            command = show_user_menu()
            print(command)
            if is_valid_command(command):
                response = stub.handle_command(command)
                if response[0] == 91:
                    print("bye bye")
                    #se a socket é eliminada das sockets ativas, então já não é preciso fazer o stub.exit() pois a socket ja nao existe sequer graças ao servidor
                    break
            else:
                print("invalid command")

if __name__ == "__main__":
    main()