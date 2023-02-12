import random as rand
class NPC:
    greetings = []
    def __init__(self, name, relationship_status, happiness, stress, physical_health, items, prices):
        self.itemsToSell = []
        self.itemPrices = []
        self.itemAmount = []
        self.name = name
        self.relationship_status = relationship_status
        self.happiness = happiness
        self.stress = stress
        self.physical_health = physical_health
        for i in items:
            self.itemsToSell.append(i)
        
        for i in prices:
            self.itemPrices.append(i)
        
        for i in len(items):
            self.itemAmount.append(rand.randomInt(5))
        
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
