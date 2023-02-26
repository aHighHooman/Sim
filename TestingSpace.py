import random
import time
from Templates.HumanTemplate import human
slowness = 0.01

def type(input, typeSpeed = slowness, speaker = False):
    if(not speaker):
        print("- ", end = "", flush = True)
    for char in input:
        print(char, end = "", flush = True)
        time.sleep(typeSpeed)
    print("\n", end = "", flush = True)

#A combatant can be described by a few numbers:
#- HP
#- OnBattle Mental State = {Excitement, Confidence}
#- OnBattle Physical State = {Strength, Agility, Vitality, Exhaustion, Affliction}
#- Attack = {Type, Damage}
#- Dodge Chance/%
#- Block Chance/%

class combatant(human):
    def __init__(self):
        self.M_onBattle = {"exc": 0, "con": 0}
        self.P_onBattle = {"str": 0, "agi": 0, "vit": 0, "exh": [0,0], "aff": 0}
        self.generate()
        self.generateStats()
        self.initiatePhrase()
        self.wounded = False
        print(f"Name = {self.name}\n")
        print(f"HP = {self.hp}\n")
        print(f"Damage = {self.dmg[1]}\n")
     
    def generateStats(self):
        #strength based stats
        self.P_onBattle["str"] = random.randint(0,10)
        self.dmg = ["type", self.P_onBattle["str"]]
        
        #agility based
        self.P_onBattle["agi"] = random.randint(0,10)
        self.blockChance = self.P_onBattle["agi"] / 30
        self.dodgeChance = self.P_onBattle["agi"] / 90

        #HP based stats
        self.P_onBattle["vit"] = random.randint(5,10)
        self.hp = 10 * self.P_onBattle["vit"]
        return
    
    def initiatePhrase(self):
        self.attackPhrase = [" attacked ", f" swung {self.pronoun[1]} fist at ", " did an upper cut to "]
        return

    def attack(self, target): #attacking another combatant
        num = random.randint(0,len(self.attackPhrase)-1)
        type(f"{self.name} {self.attackPhrase[num]} {target.name}")
        num = random.randint(0,1)
        damage = self.dmg[1]
        if(damage <= 3): #If the attacker is too exhausted
            damage += random.randint(0,3)
        else:
            if num == 0:
                damage -= random.randint(0,3)
            else:
                damage += random.randint(0,3)
        self.checkExhaustion()
        self.P_onBattle["exh"][0] += random.randint(5,10)# add exhaustion
        
        target.reduceHP(self, damage)  
        return 
        
    def reduceHP(self,attacker, inputDamage): #If attacked by another combatant
        num = random.random()
        damageTaken = inputDamage
        
        if(num <= 0.3):     #If dodged or blocked
            if(num < 0.1):  #If dodged
                damageTaken = 0;
                type(f"{self.name} dodged\n")

            else:           #If Blocked
                damageTaken = int((damageTaken/0.2 * num - damageTaken/2)*10) / 10
                if(damageTaken == 0): #If the opponent is too exhausted
                    type(f"{self.name} didn't get hurt from the attack\n")
                else:
                    if(damageTaken >= 0.5*inputDamage):
                        type(f" {self.name} blocked some of the damage.\n")
                    else:
                        type(f" {self.name} blocked most of the damage.\n")
        
        else:               #If struck
            if(damageTaken == 0): #If the opponent is too exhausted
                type(f"{self.name} didn't get hurt from the attack\n")
            else:
                type(f"{self.name} got struck by the blow\n")
        self.hp -= damageTaken

        
        if(self.hp <= 0): #If dead
            type(f"As {self.name} got hit by a fatal blow, {self.pronoun[0]} fell flat to the ground.")
            type(f"Next time' {self.pronoun[0]} said as {self.pronoun[1]} eyes slowly lost their shimmer", 0.1)
            self.alive = False
        
        elif(self.hp <= 15 and (not self.wounded)): #If severely wounded
            type(f"{self.name} started to stumble as a pool of blood gathered beneath {self.pronoun[0]} feet", 0.03)
            type(f"'not... yet I can win, I WILL win'\n", 0.09)
            self.attack(attacker)
            self.wounded = not self.wounded

    def checkExhaustion(self):
        if((self.P_onBattle["exh"][0] >= 95) and (self.P_onBattle["exh"][1] < 4)):    #If incapable of fighting 
            type(f"{self.name} tried to move {self.pronoun[1]} sword but it wouldn't move {self.pronoun[1]} arms wouldn't move no matter... how much she tried.",0.05)
            type(f"Please don't do this to me... not now .. please not now", 0.08)
            self.dmg[1] = 0 * self.dmg[1]
            self.P_onBattle["exh"][1] += 1

        elif((self.P_onBattle["exh"][0] >= 90) and (self.P_onBattle["exh"][1] < 3)):  #If extremely exhausted
            type(f"Exhaustion had finally started to catch on to {self.name}'s body.",0.05)
            type(f"{self.pronoun[1]} eyes started to close on themselves as {self.pronoun[1]} strength and speed plummeted",0.04)
            self.dmg[1] = 0.1 * self.dmg[1]
            self.P_onBattle["exh"][1] += 1

        elif((self.P_onBattle["exh"][0] >= 75) and (self.P_onBattle["exh"][1] < 2)):  #If Moderately exhausted
            type(f"{self.name}'s arms were now sore from swinging and {self.pronoun[1]} bones rattled every time collided against his opponent",0.03)
            self.dmg[1] = 0.5 * self.dmg[1]
            self.P_onBattle["exh"][1] += 1

        elif((self.P_onBattle["exh"][0] >= 60) and (self.P_onBattle["exh"][1] < 1)):  #If slightly exhausted
            type(f"A slight ache and fatigue started tugging on {self.name}'s body",0.02)
            self.dmg[1] = 0.80 * self.dmg[1]
            self.P_onBattle["exh"][1] += 1

        






#Main
player1 = combatant()
player2 = combatant()

print(f"{player1.name} will fight {player2.name} to the death")
while (player1.alive and player2.alive):
    num = random.randint(1,2)
    if(num == 1):
        player1.attack(player2)
    else:
        player2.attack(player1)
