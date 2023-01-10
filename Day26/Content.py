
import random


#--------List Comprehension

#new_list=[new_item for item in list]
#new_list=[new_item for item in list if test]


#---------Dictionary comprenhension

# new_dic= {new_key:new_value for item in list}
# new_dic= {new_key:new_value for (key,value) in dic.items()}


#-----Example
names= ["Alex","Beth","Caroline","Dave","Eleanor","Freddie"]
name_dic={name:random.randint(1,100) for name in names}
passed_names={name:score for (name,score) in name_dic.items() if score>50}
print(passed_names)

#-----
#Review Pandas .iterrows()
