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