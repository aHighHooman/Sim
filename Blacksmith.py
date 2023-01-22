
#Test run
def convo():
    userInput = input("Hello: ")
    if(userInput == 'd'):
        print("- You greet the blacksmith calmly")
        print("- The blacksmith sends a smile your way")
        print("- 'Hello there lad, whaatcha looking for in this humble smithy.'")
    elif(userInput == 'w'):
        print("- You meet the blacksmith with an air of authority")
        print("- The blacksmith frowns looking at you")
        print("- 'May I know who you are and what brings you to this crickety shop?'")
    elif(userInput == 'a'):
        print("- You give a rushed greeting to the blacksmith")
        print("- The blacksmith's eyebrows rise up in curiosity")
        print("- 'What's wrong boy, for you to be in such a rush'\n")

#Test 
print ("Hello World")
convo()