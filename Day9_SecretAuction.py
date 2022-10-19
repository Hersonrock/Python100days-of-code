logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
import os
#HINT: Clearing the Screen
#   os.system('cls')

other_bidders=True
bidders_dic={}
bidder_list= []
i=0
max_bid=0
max_bid_name=""

while other_bidders:
  os.system('cls')
  print(logo)
  i += 1
  other_bidders_raw=""
  print("Welcome to the secret auction program.")
  bidder_list.append(input("What is your name?: "))
  bidder_list.append(float(input("What is your bid?: $")))
  bidders_dic[i] = bidder_list
  bidder_list=[]

  while other_bidders_raw!="yes" and other_bidders_raw!="no":
    other_bidders_raw= input("Are there any other bidders? Type \'yes\' or \'no\'. \n").lower()
    if other_bidders_raw=="yes":
      other_bidders=True
    elif other_bidders_raw=="no":
      other_bidders=False
    else:
      print("Wrong Answer, please try again.")

os.system('cls')
print(logo)     

for bidder_number in bidders_dic:
     if   bidders_dic[bidder_number][1]>max_bid:
      max_bid=bidders_dic[bidder_number][1]
      max_bid_name=bidders_dic[bidder_number][0]

print(f"The winner is {max_bid_name} with a bid of ${max_bid}.")
