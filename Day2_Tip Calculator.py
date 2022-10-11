
print("Welcome to the tip calculator.")
totalBill=float(input("What was the total bill? $"))
percentage=float(input("What percentage tip would you like to give? 10, 12, or 15?"))
peopleToSplit=int(input("How many people to split the bill?"))
totalPay=totalBill*(percentage/100+1)
payEach="{:.2f}".format(totalPay/peopleToSplit)

message=f"Each person should pay: ${payEach}"
print(message)