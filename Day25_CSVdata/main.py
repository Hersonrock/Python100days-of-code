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

data = pandas.read_csv("Day25_CSVdata\weather_data.csv")
temp_list=data["temp"].to_list()

temp_sum=0

print(data["temp"].mean())
print(data["temp"].max())

# temp_sum=sum(temp_list)
# print(f"average temp: {temp_sum/len(temp_list)}")