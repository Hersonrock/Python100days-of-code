

mode=""
outputMessage=""
continueCipherstr="no"
continueCipher=True

def encodeMessage():
    inputMessage=input("Type your messsage: ")
    shiftNumber=input("Type the shift number: ")
    print("Here's the encoded result: "+outputMessage)

def decodeMessage():
    inputMessage=input("Type your messsage: ")
    shiftNumber=input("Type the shift number: ")
    print("Here's the decoded result: "+outputMessage)

def continueGameQuestion():
    continueCipherstr=input("Type \'yes\' if you want to go again. Otherwise type \'no\': ")
    if continueCipherstr.lower()=="no":
        continueCipher=False
    elif continueCipherstr.lower()=="yes":
        continueCipher=True

while continueCipher:
    mode=input("Type \'encode\' to encrypt, type \'decode\' to decrypt: ").lower()
    if mode=="encode":
        encodeMessage()
    elif mode=="decode":
        decodeMessage()
    else:
        print("Wrong input")
    continueGameQuestion()
    
