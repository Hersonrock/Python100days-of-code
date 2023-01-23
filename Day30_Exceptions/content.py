try:   #Code to be tried.
    file=open("a_file.txt")
    a_dictionary={"key": "value"}
    print(a_dictionary["fasdfa"])
except FileNotFoundError:   #Runs when there is a FileNotFoundError
    file=open("a_file.txt","w")
    file.write("Something")
except KeyError as error_message:  # Runs when there is a KeyError
    print(f"The Key {error_message} does not exist")
else:  #Runs when try succedds
    content=file.read()
    print(content)
finally:  #Runs regardless of try success
    file.close()
    print("file was closed")



#Raise your own exceptions

height= float(input("Height: "))
weight= int(input("Weight: "))

if height>3:
    raise ValueError("Human Height should not be over 3 meters.")  # this will create a a ValueError that can be caught by an exception block. 

bmi= weight / height ** 2
print(bmi)