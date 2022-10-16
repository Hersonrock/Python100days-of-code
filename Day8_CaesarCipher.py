

mode=""
outputMessage=""
continueCipherstr="no"
continueCipher=True
inputMessage=""
shiftNumber=0

def continueGameQuestion():
    global continueCipher
    continueCipherstr=input("Type \'yes\' if you want to go again. Otherwise type \'no\': ")
    if continueCipherstr.lower()=="no":
        continueCipher=False
    elif continueCipherstr.lower()=="yes":
        continueCipher=True

def shifter(message,shiftNumber):
    #Will work using ASCII
    # 97=a ,122=z
    
    global outputMessage
    for i in range(1,len(message)+1):
        charOrder= ord(message[i-1])+shiftNumber
        if charOrder!= 32 + shiftNumber:
            while charOrder < 97 :
                charOrder += 26  #123-97
            while charOrder > 122:
                charOrder -= 26  #123-97
        else:
            charOrder=32
        outputMessage += chr(charOrder)

while continueCipher:
    outputMessage=""
    mode=input("Type \'encode\' to encrypt, type \'decode\' to decrypt: ").lower()


    if mode=="encode":
        inputMessage=input("Type your messsage: ").lower()
        shiftNumber=int(input("Type the shift number: "))
        shifter(inputMessage,shiftNumber)
    elif mode=="decode":
        inputMessage=input("Type your messsage: ").lower()
        shiftNumber=int(input("Type the shift number: "))
        shifter(inputMessage,-shiftNumber)
    else:
        print("Wrong input")
    print("Here's the encoded result: "+outputMessage)
    
    continueGameQuestion()

print("Good Bye")