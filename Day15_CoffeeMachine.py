
coffee_dic= {
    # name : [price (cents),water(ml),coffee(g),milk(ml)]
    "espresso"  : {"price":150, "water":50 , "coffee":18, "milk":0},
    "latte"     : {"price":250, "water":200, "coffee":24, "milk":150},
    "cappuccino": {"price":300, "water":250, "coffee":24, "milk":100},
}

#resources [water,coffee,milk]
starting_resources=[300, 100, 200]
coin_worth={
    "penny": 1,
    "nickel": 5,
    "dime": 10,
    "quarter": 25
}

#I need to print a report, what resources it has left.
machine_on=True
order_requested=False

def report():
    
    print( f"Water={starting_resources[0]}")
    print( f"Coffee={starting_resources[1]}")
    print( f"Milk={starting_resources[2]}")

def enough_resources(choice):

    if coffee_dic[choice]["water"] > starting_resources[0]:
        print("There is not enough Water for this option, Try again")
        return False
    elif coffee_dic[choice]["coffee"] > starting_resources[1]:
        print("There is not enough Coffee for this option, Try again")
        return False
    elif coffee_dic[choice]["milk"] > starting_resources[2]:
        print("There is not enough Milk for this option, Try again")
        return False
    return True

while machine_on:

    while not order_requested:
        choice=input("What would you like? \(espresso\/latte\/cappuccino\): ").lower()
        if choice=="report":
            report()
        elif choice=="espresso" or choice== "latte" or choice =="cappuccino":
            order_requested=True
            if enough_resources(choice):
               print("Processing order")
            
        elif choice=="off":
            machine_on= False
            break
        else:
            print("Invalid Choice, Try again")
    #Refresh for new order.
    order_requested=False

    # # It should check resources before asking for coins.
    # print("Sorry there is not enough X, try another option")

    # # ask for inputs
    # input("How many quarters?: ")
    # input("How many dimes?: ")
    # input("How many nikels?: ")
    # input("How many pennies?: ")
    # print("Sorry that's not enough money. Money refunded.")

    # #provides change
    # print(f"Here is your {change} in change.")

    # #bye
    # print("Here is your latte Enjoy!")
