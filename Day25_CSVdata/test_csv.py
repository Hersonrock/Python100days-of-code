import pandas
#https://pandas.pydata.org/docs/reference/

data = pandas.read_csv("Day25_CSVdata\Test_values.csv")
temp_list=data.to_list()
print(temp_list)