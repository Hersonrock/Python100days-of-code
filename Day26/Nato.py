# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# import pandas
# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}

#-------------------------------------------
# #TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

# #TODO 2. Create a list of the phonetic code words from a word that the user inputs.


import pandas as pd

nato=pd.read_csv("Day26\\nato_phonetic_alphabet.csv")

nato_dic ={row.letter:row.code for (index,row) in nato.iterrows()}
#-------Debug-------
# print(nato_dic)



error=False

while error==False:
    try:
        word = input("Enter a word: ").upper()
        response = [ nato_dic[letter] for letter in word]
    except KeyError:
        print("Word can only contain letters in the alphabet")
    else:
        error=True



#My first attempt I was taking the inverse approach of going trough the dic to match the list , instead of going through the list to match the dic
#response= [ code for (letter,code) in nato_dic.items() if letter.lower() in word_list ]



print(response)