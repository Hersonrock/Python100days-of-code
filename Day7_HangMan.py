#Using random word API from
#   http://random-word-api.herokuapp.com/home
#    https://random-word-api.herokuapp.com/word
#Using "requests" , installed with command "pip install requests"
#   see: https://www.geeksforgeeks.org/get-post-requests-using-python/

import requests
randomWordURL = "https://random-word-api.herokuapp.com/word"
randomWordRAW = requests.get(url=randomWordURL)
randomWordStringRaw= randomWordRAW.text
randomWordString=randomWordStringRaw[2:-2]
print (randomWordString)
guessWord= []
lives=10
guessLetter=""
index = -1
hit= False
guessDone=""

for character in randomWordString:
    guessWord.append("_")

def update ():
    print(guessWord)
    print("Letters given: " + guessDone)
    print("Lives Remaining: "+ str(lives) )
    print("\n")


def solved():
    i=len(randomWordString)
    for character in guessWord:
        if character=="_":
            return False
        else:
            i -= 1
    if i==0:
        return True

print("Welcome to HangMan, will you guess in time?")
update()

while not solved() and lives!=0:
    guessLetter=input("Guess a letter: ")
    hit=False
   
    guessDone += guessLetter
    for randomWordLetter in randomWordString:
        index += 1
        if guessLetter == randomWordLetter:
            guessWord[index]=guessLetter
            hit=True
    if hit==False:
        lives -= 1
    index= -1
    update()



if solved():
    print("You Win!!!")
else:
    print("The word was "+ "".join(randomWordString))
    print("You Lose,try again")

