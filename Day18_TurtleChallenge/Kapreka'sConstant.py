from turtle import Turtle,Screen

lechuga = Turtle()
lechuga.shape("turtle")
lechuga.speed(0)
lechuga.setposition(-1000,0)

i=0
coordinates={}
def Decending_order(string_input):
    list=[*string_input]
    list.sort(reverse=True)
    return "".join(list)

def Invert_Number(string_input):
    inverse_number=[]
    number_list=[*string_input]
    for i in range(1,5):
        inverse_number.append(number_list[-i])
    return "".join(inverse_number)

# number  = input("Provide a 4 digit number: ")
# original_number=number
# number  = Decending_order(number)
# inverse = Invert_Number(number)

def Substract(number1,number2):
    return str(number1-number2)

for input_number in range (1000,2000):   
    number  = str(input_number)
    original_number=number
    number  = Decending_order(number)
    inverse = Invert_Number(number)
    for i in range (0,20):
        i +=1
        result=str(Substract(int(number),int(inverse)))
        #print(f"Interation[{i}]:{result}")
        while len(result)<4:
            result="0"+result

        number=Decending_order(result)
        inverse=Invert_Number(number)
        if (result=="6174"):
            break
    coordinates[int(original_number)]= i

for point in coordinates:
    lechuga.setposition((point-2000)*3,coordinates[point]*30)
    print(f"({point},{coordinates[point]})")
    # print(f"Number: {original_number} took {i}")

lechuga.penup()
lechuga.setposition(-500,-7*30)
lechuga.pendown()

previousy=0
for point in coordinates:
    
    lechuga.setposition((point-2000)*3,-(previousy-coordinates[point])*30-7*30) 
    previousy=coordinates[point]
    print(f"({point},{coordinates[point]})")
    # print(f"Number: {original_number} took {i}")

screen = Screen()
screen.screensize(1000,500)
screen.exitonclick()


