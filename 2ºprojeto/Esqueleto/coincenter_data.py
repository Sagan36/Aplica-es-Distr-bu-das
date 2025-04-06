from typing import Dict,List

class Asset:
    def __init__(self, name:str, symbol:str, price:float, available_supply:int):
        self.symbol = symbol
        self.name = name
        self.price = price
        self.available_supply = available_supply

    def __str__(self):
        return f"{self.name} ({self.symbol}): Price = {self.price}, Supply = {self.available_supply}"

    def check_availability(self, quantity:int) -> bool:
        """
        Confirma se a quantidade de ativos é válida
        """
        return quantity > 0 and quantity <= self.available_supply

    def decrease_quntity(self, quantity:int) -> bool:
        """
        Reduz a quantidade de ativos
        """
        if self.check_availability(quantity):
            self.available_supply -= quantity
            return True
        else:
            return False
    def increase_quntity(self, quantity):
        """
        Aumenta a quantidade de ativos
        """
        self.available_supply += quantity

class User():
    def __init__(self, id):
        self.id = id    
        self.balance = 100
        self.holdings:Dict[str,float] = {}
    
    def get_holdings(self):
        return self.holdings
    def get_balance(self):
        return self.balance