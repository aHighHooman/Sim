class NPC:
    def __init__(self, name, relationship_status, happiness, stress, physical_health):
        self.name = name
        self.relationship_status = relationship_status
        self.happiness = happiness
        self.stress = stress
        self.physical_health = physical_health
    
    def update_relationship_status(self, new_status):
        self.relationship_status = new_status
        print(self.name + " is now " + new_status)
        
    def update_happiness(self, new_happiness):
        self.happiness = new_happiness
        print(self.name + "'s happiness level is now " + str(new_happiness))
        
    def update_stress(self, new_stress):
        self.stress = new_stress
        print(self.name + "'s stress level is now " + str(new_stress))
        
    def update_physical_health(self, new_health):
        self.physical_health = new_health
        print(self.name + "'s physical health level is now " + str(new_health))

NPC1 = NPC("Bob", "single", 75, 20, 90)
print(NPC1.name + " is " + NPC1.relationship_status + " with a happiness level of " + str(NPC1.happiness) + ", a stress level of " + str(NPC1.stress) + " and a physical health level of " + str(NPC1.physical_health))

NPC1.update_relationship_status("in a relationship")
NPC1.update_happiness(90)
NPC1.update_stress(10)
NPC1.update_physical_health(80)