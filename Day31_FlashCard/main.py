import csv

#Reading file contents.
with open("E:\Python 100 days\Day31_FlashCard\ja_full.txt", mode="r",encoding="utf8") as ja_raw:
    content=ja_raw.read().replace(" ",",")

    print(content,file=open("E:\Python 100 days\Day31_FlashCard\ja.csv","w",encoding="utf8"))

