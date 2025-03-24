"""
Aplicações Distribuídas - Projeto 1 - coincenter_data.py
Números de aluno: 62269 
"""
from typing import Dict,List
from abc import ABC, abstractmethod




class Asset:
    """
    Cria um objeto Asset com os seguintes atributos:
        symbol - símbolo do ativo
        name - nome do ativo
        price - preço do ativo
        available_supply - quantidade disponível do ativo
    """
    def __init__(self, symbol: str, name: str, price: float, available_supply: int):
        """
        Construtor
        """
        self.symbol = symbol
        self.name = name
        self.price = price
        self.available_supply = available_supply

    def __str__(self):
        return f"{self.name} ({self.symbol}): Price = {self.price}, Supply = {self.available_supply}"

    def check_availability(self, quantity:float) -> bool:
        """
        Verifica se a quantidade de ativos é válida
        quantity - quantidade de ativos
        """ 
        return quantity > 0 and quantity <= self.available_supply

    def decrease_quantity(self, quantity:float) -> bool:
        """
        Decrementa a quantidade de ativos
        quatity - quantidade de ativos
        """ 
        if self.check_availability(quantity):
            self.available_supply -= quantity
            return True
        else:
            return False

    def increase_quantity(self, quantity:float):
        """
        Incrementa a quantidade de ativos
        quatity - quantidade de ativos
        """
        self.available_supply += quantity




class AssetController:
    """
    Controla os ativos
    """
    assets:List[Asset] = []
    @staticmethod
    def list_all_assets()->str:
        """
        Faz uma lista de todos os ativos.
        """
        if len(AssetController.assets) == 0:
            return "There is no active assets you should add one."
        else:
            assettoSTR = "\n".join(list(map(str, AssetController.assets)))#Transforma os objetos assets em strings legiveis
            return assettoSTR 
    
    @staticmethod
    def remove_asset(symbol:str):
        """
        Remove um ativo
        symbol - símbolo do ativo
        """
        Allclients = ClientController.clients
        for i in Allclients.values():
            if isinstance(i, User):
                for j in i.holdings:
                    if j == symbol:
                        print("There are users with this asset.")
                        return False
        for i in AssetController.assets:
            if i.symbol == symbol:
                AssetController.assets.remove(i)
                return True
        print("Asset not found.")
        return False
    @staticmethod
    def add_asset(symbol:str,name:str,price:float,available_supply:int):
        """
        Adiciona um ativo
        symbol - símbolo do ativo
        name - nome do ativo
        price - preço do ativo
        available_supply - quantidade disponível do ativo
        """
        for i in AssetController.assets:
            if i.symbol == symbol:
                return print("This asset already exists.")
        AssetController.assets.append(Asset(symbol, name, float(price), int(available_supply)) )       




class Client(ABC):
    """
    Classe abstrata que representa um cliente
    """
    def __init__(self, id):
        self.id = id
    
    @abstractmethod
    def process_request(self,_):
        """
        Método abstrato que processa um pedido, que vai ser 
        implementado nas classes User e Manager.
        """
        pass
                


        
