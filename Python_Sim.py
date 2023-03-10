import random


class Trait():
    def __init__(self):
        self.traitList = ["Heroic", "Will to Live", "Cool Headed", "Observant", "Coward", "Curious", "Prideful", "Prepared"]

    def getRandomTrait(self):
        index = random.randint(0, len(self.traitList) - 1)
        trait = self.traitList[index]
        self.traitList.remove(self.traitList[index])
        return trait




class human:
    names_M = ["Liam", "Oliver", "Noah", "Elijah", "William", "James", "Benjamin", "Lucas"]
    names_F = ["Olivia", "Emma", "Charlotte", "Amelia", "Ava", "Sophia", "Isabella", "Mia"]
    jobs = ["Party Leader", "Blacksmith", "Trainer", "Mayor", "Adventurer", "Hunter", "Alchemist"]


    
    def __init__(self): 
        self.trait_dic = Trait()        
        self.combat_talents = ["Sword", "Spear", "Dagger", "Archer", "Gunsman", "Large Mana", "Elemental Affinity", "Intruition", "Camouflage", "Artillery Load", "Scouting", "Ambidextrous"]
        self.generalist_talents = ["Management", "High Adaptability", "High Charisma", "Quick Learner", "Creative", "Large Build","Blacksmithing", "Farmer", "Builder", "Engineer", "Cook"]
        self.talent = []
        self.trait = []
        
        #generating name + sex
        self.generateName()

        #generating growth factor
        self.generateGF() 

        #generating job
        self.generateJob()

        #generating traits
        self.generateTrait()

        #generating talents
        self.generateTalents()
        


    #generator functions
    def generateJob(self):
        self.job = human.jobs[random.randint(0,len(human.jobs) - 1)] #Generating Job
        if(self.job == "Mayor"):
            human.jobs.remove(self.job)

    def generateTrait(self):
        i = 0 
        while(i < 3):
            self.trait.append(self.trait_dic.getRandomTrait())
            i += 1

    def generateName(self):
        if(random.randint(0,1) == 1): #generating sex
            self.sex = "M"
            self.name = human.names_M[random.randint(0, len(human.names_M) - 1)]
            human.names_M.remove(self.name)
        else: 
            self.sex = "F"
            self.name = human.names_F[random.randint(0, len(human.names_F) - 1)]
            human.names_F.remove(self.name)
    
    def generateGF(self):
        self.MGF = random.randint(0,10)
        self.PGF = random.randint(0,10)
        self.growth_factor = [self.MGF,self.PGF] #Mental,Physical

    def generateTalents(self):
        i = True
        while(i == True):
            domain = random.randint(1,2)
            num = random.uniform(0,1)
            if(domain == 1): #if you get combat talents
                if(num < (len(self.talent) + 1)**(-1)):
                    typeA = self.combat_talents[random.randint(0, len(self.combat_talents) - 1)]
                    self.talent.append(typeA)
                    self.combat_talents.remove(typeA)
                    continue
            elif(domain == 2): # if you get generalist talents
                if(num < (len(self.talent) + 1)**(-1)):
                    typeB = self.generalist_talents[random.randint(0, len(self.generalist_talents) - 1)]
                    self.talent.append(typeB)
                    self.generalist_talents.remove(typeB)
                    continue
            i = False

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




# main 
humanList = []
i = 0
while (i < 9):
    humanList.append(human())
    print(f"Name: {humanList[i].getName()}")
    print(f"Sex: {humanList[i].getSex()}")
    print(f"Job: {humanList[i].getJob()}")
    print(f"P.G.F.: {humanList[i].getGrowthFactor(1)}   M.G.F.: {humanList[i].getGrowthFactor(0)} \n")
    i += 1
    