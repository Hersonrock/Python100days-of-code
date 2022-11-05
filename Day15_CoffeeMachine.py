
coffee_dic= {
    # name : [price (cents),water(ml),coffee(g),milk(ml)]
    "espresso"  : {"price":150, "water":50 , "coffee":18, "milk":0},
    "latte"     : {"price":250, "water":200, "coffee":24, "milk":150},
    "cappuccino": {"price":300, "water":250, "coffee":24, "milk":100},
}

#resources [water,coffee,milk]
avail_resources=[300, 100, 200]

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
    
    print( f"Water\t=\t{avail_resources[0]}")
    print( f"Coffee\t=\t{avail_resources[1]}")
    print( f"Milk\t=\t{avail_resources[2]}")

def enough_resources(choice):

    if coffee_dic[choice]["water"] > avail_resources[0]:
        print("There is not enough Water for this option, Try again")
        return False
    elif coffee_dic[choice]["coffee"] > avail_resources[1]:
        print("There is not enough Coffee for this option, Try again")
        return False
    elif coffee_dic[choice]["milk"] > avail_resources[2]:
        print("There is not enough Milk for this option, Try again")
        return False
    return True

def remaining_resources(choice):
    consumed=[
        avail_resources[0]-coffee_dic[choice]["water"],
        avail_resources[1]-coffee_dic[choice]["coffee"],
        avail_resources[2]-coffee_dic[choice]["milk"]
    ]
    return consumed


while machine_on:

    while not order_requested:
        choice=input("What would you like? \(espresso\/latte\/cappuccino\): ").lower()
        if choice=="report":
            report()
        elif choice=="espresso" or choice== "latte" or choice =="cappuccino":
            order_requested=True
            if enough_resources(choice):
                avail_resources=remaining_resources(choice)
                print("Processing order")
            
        elif choice=="off":
            machine_on= False
            break
        else:
            print("Invalid Choice, Try again")
    #Refresh for new order.
    order_requested=False


print("Turning off...")


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
