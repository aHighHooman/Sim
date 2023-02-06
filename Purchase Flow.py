import random

def checkWeaponType(list):
    ### Sword : {Sword,Estoc,Rapier,greatsword}
    swords = ["sword","estoc","rapier","greatsword"]
    for i in swords:
        if(i in list):
            return i
    return "none"

def greetCustomer():
    greetings = ["Hello there", "Greetings Customer", "..."]
    num = random.randint(0,len(greetings)-1)
    print(greetings[num])

def checkSwordType(weaponType,uInput):
    if(weaponType == "sword"):
        if ("long" in uInput):
            return "long sword"
        elif("short" in uInput):
            return "short"
        elif("broad" in uInput):
            return "broad sword"
        else:
            return "none"
    elif(weaponType == "rapier"):
        return weaponType
    elif(weaponType == "estoc"):
        return weaponType
    else:
        return "none"
    


#main
greetCustomer()
print("What can I help you with?")

val = input("I need a: ")
userInput = val.split(" ")
print(userInput)
if(len(userInput) <= 2):
    weaponType = checkWeaponType(userInput)
    swordType = checkSwordType(weaponType,userInput)
    if(swordType == "none"):
            print(f"Unfortunately I do not have a {val}")
    else:
            print(f"Oh I do have a {val}")
else:
    print(f"Unfortunately I do not have a '{val}'")