import random
class combatant():
    def __init__(self,name, M_onBattle, P_onBattle ,damage):
        self.hp = 100
        self.M_onBattle = M_onBattle
        self.P_onBattle = P_onBattle
        self.dmg = ["Type", damage]
        self.blockChance = 0.3
        self.dodgeChance = 0.1
    
    def attack(self, target):
        target.reduceHP(self.dmg)
        return
        
    def reduceHP(self,inputDamage):
        num = random.random()
        damageTaken = inputDamage[1]
        if(num <= 0.3):
            if(num < 0.1):
                damageTaken = 0;
            else:
                damageTaken = damageTaken/0.2 * num - damageTaken
        self.hp -= damageTaken