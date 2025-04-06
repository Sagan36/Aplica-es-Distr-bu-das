from coincenter_data import Asset, User
from typing import Dict,List

class CoinCenterSkeleton:
    def __init__(self):
        self.assets:List[Asset] = []
        self.users:Dict[int,User] = {}

    def handle_request(self, request):
        """
        Processa o pedido
        
        """
        response = None
        id = request[-1]
        if id not in self.users and id != 0:
            self.users[id] = User(id)
            
        try:
            if request[0] == 10: #ADD_ASSET
                response = self.handle_add_asset(request)
            elif request[0] == 20: #GET_ALL_ASSETS
                response = self.handle_get_all_assets(request)
            elif request[0] == 30: #REMOVE_ASSET
                response = self.handle_remove_asset(request)
            elif request[0] == 40: #EXIT
                response = self.handle_exit(request)
            elif request[0] == 50: #GET:ALL_ASSETS
                response = self.handle_get_all_assets(request)
            elif request[0] == 60: #GET_ASSETS_BALANCE
                response = self.handle_get_assets_balance(request)
            elif request[0] == 70: #BUY
                response = self.handle_buy(request)
            elif request[0] == 80: #SELL
                response = self.handle_sell(request)
            elif request[0] == 90: #EXIT
                response = self.handle_exit(request)
            elif request[0] == 100: #DEPOSIT
                response = self.handle_deposite(request)
            elif request[0] == 110: #WITHDRAW
                response = self.handle_withdraw(request)
        except:
            print("ERROR")
            response = [request[0] + 1, False]
        return response
    
    
    def handle_add_asset(self, args):
        for asset in self.assets:
            if asset.symbol == args[2]:
                print("Asset already exists.")
                return [args[0] + 1, False]
        self.assets.append(Asset(args[1],args[2], args[3], args[4]))
        return [args[0] + 1, True]
    
    
    def handle_get_all_assets(self, args):
        r = [args[0]+1, True]
        for aset in self.assets:
            r.append(str(aset))
        return r


    def handle_remove_asset(self, args):
        for i in self.users.values():
            for j in i.holdings:
                if j == args[1]:
                    print("There are users with this asset.")
                    return [args[0]+1, False, args[1]]
        for i in self.assets:
            if i.symbol == args[1]:
                self.assets.remove(i)
                return [args[0]+1, True, args[1]]
        print("Asset not found.")
        return [args[0]+1, False]

    def handle_get_assets_balance(self, args):
        r = [args[0] + 1, True]
        print(self.users)
        user = self.users[args[-1]]
        r.append(user.get_balance())
        for i in user.holdings.items():
            r.append(i)
        return r
                

    def handle_buy(self, args):
        user = self.users.get(args[3])
        for i in self.assets:
            if i.symbol == args[1]: #ve se o ativo existe
                if int(user.balance) >= i.price*float(args[2]):#dinheiro sufueciente na conta do user
                    if i.check_availability(float(args[2])):#ve se a quantidade de ativos é válida
                        user.balance -= i.price*float(args[2])#retira dinheiro da conta do user
                        user.holdings[args[1]] = float(args[2]) + user.holdings.get(args[1], 0.0)
                        i.decrease_quntity(float(args[2]))
                        print("Asset bought.")
                        return [args[0] + 1, True]
                    else:
                        print("There isnt available supply to be bought")
                        return [args[0] + 1, False]
                else:
                    print("You dont have enough money.")
                    return [args[0] + 1, False]
        print("Asset not found.")
        return [args[0] + 1, False]

    def handle_sell(self, args):
        user = self.users.get(args[3])
        if not user.holdings:
            print("You dont have any assets.")
            return [args[0] + 1, False]
        for i in user.holdings.keys():
            for j in self.assets:
                if i == args[1] and j.symbol == args[1]:
                    if float(user.holdings.get(args[1])) >= float(args[2]):
                        user.balance += j.price*float(args[2]) #deposita saldo no utilizador
                        user.holdings[args[1]] =  user.holdings.get(args[1],0.0) - float(args[2])
                        if user.holdings[args[1]] == 0.0:
                            del user.holdings[args[1]]
                        j.increase_quntity(float(args[2]))
                        print("Asset sold.")
                        return [args[0] + 1, True]
                    else:
                        print("There isnt available supply to be sold.")
                        return [args[0] + 1, False]
        print("Asset not found.")
        return [args[0] + 1, False]

    def handle_exit(self, args):  
        print("Server closed.")      
        return [args[0] + 1, True]

    def handle_deposite(self, args):
        user = self.users.get(args[2])
        user.balance += args[1]
        if user.balance == 0:
            print("You cant be in debt.")
            return [args[0] + 1, False]
        return [args[0] + 1, True]
    
    def handle_withdraw(self, args):
        user = self.users.get(args[2])
        user.balance -= args[1]
        return [args[0] + 1, True]
