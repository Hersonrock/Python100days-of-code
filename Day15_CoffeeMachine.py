


coffee_dic= {
    # name : [price (cents),water(ml),coffee(g),milk(ml)]
    "expresso"  : {"price":150, "water":50 , "coffee":18, "milk":0},
    "latte"     : {"price":250, "water":200, "coffee":24, "milk":150},
    "cappuccino": {"price":300, "water":250, "coffee":24, "milk":100},
}

#resources [water,coffee,milk]
starting_resources=[300,100,200]
coin_worth={
    "penny": 1,
    "nickel": 5,
    "dime": 10,
    "quarter": 25
}

#I need to print a report, what resources it has left.

input("What would you like? \(espresso\/latte\/cappuccino\): ")

# It should check resources before asking for coins.
print("Sorry there is not enough X, try another option")

# ask for inputs
input("How many quarters?: ")
input("How many dimes?: ")
input("How many nikels?: ")
input("How many pennies?: ")
print("Sorry that's not enough money. Money refunded.")

#provides change
print(f"Here is your {change} in change.")

#bye
print("Here is your latte Enjoy!")
