import random

class DiceRoller:
    
    def __init__(self, numb_of_dice):
        self.numb_of_dice = numb_of_dice
    
    def roll(self,all_value = 0):
        time = 1
        while time <= self.numb_of_dice:
            random_value = random.randint(1,6)
            print("The %dth roll value is: %d" %(time, random_value))
            all_value += random_value
            time += 1
        return all_value
    
    def roll_many(self, n ,n_lst =[]):
        while n > 0:
            n_lst.append(self.roll())
            n -= 1
        print(n_lst)



dice =DiceRoller(2)

dice.roll_many(4)