class item:
    def __init__(self, itemType, classType, useType, price):
        self.effectiveness = 0                  #amount of (useType) item does
        self.attributes = 0                     #special effects of using the weapon
        self.durability = 0                     #durability
        self.modifier = ""                      #description about weapon make and if its 'named'
        
        self.itemType = itemType
        self.classType = classType              #user type
        self.useType  = useType                 #protection, damage, healing, buff/debuff
        self.name = self.modifier + self.itemType   #full weapon name
        self.price = price


#Main

#Weapons
sword = item("sword", "c", "weapon", 10)
axe =   item("axe", "c", "weapon", 8)
bow =   item("bow", "c", "weapon", 11)
spear = item("bow", "c", "weapon", 13)
pistol= item("pistol", "c", "weapon", 17)

#Ammo
arrow = item("arrow", "c", "ammo", 1)
bullet= item("bulles", "c", "ammo", 1)


weaponList =    [sword, axe, bow, spear]
ammoList =      [arrow, bullet]