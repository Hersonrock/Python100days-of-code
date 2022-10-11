# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

maxAge=90
realAge=int(age)
yearLeft=maxAge-realAge
monthsLeft=yearLeft*12
weeksLeft=yearLeft*52
daysLeft=yearLeft*365

message=(f"You have {daysLeft} days, {weeksLeft} weeks, and {monthsLeft} months left.")

print(message)
#Write your code below this line 👇