# String immutability
#Strings are immutable in nature so we can reassign a variable to a new string but we can’t make any changes in the string.

name = "Maria"
print(f"Name last letter is {name[-1]}")

# Attempting to change the last letter will give an error
# name[-1]="o"
#TypeError: 'str' object does not support item assignment 

# Any operation that appears to modify a string actually creates a new string object. 
# This is because Python strings are immutable, and the original string object cannot be changed directly.


#-----------------------
#An example of a mutable object would be a list

ages=[20,30,40]
print(f"The first age is {ages[0]}")

ages[0]="45"
print(f"Now the frist age is {ages[0]}")

#lists can also be constructed using a "list constructor"

ages2=list(range(10))
print(f"The type of ages2 is: {type(ages2)}")
print(f"ages2 contains {ages2}")

#-----------------------
# Tuples are also inmmutable, same as strings.

coordinates=(20,3,51)
print(f"The first coordinate is {coordinates[0]}")
# coordinates[0]=32
#Attempting to make this new assigment will give an error.
# TypeError: 'tuple' object does not support item assignment

#-----------------------

