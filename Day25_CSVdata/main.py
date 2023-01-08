# with open("Day25_CSVdata\weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)


# import csv

# temperatures=[]
# with open ("Day25_CSVdata\weather_data.csv") as data_file:
#     data= csv.reader(data_file)
#     for row in data:
#         if row[1]!="temp":
#             temperatures.append(int(row[1]))

# print(temperatures)

import pandas
#https://pandas.pydata.org/docs/reference/

data = pandas.read_csv("Day25_CSVdata\weather_data.csv")
temp_list=data["temp"].to_list()

temp_sum=0

def to_f(c):
    return (c*9/5)+32

# print(data["temp"].mean())
# print(data["temp"].max())

# monday=data[data.day=="Monday"]
# monday_temp=int(monday.temp)

# print(to_f(monday_temp))

# temp_sum=sum(temp_list)
# print(f"average temp: {temp_sum/len(temp_list)}")


#create a dataframe

data_dic = {
    "students": ["Amy","Angela","Karen"],
    "scores":[76,56,65]
}

data=pandas.DataFrame(data_dic)

data.to_csv(".\Day25_CSVdata\\new_data.csv")
