import random as rand
import time

speed = 0.05

swordList = ["Long Sword", "Broadsword", "Shortsword", "Rapier", "Estoc"]

#utility functions
def type(input, typeSpeed = speed, speaker = False):
    if(not speaker):
        print("- ", end = "", flush = True)
    for char in input:
        print(char, end = "", flush = True)
        time.sleep(typeSpeed)
    print("\n", end = "", flush = True)


#conversational functions 
def greetCustomer():
    greetings = ["Hello there", "Greetings Customer", "..."]
    num = rand.randint(0,len(greetings)-1)
    type(greetings[num])

def askForNeeds():
    phrases = ["What do you need today","How can I help you today","Whaddya need","Looking for something?"]
    num = rand.randint(0,len(phrases)-1)
    type(phrases[num])


#process functions
def checkAvailability(ID):
    if (ID == 6):
        type("Unfortunately I do not have any other selections right now.")
    else:
        type(f"Oh I have a {swordList[ID]}")
    
def showcaseWeapon(ID):
    if (ID == 1 or ID == 2 or ID == 3):
        type(f"This {swordList[ID]} will cost 5 gold.")
    elif(ID == 4):
        type("This was on of my favorite ones to work on... it costs 8 gold.")
    elif(ID == 5):
        type(f"The {swordList[ID]} costs 7 gold")


#main
greetCustomer() #Greet the player can change depending on the mood
askForNeeds()

type("I need a: \n1: Long Sword \n2: Broadsword\n3: Shortsword\n4: Rapier\n5: Estoc\n6: Other", typeSpeed=0.01, speaker=True)
val = int(input())
while(val > 6 or val < 1):
    val = int(input("I need a: \n1. Long Sword \n2. Broadsword\n3. Shortsword\n4. Rapier\n5. Estoc\n6. Other"))

checkAvailability(val-1)
if(not(val == 6)):
    showcaseWeapon(val-1)
#else:
    #Apoligies of sorts