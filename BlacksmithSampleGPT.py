class Blacksmith():
    def __init__(self):
        self.items = {"sword": 50, "armor": 100, "shield": 75}

    def welcome(self):
        print("Welcome to the blacksmith's shop! I am the blacksmith, what can I do for you today?")

    def list_items(self):
        print("Here is a list of items I have for sale:")
        for item, price in self.items.items():
            print(f"{item}: {price} gold")

    def buy_item(self, item, gold):
        if item in self.items:
            if gold >= self.items[item]:
                print(f"Thank you for buying the {item}! Enjoy your purchase.")
                return self.items[item]
            else:
                print("You do not have enough gold.")
        else:
            print("I'm sorry, we do not have that item.")
            return None

    def make_item(self, item, gold):
        if item in self.items:
            if gold >= self.items[item]:
                print(f"I will make you a {item} and it will cost {self.items[item]} gold.")
                return self.items[item]
            else:
                print("You do not have enough gold.")
        else:
            print("I'm sorry, I cannot make that item.")
            return None

blacksmith = Blacksmith()
blacksmith.welcome()
blacksmith.list_items()

item = input("What item would you like to buy or make? ")
gold = int(input("How much gold do you have? "))

cost = blacksmith.buy_item(item, gold)
if cost:
    gold -= cost
    print(f"You have {gold} gold left.")

cost = blacksmith.make_item(item, gold)
if cost:
    gold -= cost
    print(f"You have {gold} gold left.")