# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1Lower = name1.lower()
name2Lower = name2.lower()

true = name1Lower.count("t")+name1Lower.count("r")+name1Lower.count("u")+name1Lower.count("e")+name2Lower.count("t")+name2Lower.count("r")+name2Lower.count("u")+name2Lower.count("e")

love = name1Lower.count("l")+name1Lower.count("o")+name1Lower.count("v")+name1Lower.count("e")+name2Lower.count("l")+name2Lower.count("o")+name2Lower.count("v")+name2Lower.count("e")

trueLove= int(f"{true}{love}")

if trueLove <10 or trueLove > 90:
    print(f"Your score is {trueLove}, you go together like coke and mentos.")
elif trueLove > 40 and trueLove < 50:
    print(f"Your score is {trueLove}, you are alright together.")
else:
    print(f"Your score is {trueLove}.")
