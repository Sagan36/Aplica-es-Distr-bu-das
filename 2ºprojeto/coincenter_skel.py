import coincenter_data

class CoinCenterSkeleton():
    
    def __init__(self) -> None:
       self.asnwer = []
       
    def ProcessControler(self, message):
        
        answer = []
        
        #adicionoa o cliente á base de dados 
        coincenter_data.ClientController.process_request(message)
            
        #Manager
        try:
            if message[0] == 10: 
                coincenter_data.AssetController.add_asset(message[1], message[2], message[3], message[4]) 
                answer.append(int(message[0]) + 1)
                answer.append("True")
            elif message [0] == 20:
                answer.append(int(message[0]) + 1, coincenter_data.AssetController.list_all_assets())
                answer.append("True")
            elif message[0] == 30:
                coincenter_data.AssetController.remove_asset(message[1])
            elif message[0] == 40:
                answer.append(int(message[0]) + 1)
                answer.append("True") 
            elif message[0] == 50:
                answer.append(int(message[0]) + 1,coincenter_data.AssetController.list_all_assets())
                answer.append("True")   
            elif message[0] == 60:
                answer.append(int(message[0]) + 1, coincenter_data.User.get_balance(), coincenter_data.User.get_holdings())
                answer.append("True")
            elif message[0] == 70:
                coincenter_data.User.buy_asset(message[1], message[2])
                answer.append(int(message[0]) + 1)
                answer.append("True")
            elif message[0] == 80: