logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


def add(n1, n2):
    return n1+n2

def subtract(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def divide(n1, n2):
    if n2 !=0:
        return n1/n2
    else:
        print("Cannot divide by 0")
        return 

operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}
continue_calculating=True
continue_calculating_raw=""
flag=True
print(logo)


def calculation(previous):

    if flag:
        num1 = int(input("What's the first number?: "))

    for symbol in operations:
          print(symbol)
    operation_symbol=input("Pick an operation from the line above: ")
    num2 = int(input("What's the second number?: "))

    calculation_function = operations[operation_symbol]
    if flag:
        result= calculation_function(num1, num2)
        return [num1, operation_symbol, num2, result]
    else:
        result= calculation_function(previous, num2)
        return [previous, operation_symbol, num2, result]


while continue_calculating:

    if flag:
        result_data= calculation(1)
    else:
        result= result_data[3]
        result_data= calculation(result)

    print (f"{result_data[0]} {result_data[1]} {result_data[2]} = {result_data[3]}")

    while continue_calculating_raw!="y" and continue_calculating_raw!="n":
        continue_calculating_raw=input(f"Type \'y\' to continue calculating with {result_data[3]}, or type \'n\' to exit: ")
        if continue_calculating_raw=="y":
            continue_calculating=True
        elif continue_calculating_raw=="n":
            continue_calculating=False
    continue_calculating_raw=""
    flag=False

print("Good Bye")