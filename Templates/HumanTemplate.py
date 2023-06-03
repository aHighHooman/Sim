import random





#map
h = "h"
p = "p"
g = "g"

class GameMap():
    def __init__(self):
        self.size = (10,10)
        self.mapp = [
            [g,g,g,h,p,p,h,g,g,g],
            [g,g,g,h,p,p,h,g,g,g],
            [g,g,g,h,p,p,h,g,g,g],
            [h,h,h,h,p,p,h,h,h,h],
            [p,p,p,p,p,p,p,p,p,p],
            [p,p,p,p,p,p,p,p,p,p],
            [h,h,h,h,p,p,h,h,h,h],
            [g,g,g,h,p,p,h,g,g,g],
            [g,g,g,h,p,p,h,g,g,g],
            [g,g,g,h,p,p,h,g,g,g],
        ]
        return

    def printMap(self):
        for row in self.mapp:
            print(row)
        print("\n\n")
        return

    def updateMap(self,character):
        newX = character.coordinate[0]
        newY = character.coordinate[1]
        oldX = 5 #for initialization
        oldY = 5 #for initialization
        for i in range(len(self.mapp)):
            if "N" in self.mapp[i]:
                oldX = i
                oldY = self.mapp[i].index("N")
                break
          
        self.mapp[oldX][oldY] = character.coordinateContent
        self.mapp[newX][newY] = "N"   
        return












class item:
    def __init__(self,name):
        self.name = name
        self.durability = random.randint(1,10)
        self.weight = random.randint(1,10)
        self.quality = random.randint(1,10)
        self.damage = random.randint(1,10)
        self.price = random.randint(10,1000)

#Weapons
sword = item("Sword")
axe =   item("Axe")
bow =   item("Bow")
spear = item("Spear")
pistol= item("Pistol")
#Ammo
arrow = item("Arrow")
bullet= item("Bullet")
#Lists
weaponList =    [sword, axe, bow, spear]
ammoList =      [arrow, bullet]


class location:
    def __init__(self,name,type,description):
        self.name = name
        self.type = type
        self.description = description

smithy1 = location("smithy","business", "A small, dimly lit blacksmith forge with a roaring fire in the hearth.")

class human:
    names_M = [
                "Liam", 
                "Oliver", 
                "Noah", 
                "Elijah", 
                "William", 
                "James", 
                "Benjamin", 
                "Lucas"]
    names_F = [
                "Olivia", 
                "Emma",
                "Charlotte", 
                "Amelia", 
                "Ava", 
                "Sophia", 
                "Isabella", 
                "Mia"]
    jobs = [
        "Party Leader", 
        "Blacksmith", 
        "Trainer", 
        "Mayor", 
        "Adventurer", 
        "Hunter", 
        "Alchemist"
        "Merchant"]
    
    def __init__(self): 
        self.traitList = [
            "Heroic", 
            "Will to Live", 
            "Cool Headed", 
            "Observant", 
            "Coward", 
            "Curious", 
            "Prideful", 
            "Prepared"]        
        self.combat_talents = [
            "Sword", 
            "Spear", 
            "Dagger", 
            "Archer", 
            "Gunsman", 
            "Large Mana", 
            "Elemental Affinity", 
            "Intruition", 
            "Camouflage", 
            "Artillery Load", 
            "Scouting", 
            "Ambidextrous"]
        self.general_talents = [
            "Management", 
            "High Adaptability", 
            "High Charisma", 
            "Quick Learner", 
            "Creative", 
            "Large Build",
            "Blacksmithing", 
            "Farmer", 
            "Builder", 
            "Engineer", 
            "Cook"]
        self.talents = []
        self.traits = []
        self.skills = []
        self.coordinate = [5,5]
        self.coordinateContent = "p"

        self.generateParameters()
        
        
    def generateParameters(self):
        #Sex
        biology = random.randint(0,1)
        if(biology == 1):
            self.sex = "M"
            self.name = random.choice(human.names_M)
            #human.names_M.remove(self.name)
        else: 
            self.sex = "F"
            self.name = random.choice(human.names_F)
            #human.names_F.remove(self.name)
        
        #Growth Factor
        self.mentalGF = random.randint(0,10)
        self.physicalGF = random.randint(0,10)
        
        #Job
        self.job = random.choice(human.jobs)
        #if(self.job == "Mayor"):
            #human.jobs.remove(self.job)
        
        #Traits
        for i in range(3): 
            randomTrait = random.choice(self.traitList)
            self.traits.append(randomTrait) 
            self.traitList.remove(randomTrait)
        #self.traitType = []
        #self.traitIntensity = []
        self.traitTarget = random.choice(["self","party"])

        #Talent
        self.generateTalents()
    
        #Mental State
        self.stress = random.randint(0,60)
        self.happiness = random.randint(0,80)
        self.health = 80

        #Reputation
        self.charisma = random.randint(0,100)
        self.feats = []
        #self.home =  []
        self.wealth = random.randint(0,10**4)

        #Relationships
        #self.affection = []
        #self.trust = []
        #self.compatibility = []

        #Looks
        #self.looks = []

        #Skill
        #self.skills = []
        #self.skillLevel = []
        #self.skillRank = []

        return
        
    def generateTalents(self): #Domain+Rank
        i = True
        while(i == True):
            domain = random.randint(1,2)
            if(domain == 1): #if you get combat talents
                if(random.uniform(0,1) < 1/(len(self.talents) + 1)):
                    combatTalent = random.choice(self.combat_talents)
                    self.talents.append(combatTalent)
                    self.combat_talents.remove(combatTalent)
                else:
                    i = False
            elif(domain == 2): # if you get general talents
                if(random.uniform(0,1) < 1/(len(self.talents) + 1)):
                    generalTalent = random.choice(self.general_talents)
                    self.talents.append(generalTalent)
                    self.general_talents.remove(generalTalent)
                else: 
                    i = False

    def buyItem(self,item,merchant):
        print(f"{self.name}: Hmm, okay then I'll buy it!")
        merchant.sellItem(self, merchant.itemList.index(item))

    def movement(self,refMap,type = "wander"):
        moveType = {"wander":True,
                  "target":False}
        wander = moveType[type]

        if(wander):
            futureX = self.coordinate[0] + random.randint(-1,1)
            futureY = self.coordinate[1] + random.randint(-1,1)
            if (futureX > refMap.size[0]):
                futureX = refMap.size[0]
            elif (futureX < 0):
                futureX = 0
            if (futureY > refMap.size[1]):
                futureY = refMap.size[1]
            elif (futureY < 0):
                futureY = 0
        
            if (refMap.mapp[futureX][futureY] == "N"): #optimizable
                return
            else:
                refMap.mapp[self.coordinate[0]][self.coordinate[1]] = self.coordinateContent
                self.coordinate[0] = futureX
                self.coordinate[1] = futureY
                return
        else:
            return

        
   

