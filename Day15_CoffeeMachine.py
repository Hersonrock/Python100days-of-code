
coffee_dic= {
    # name : [price (cents),water(ml),coffee(g),milk(ml)]
    "espresso"  : {"price":150, "water":50 , "coffee":18, "milk":0},
    "latte"     : {"price":250, "water":200, "coffee":24, "milk":150},
    "cappuccino": {"price":300, "water":250, "coffee":24, "milk":100},
}

#resources [water,coffee,milk]
avail_resources=[300, 100, 200]

COIN_WORTH={
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

def process_coins(choice):
    pennies=int(input("How many pennies?: "))
    nickels= int(input("How many nickels?: "))
    dimes= int(input("How many dimes?: "))
    quarters= int(input("How many quarters?: "))
    
    total= pennies*COIN_WORTH["penny"]+nickels*COIN_WORTH["nickel"]+dimes*COIN_WORTH["dime"]+quarters*COIN_WORTH["quarter"]

    if total >= coffee_dic[choice]["price"]:
        return total
    else:
        print("Sorry that's not enough money. Money refunded.")
        return -1


while machine_on:

    while not order_requested:
        choice=input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choice=="report":
            report()
        elif choice=="espresso" or choice== "latte" or choice =="cappuccino":
            #Here the main order will be processed.
            order_requested=True
            if enough_resources(choice):
                avail_resources=remaining_resources(choice)
                money_input_raw=process_coins(choice)
                if  money_input_raw != -1:
                    change_raw= money_input_raw- coffee_dic[choice]["price"]
                    #Building strings after handling amounts in cents.
                    money_input_str= f"{money_input_raw//100}.{money_input_raw%100}"
                    change_str=f"{change_raw//100}.{change_raw%100}"
                    print(f"Money Inserted $"+money_input_str)
                    print(f"Your change is $"+change_str)
                    
                           
        elif choice=="off":
            machine_on= False
            break
        else:
            print("Invalid Choice, Try again")
    #Refresh for new order.
    order_requested=False


print("Turning off...")

    # #provides change
    # print(f"Here is your {change} in change.")

    # #bye
    # print("Here is your latte Enjoy!")