class User(Client):
    """
    Classe que representa um utilizador, um dos tipos de clientes.
    """
    def __init__(self, user_id: str, balance: float = 0.0, holdings: dict = {}):
        """
        Construtor
        user_id - id do utilizador
        balance - saldo do utilizador
        holdings - ativos do utilizador

        """
        super().__init__(user_id) 
        self.balance = balance  
        self.holdings = holdings 
        
    def __str__(self) -> str:
        holdingslist = []
        for i in self.holdings:
            holdingslist.append([i.key, i.value])
        return f"User ID: {self.user_id}, Balance: ${self.balance}, Holdings: {holdingslist}"

    def buy_asset(self, asset_symbol:str, quantity:float) -> bool:
        """
        Compra um ativo
        asset_symbol - símbolo do ativo
        quantity - quantidade de ativos
        """
        for i in AssetController.assets:
            if i.symbol == asset_symbol:#ve se o ativo existe
                if int(self.balance) >= i.price*float(quantity):#ve se o utilizador tem dinheiro suficiente
                    if i.check_availability(float(quantity)):#ve se a quantidade de ativos é válida
                        self.withdraw(i.price*float(quantity))
                        self.holdings[asset_symbol] = float(quantity) + self.holdings.get(asset_symbol, 0.0)
                        i.decrease_quantity(float(quantity))
                        print("Asset bought.")
                        return True
                    else:
                        print("There isnt available supply to be bought")
                        return False
                else:
                    print("You dont have enough money.")
                    return False        
        print("Asset not found.")
        return False
    
    def sell_asset(self, asset_symbol:str, quantity:float) -> bool:
        """
        Vende um ativo
        asset_symbol - símbolo do ativo
        quantity - quantidade de ativos
        """
        if not self.holdings:
            print("You dont have any assets.")
            return False
        
        for i in self.holdings.keys():
            for j in AssetController.assets:
                if i == asset_symbol and j.symbol == asset_symbol:
                    if float(self.holdings.get(asset_symbol)) >= float(quantity):
                        self.deposit(j.price*float(quantity))
                        self.holdings[asset_symbol] =  self.holdings.get(asset_symbol,0.0) - float(quantity)
                        j.increase_quantity(float(quantity))
                        return True
                    else:
                        print("There isnt available supply to be sold.")
                        return False
        print("Asset not found.")
        return False

    def deposit(self,amount:int):
        """
        Deposita dinheiro
        amount - quantidade de dinheiro
        """
        self.balance += amount

    def withdraw(self,amount:int):
        """
        Efetua um levantamento
        amount - quantidade de dinheiro
        """
        self.balance -= amount
    
    def process_request(self, request) -> str:
        """
        Processa um pedido do tipo user e retorna uma string
        request - comando vindo do cliente com as acoes a serem tomadas
        """
        action_atm = str(request[0])
        try:   
            if action_atm == "GET_ALL_ASSETS":
                return AssetController.list_all_assets()
            
            elif action_atm == "GET_ASSETS_BALANCE":
                if len(self.holdings) == 0:
                    return f"BALANCE:{self.balance}. You dont have any assets."
                else:
                    return f"BALANCE:{self.balance}. ASSETS:{self.holdings}"
            
            elif action_atm == "BUY":
                self.buy_asset(request[1],request[2])
                return "OK" 
            
            elif action_atm == "SELL":
                self.sell_asset(request[1], request[2])
                return "OK"
            
            elif action_atm == "DEPOSIT":
                self.deposit(int(request[1]))
                return "OK"
                
            elif action_atm == "WITHDRAW":
                self.withdraw(int(request[1]))
                return "OK"   
        except:
            return print("NOK")



class Manager(Client):
    """
    Classe que representa um gestor, um dos tipos de clientes.
    """
    def __init__(self, user_id):
        """
        Construtor
        user_id - id do utilizador
        """
        super().__init__(user_id)

    def process_request(self, request):
        """
        Processa um pedido do tipo manager e retorna uma string
        request - comando vindo do cliente com as acoes a serem tomadas
        """
        
        try:
            action_atm = str(request[0])
            
            if action_atm == "ADD_ASSET":
                AssetController.add_asset(request[2], request[1],request[3], request[4])
                return f"Asset added:{request[2]}"
            elif action_atm == "GET_ALL_ASSETS":
                return f"{AssetController.list_all_assets()}"       
            elif action_atm == "REMOVE_ASSET":
                AssetController.remove_asset(request[1])
                return "OK"
        except:
            return print("NOK")
        
        
        
class ClientController:
    """
    Controla os clientes
    """
    clients:Dict[int,Client] = {0:Manager(0)}
    @staticmethod
    def process_request(request:str)->str:
        """
        Processa um pedido que vai ser filtrado tendo em conta o tipo de cliente 
        request - comando vindo do cliente com as acoes a serem tomadas
        """
        client_id = int(request[-1])
        if client_id not in ClientController.clients:
            ClientController.clients[client_id] = User(client_id)
        return ClientController.clients[client_id].process_request(request)            