class merchant(human):
    greetings = []
    def __init__(self, items):
        super().__init__()
        self.job = "Merchant"
        self.itemList = []
        self.itemAmount = []
        for i in items:
            self.itemList.append(i)
        for i in range(len(items)):
            self.itemAmount.append(random.randint(1,5))

    def checkAvailability(self, ID):
        if((ID >= len(self.itemList)) or (ID < 0)):
            print(f"{self.name}: I don't have such an item...")
            return 0
        else: 
            if(self.itemAmount[ID] > 1):
                print(f"{self.name}: I have {self.itemAmount[ID]} {self.itemList[ID].name}s")
            elif(self.itemAmount[ID] > 0):
                print(f"{self.name}: I have {self.itemAmount[ID]} {self.itemList[ID].name}")
            else:
                print(f"{self.name}: Unfortunately I am out of {self.itemList[ID].name}s haha..")
            return self.itemList[ID]
    
    def checkItemPrice(self,ID):
        print(f"{self.name}: {self.itemList[ID].name}'s price is {self.itemList[ID].price}")
        return self.itemList[ID].price
    
    def greet(self):
        greetings = [
            "Hail, traveler!",
            "Well met, adventurer!",
            "Greetings, friend! I'm the local smithy.",
            "Ho there! Looking for some metalwork? You've come to the right place.",
            "Welcome to my forge!",
            "Ahoy there wanderer!",
            "Greetings, stranger! You've found your way to the home of the finest blades and armor in the realm.",
            "Hello, friend! I'm the master of this forge.",
            "Well hello there! It's not often we get visitors.",
            "Greetings, honored guest! Step inside and let's see what we can create together."
        ]
        print(f"{self.name}: {random.choice(greetings)}")

    def askForNeeds(self, isPlayer):
        askForNeeds = [
            "What can I do for you today?",
            "What brings you here?",
            "How can I assist you?",
            "So, what are you looking for?",
            "What brings you to my forge today?",
            "What can I do for you today, weary traveler?",
            "Step right up and let me know how I can be of service.",
            "Need something forged or repaired?"
        ]
        print(f"{self.name}: {random.choice(askForNeeds)}")
        if(isPlayer):
            for i in range(len(self.itemList)):
                print(f"{i+1}. {self.itemList[i].name}")
          
    def showcaseItem(self,ID):
        print(f"Name: {self.itemList[ID].name}")
        print(f"Durability: {self.itemList[ID].durability}")
        print(f"Weight: {self.itemList[ID].weight}")
        print(f"Quality: {self.itemList[ID].quality}")
        print(f"Damage: {self.itemList[ID].damage}")
        return self.itemList[ID]
    
    def sellItem(self,buyer,ID):
        buyer.wealth -= self.itemList[ID].price
        self.itemAmount[ID] -= 1
  
        








#Set of Functions

def businessInteractionNPC(customer,merchant):
    merchant.greet()
    merchant.askForNeeds(isPlayer = False)
    itemDesired = random.choice(merchant.itemList)
    itemID = weaponList.index(itemDesired)
    
    print(f"{customer.name}: I would like a {itemDesired.name}")
    while (merchant.checkAvailability(itemID) == 0): #Possible infinite Loop if merchant isn't configured properly
        oldItemID = itemID
        ItemDesired = random.choice(weaponList)
        ItemID = merchant.itemList.index(ItemDesired)
    merchant.showcaseItem(itemID)  
    
    if(merchant.checkItemPrice(itemID) <= customer.wealth):
        customer.buyItem(itemDesired,merchant1)
    else:
        print(f"{customer.name}: Aww, guess I gotta save more money :(.")



#game loop

nat = human()
game_map = GameMap()
game_map.updateMap(nat)
game_map.printMap()
for time in range(1,10):
    nat.movement(game_map)
    game_map.updateMap(nat)
    game_map.printMap()
    