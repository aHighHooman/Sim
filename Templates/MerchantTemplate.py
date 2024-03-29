import random as rand
from Templates import HumanTemplate as h
class merchant(h.human):
    greetings = []
    def __init__(self, items):
        self.itemList = []
        self.itemAmount = []
        for i in items:
            self.itemList.append(i)
        
        for i in range(len(items)):
            self.itemAmount.append(rand.randint(0,5))
        
        return
    
    def checkAvailability(self, ID):
        if(ID >= len(self.itemList)):
            print("I don't have such an item...")
        else: 
            print(f"I have {self.itemAmount[ID]} {self.itemList[ID].name}s")
            return self.itemList[ID]
    
    def checkItemPrice(self,ID):
        print(f"{self.itemList[ID].name}'s price is {self.itemList[ID].price}")
        
        return self.itemList[ID].price
    
    def greet(self):
        print("Hello there")
        
        return

    def askForNeeds(self):
        print("So, what are you looking for?")
        for i in range(len(self.itemList)):
            print(f"{i+1}. {self.itemList[i].name}")
        
        return
    
    def showcaseItem(self,ID):
        
        return self.itemList[ID]
    
    def sellItem(self, buyer,ID):
        buyer.money -= self.itemPrice[ID]
        self.itemAmount[ID] -= 1
        
        return self.itemList[ID]
    
