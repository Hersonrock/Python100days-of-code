

mode=""
outputMessage=""
continueCipherstr="no"
continueCipher=True

def encodeMessage():
    inputMessage=input("Type your messsage: ").lower()
    shiftNumber=int(input("Type the shift number: "))
    shifter(inputMessage,shiftNumber)
    print("Here's the encoded result: "+outputMessage)

def decodeMessage():
    inputMessage=input("Type your messsage: ").lower()
    shiftNumber=int(input("Type the shift number: "))
    shifter(inputMessage,-shiftNumber)
    print("Here's the decoded result: "+ outputMessage)

def continueGameQuestion():
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
        charOrder= ord(message[i-2:i-len(message)-1])+shiftNumber
        print(message[i-1:i-len(message)]+ " world")
        while charOrder < 97 :
            charOrder += 26  #123-97
        while charOrder > 122:
            charOrder -= 26  #123-97e

    
        outputMessage += chr(charOrder)



while continueCipher:
    
    mode=input("Type \'encode\' to encrypt, type \'decode\' to decrypt: ").lower()
    if mode=="encode":
        encodeMessage()
    elif mode=="decode":
        decodeMessage()
    else:
        print("Wrong input")
    outputMessage=""
    continueGameQuestion()
    
