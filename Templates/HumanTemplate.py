import random

class item:
    def __init__(self,name):
        self.name = name
        self.durability = random.randint(1,10)
        self.weight = random.randint(1,10)
        self.quality = random.randint(1,10)
        self.damage = random.randint(1,10)
        self.price = random.randint(10,1000)

#Main

#Weapons
sword = item("Sword")
axe =   item("Axe")
bow =   item("Bow")
spear = item("Spear")
pistol= item("Pistol")

#Ammo
arrow = item("Arrow")
bullet= item("Bullet")


weaponList =    [sword, axe, bow, spear]
ammoList =      [arrow, bullet]


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
        
        self.generateInfo(random.randint(0,1))
        self.generateGF() 
        self.generateJob()
        self.generateTrait()
        self.generateTalents()
        self.generateNormalState()
        self.generateReputation()
        self.generateRelationship()
        self.generateLooks()
        self.generateSkills()

    def generateInfo(self,biology):
        if(biology == 1): #generating sex
            self.sex = "M"
            self.name = random.choice(human.names_M)
            #human.names_M.remove(self.name)
        else: 
            self.sex = "F"
            self.name = random.choice(human.names_F)
            #human.names_F.remove(self.name)

    def generateGF(self):
        self.MentalGF = random.randint(0,10)
        self.PhysicalGF = random.randint(0,10)
        
    def generateJob(self):
        self.job = random.choice(human.jobs)
        #if(self.job == "Mayor"):
            #human.jobs.remove(self.job)

    def generateTrait(self): #Type+Intensity
        for i in range(3): #Generate 3 random traits for the person
            randomTrait = random.choice(self.traitList)
            self.traits.append(randomTrait) 
            self.traitList.remove(randomTrait)
        
        #self.traitType = []
        #self.traitIntensity = []
        self.traitTarget = random.choice(["self","party"])

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
        
        #self.talentDomain = []
        #self.talentRank = []

    def generateNormalState(self):
        self.stress = random.randint(0,60)
        self.happiness = random.randint(0,80)
        self.health = 80

    #Home
    def generateReputation(self):
        self.charisma = random.randint(0,100)
        self.feats = []
        #self.home =  []
        self.wealth = random.randint(0,10**4)

    #Affection+Trust+Compatibility
    def generateRelationship(self):
        self.affection = []
        self.trust = []
        self.compatibility = []
    
    #Looks
    def generateLooks(self):
        #self.looks = []
        return
    
    #Skills + Level + Rank
    def generateSkills(self):
        self.skills = []
        self.skillLevel = []
        self.skillRank = []

    def buyItem(self,item,merchant):
        print(f"{self.name}: Hmm, okay then I'll buy it!")
        merchant.sellItem(self, merchant.itemList.index(item))

    #Getters
    def getSex(self):
        if(self.sex == "M"):
            return "Male"
        return "Female"

    def getTrait(self, index):
        return self.trait[index]

    def getName(self):
        return self.name

    def getJob(self):
        return self.job

    def getGrowthFactor(self,type):
        return self.growth_factor[type]

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
    



def businessInteractionNPC(customer,merchant):
    merchant.greet()
    merchant.askForNeeds(isPlayer = False)
    itemDesired = random.choice(weaponList)
    itemID = weaponList.index(itemDesired)
    newItemDesired = itemDesired
    newItemID = itemID
    print(f"{customer1.name}: I would like a {itemDesired.name}")
    while (merchant.checkAvailability(itemID) == 0): #Possible infinite Loop if merchant isn't configured properly
        newItemDesired = random.choice(weaponList)
        newItemID = merchant.itemList.index(newItemDesired)
        while(newItemID == itemID):
            newItemDesired = random.choice(weaponList)
            newItemID = merchant.itemList.index(newItemDesired)
        
        print(f"{customer.name}: oh.. then how about a {newItemDesired.name}?")
    itemDesired = newItemDesired
    itemID = newItemID
    merchant.showcaseItem(itemID)  
    if(merchant.checkItemPrice(itemID) <= customer.wealth):
        customer.buyItem(itemDesired,merchant1)
    else:
        print(f"{customer.name}: Aww, guess I gotta save more money :(.")


merchant1 = merchant(weaponList)
customer1 = human()
businessInteractionNPC(customer1,merchant1)


