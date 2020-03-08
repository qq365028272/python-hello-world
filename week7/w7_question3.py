import random
class CoinFlipper:
    
    def __init__(self,num_of_coins = None):
        self.num_of_coins = num_of_coins
    
    def flip(self, coin_lst = None):
        num_of_coins = random.randint(1,2)
        #coin_lst.append(num_of_coins)
        #retrun coin_lst
        return num_of_coins


