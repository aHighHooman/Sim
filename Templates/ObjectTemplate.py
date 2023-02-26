class item:
    def __init__(self, type, classType, useType):
        self.type = type
        self.classType = classType              #user type
        self.useType  = useType                 #protection, damage, healing, buff, debuff
        self.name = self.modifier + self.type   #full weapon name
        self.effectiveness = 0                  #amount of (useType) item does
        self.attributes = 0                     #special effects of using the weapon
        self.durability = 0                     #durability
        self.modifier = ""                      #description about weapon make and if its 'named'


#Main

#Weapons
sword = item("sword", "c", "weapon")
axe =   item("axe", "c", "weapon")
bow =   item("bow", "c", "weapon")
spear = item("bow", "c", "weapon")
pistol= item("pistol", "c", "weapon")

#Ammo
arrow = item("arrow", "c", "ammo")
bullet= item("bulles", "c", "ammo")


weaponList =    [sword, axe, bow, spear]
ammoList =      [arrow, bullet]