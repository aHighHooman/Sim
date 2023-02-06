
#Test run

###conversations are made of multiple steps
# 1: Greeting //Can affect the mood of the blacksmith
# 2: "What can I help you with"   //Can be affected by the mood of the blacksmith 
# 3: I need X   //If item description is BS then P2 then P24
# 4: P1: Oh I have X //or something like X
# 5: Item Description provided
# 6: P11: You buy the item 
# 7: "Have a good day" //Mood & Relationship are affected
# End
# 8: P12: You don't buy the item
# 9: "Hmm"
# 10: P2: "Unfortunately I don't have anything (else) like X"
# 11: P21: "But you might like this item Y." // Go back to Step 5
# 12: P22: Smiling Ruefully "I make weapons like that but I'm just sold out, so may come back at a better time eh"
# End
# 16: P23: "Maybe check shops C and D, they might make the item"
# End
# 13: P24: "If you want, I can make the item but I may need materials" //Conditional on mood and relationship
# 14: P241: "Get me these materials along with material A and B for the payment" //Conditional on item quality and reationship
# End
# 15: P242: "Get me these materials and I'll make the item." //Conditional on item quality and reationship
# End ###



def convo():
    userInput = input("Hello: ")
    #Step 1 of the conversation
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