#o stub remistura o pedido e filtra o e dps manda para o servidor 

from net_client import NetClient

class CoinCenterStub:
    
    def __init__(self, host, port, id):
        self.id = id
        self.server = NetClient(host,port)#quando e criada a socket esta automaticamente conecta-se

    def disconnect(self):
        self.server.close()
    
    #gestor
    
    def ADD_ASSET(self, symbol, price, supply):
        request = [10, symbol, price, supply, self.id]
        return self.server.send(request)
        
    def GET_ALL_ASSETS_G(self):
        request = [20,self.id]
        return self.server.send(request)
    
    def REMOVE_ASSET(self,symbol):
        request = [30,symbol, self.id]
        return self.server.send(request)
    
    def EXITG(self):
        request = [40,self.id]
        return self.server.send(request)
    
    #utilizador
    
    def GET_ALL_ASSETS_U(self):
        request = [50, self.id]
        return self.server.send(request)
    
    def GET_ASSETS_BALANCE(self):
        request = [60, self.id]
        return self.server.send(request)
    
    def BUY(self, symbol, quantity):
        request = [70, symbol, quantity, self.id]
        return self.server.send(request)
    
    def SELL(self, symbol, quantity):
        request = [80, symbol, quantity, self.id]
        return self.server.send(request)
    
    def WITHDRAW(self, quantity):
        request = [110, quantity, self.id]
        return self.server.send(request)
    
    def DEPOSIT(self, quantity):
        request = [100, quantity, self.id]
        return self.server.send(request)
    
    def EXITU(self):
        request = [90, self.id]
        return self.server.send(request)
        