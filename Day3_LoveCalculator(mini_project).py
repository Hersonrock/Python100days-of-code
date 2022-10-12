# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

namesLower = name1.lower() + name2.lower()


true = namesLower.count("t")+namesLower.count("r")+namesLower.count("u")+namesLower.count("e")

love = namesLower.count("l")+namesLower.count("o")+namesLower.count("v")+namesLower.count("e")

trueLove= int(f"{true}{love}")

if trueLove <10 or trueLove > 90:
    print(f"Your score is {trueLove}, you go together like coke and mentos.")
elif trueLove > 40 and trueLove < 50:
    print(f"Your score is {trueLove}, you are alright together.")
else:
    print(f"Your score is {trueLove}.")
