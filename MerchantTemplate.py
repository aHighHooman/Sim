import random as rand
from HumanTemplate import human
class merchant(human):
    greetings = []
    def __init__(self, items, prices):
        self.itemsToSell = []
        self.itemPrices = []
        self.itemAmount = []
        for i in items:
            self.itemsToSell.append(i)
        
        for i in prices:
            self.itemPrices.append(i)
        
        for i in len(items):
            self.itemAmount.append(rand.randomInt(0,5))
        
        return
    
    def checkAvailability(self, ID):
        if(ID >= len(self.itemsToSell)):
            print("I don't have any other items at hand unfotunately...")
        return self.itemsToSell[ID]
    
    def checkItemPrice(self,ID):
        return self.itemPrices[ID]
    
    def greet(self):
        return

    def askForNeeds(self):
        return
    
    def showcaseItem(self,ID):
        return
    
    def sellItem(self,ID):
        return
