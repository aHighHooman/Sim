import random as rand
from HumanTemplate import human

class merchant(human):
    greetings = []
    def __init__(self, items):
        self.itemList = []
        self.itemAmount = []
        for i in items:
            self.itemList.append(i)
        
        for i in range(len(items)):
            self.itemAmount.append(rand.randomInt(0,5))
        
        return
    
    def checkAvailability(self, ID):
        if(ID >= len(self.itemList)):
            print("I don't have such an item...")
        
        return self.itemList[ID]
    
    def checkItemPrice(self,ID):
        print(f"{self.itemList[ID]}'s price is {self.itemList[ID].price}")
        
        return self.itemList[ID].price
    
    def greet(self):
        print("Hello there")
        
        return

    def askForNeeds(self):
        print("So, what are you looking for?")
        for i in range(len(self.itemList)):
            print(f"{i}. {self.itemList[i]}")
        
        return
    
    def showcaseItem(self,ID):
        
        return self.itemList[ID]
    
    def sellItem(self, buyer,ID):
        buyer.money -= self.itemPrice[ID]
        self.itemAmount[ID] -= 1
        
        return self.itemList[ID]
    

merchant = merchant([])