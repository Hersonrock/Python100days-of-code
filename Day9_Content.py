programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", 
"Function": "A piece of code that you can easily call over and over again.",
"Loop": "The action of doing something over and over again."},

# Python dictionaries need to be strings.

#Retrieving items from dictionary.
print(programming_dictionary["Function"])

#Adding new items to dictionary.
programming_dictionary["Variable"]="A container for data."

#Create an empty dictionary.
empty_dictionary = {}

#Wipe an existing dictionary
# programing_dictionary= {}


#Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer"

#Loop trough a dictionary
for thing in programming_dictionary:
    print(thing)
# This will give me just the keys
    print(programing_dictionary[key])