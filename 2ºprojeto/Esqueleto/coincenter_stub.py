from net_client import NetClient

class CoinCenterStub:
    def __init__(self, user_id,server_ip,server_port):
        self.id = user_id
        self.net_client = NetClient(server_ip, server_port)

    def handle_command(self, command):
        """
        Trata dos comandos recebidos do utilizador.
        """
        response = None
        try:
            if self.id == 0: #gestor
                if command[0] == "ADD_ASSET":
                    response = self.add_asset(command[1],command[2],float(command[3]),float(command[4]))
                elif command[0] == "GET_ALL_ASSETS":
                    response = self.get_all_assets()
                elif command[0] == "REMOVE_ASSET":
                    response = self.remove_asset(command[1])
                elif command[0] == "EXIT":
                    response = self.exit()
            else: #user
                if command[0] == "GET_ALL_ASSETS":
                    response = self.get_all_assets()
                elif command[0] == "GET_ASSETS_BALANCE":
                    response = self.get_assets_balance()
                elif command[0] == "BUY":
                    response = self.buy(command[1], float(command[2]))
                elif command[0] == "SELL":
                    response = self.sell(command[1], float(command[2]))
                elif command[0] == "DEPOSIT":
                    response = self.deposite(float(command[1]))
                elif command[0] == "WITHDRAW":
                    response = self.withdraw(float(command[1]))
                elif command[0] == "EXIT":
                    response = self.exit()
        except:
            response = ["ERROR the command is not valid or it doesnt have the right arguments" ]
        return response
            
    def add_asset(self, asset_name, asset_symbol, asset_price, available_supply):
        request = [10, asset_name, asset_symbol, asset_price, available_supply, self.id]
        self.net_client.send(request)
        response = self.net_client.recv()
        return response

    def get_all_assets(self):
        if self.id == 0:
            request = [20,self.id]
        else:
            request = [50,self.id]
        self.net_client.send(request)
        response = self.net_client.recv()
        return response

    def remove_asset(self, asset_symbol):
        request = [30,asset_symbol, self.id]
        self.net_client.send(request)
        response = self.net_client.recv()
        return response

    def get_assets_balance(self):
        request = [60,self.id]
        self.net_client.send(request)
        response = self.net_client.recv()
        return response

    def buy(self, asset_symbol,quantity):
        request = [70, asset_symbol,quantity, self.id]
        self.net_client.send(request)
        response = self.net_client.recv()
        return response

    def sell(self, asset_symbol, quantity):
        request = [80, asset_symbol, quantity, self.id]
        self.net_client.send(request)
        response = self.net_client.recv()
        return response

    def deposite(self, quantity):
        request = [100, quantity, self.id]
        self.net_client.send(request)
        response = self.net_client.recv()
        return response
    
    def withdraw(self, quantity):
        request = [110,quantity, self.id]
        self.net_client.send(request)
        response = self.net_client.recv()
        return response

    def exit(self):
        if self.id == 0:
            request = [40,self.id]
        else:
            request = [90,self.id]
        self.net_client.send(request)
        response = self.net_client.recv()
        return response