

mode=""
outputMessage=""
continueCipherstr="no"
continueCipher=True
#97=a ,122=z
def encodeMessage():
    inputMessage=input("Type your messsage: ").lower()
    shiftNumber=input("Type the shift number: ")
    print("Here's the encoded result: "+outputMessage)

def decodeMessage():
    inputMessage=input("Type your messsage: ").lower()
    shiftNumber=input("Type the shift number: ")
    print("Here's the decoded result: "+outputMessage)

def continueGameQuestion():
    continueCipherstr=input("Type \'yes\' if you want to go again. Otherwise type \'no\': ")
    if continueCipherstr.lower()=="no":
        continueCipher=False
    elif continueCipherstr.lower()=="yes":
        continueCipher=True

def shifter(shiftNumber):


while continueCipher:
    mode=input("Type \'encode\' to encrypt, type \'decode\' to decrypt: ").lower()
    if mode=="encode":
        encodeMessage()
    elif mode=="decode":
        decodeMessage()
    else:
        print("Wrong input")
    continueGameQuestion()
    
