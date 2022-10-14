
# Learned
#  For loops
#  The importance of indentation.
#  The range function (example {4..5})  


# example 1:

   # fruits = ["Apple","Pear","Coconut"]
   # for fruit in fruits:
   #    print (fruit+" Pie")

#Here we can see how the for loop will go trough each element "fruit" of the list "fruits"

# example 2:

   # # 🚨 Don't change the code below 👇
   # student_heights = input("Input a list of student heights ").split()
   # for n in range(0, len(student_heights)):
   # student_heights[n] = int(student_heights[n])
   # # 🚨 Don't change the code above 👆

   # #Write your code below this row 👇

   # sum = 0
   # count = 0
   # for i in student_heights:
   #    sum += i
   #    count +=  1

   # average = round(sum/count)
   # print (average)

#Here the loop will go through each element VALUE directly. If I want to know on which step of the loop I am, I would need to manually count it.

# example 3: 

   # # 🚨 Don't change the code below 👇
   # student_scores = input("Input a list of student scores ").split()
   # for n in range(0, len(student_scores)):
   #   student_scores[n] = int(student_scores[n])
   # print(student_scores)
   # # 🚨 Don't change the code above 👆

   # #Write your code below this row 👇

   # highScore=0

   # for score in student_scores:
   #     if score>highScore:
   #         highScore=score

   # print(f"The highest score in the class is: {highScore}")

#Here the loop us used to calculate a "maximum",means that on each instance of the loop it checks if the value is higher than the last, if not is discarded.

# example 4:
   # for number in range(1,21):
   #    print(number)
#In this example we can see how it would be required a range from 1,21 to print numbers from 1 to 20.

#example 5: 

   # numbers = range(0,102)
   # sum = 0
   # for number in numbers:
   #     if number%2==0:
   #         sum +=number

   # print(sum)

#here we can see another use of the range function.