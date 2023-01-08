# with open("Day25_CSVdata\weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)


import csv

temperatures=[]
with open ("Day25_CSVdata\weather_data.csv") as data_file:
    data= csv.reader(data_file)
    for row in data:
        if row[1]!="temp":
            temperatures.append(int(row[1]))

print(temperatures)
