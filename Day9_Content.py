from importlib.abc import Traversable


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
print(programming_dictionary["key"])

#You can have lists as inside a dictionary, this is "Nesting"
travel_log = {
    "France": ["Paris", "Lille", "Dijon"]
}

#You can also have dictionaries within dictionaries.

travel_log = {
    "France": { "Cities visited" : ["Paris", "Lille", "Dijon"], "total_visits" :12 },
    "Germany": { "Cities visited" : ["Berlin", "Hamburg", "Stuttgart"], "total_visits" :12}
}

#We can as well Nest dictionary in a list

travel_log = [
    {
        "country": "France" ,
         "Cities visited" : ["Paris", "Lille", "Dijon"], 
         "total_visits" :12 
    },
    {
        "country": "Germany", 
        "Cities visited" : ["Berlin", "Hamburg", "Stuttgart"], 
        "total_visits" :5
    }
]


# To access a value within a nested diccionary/list , this example can help
order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}
#Which line of code will print "Steak"?
print(order["main"][2][0])
#[2] accesses the value with key 2, [0] gets the first item from the list.