import random as rand



#conversational functions 
def greetCustomer():
    greetings = ["Hello there", "Greetings Customer", "..."]
    num = rand.randint(0,len(greetings)-1)
    print(greetings[num])

def askForNeeds():
    phrases = ["What do you need today","How can I help you today","Whaddya need","Looking for something?"]
    num = rand.randint(0,len(phrases)-1)
    print(phrases[num])


#process functions
def checkWeaponType(list):
    ### Sword : {Sword,Estoc,Rapier,greatsword}
    swords = ["sword","estoc","rapier","greatsword"]
    for i in swords:
        if(i in list):
            return i
    return "none"

def checkSwordType(weaponType,uInput):
    if(weaponType == "sword"):
        if ("long" in uInput):
            return "long sword"
        elif("short" in uInput):
            return "short"
        elif("broad" in uInput):
            return "broad sword"
        else:
            return "sword"
    elif(weaponType == "rapier"):
        return weaponType
    elif(weaponType == "estoc"):
        return weaponType
    else:
        return "none"
    


#main
greetCustomer() #Greet the player can change depending on the mood
askForNeeds()

val = input("I need a: ")
userInput = val.split(" ")

if(len(userInput) <= 2):
    weaponType = checkWeaponType(userInput)
    swordType = checkSwordType(weaponType,userInput)
    if(swordType == "none"):
            print(f"Unfortunately I do not have a {val}")
    else:
            print(f"Oh I do have a {val}")
else:
    print(f"Unfortunately I do not have a '{val}'")