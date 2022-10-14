
# Learned
#    For loops
#    The importance of indentation.


# example 1:

   fruits = ["Apple","Pear","Coconut"]
   for fruit in fruits:
      print (fruit+" Pie")

#Here we can see how the for loop will go trough each element "fruit" of the list "fruits"

# example 2:

   # 🚨 Don't change the code below 👇
   student_heights = input("Input a list of student heights ").split()
   for n in range(0, len(student_heights)):
   student_heights[n] = int(student_heights[n])
   # 🚨 Don't change the code above 👆

   #Write your code below this row 👇

   sum = 0
   count = 0
   for i in student_heights:
      sum += i
      count +=  1

   average = round(sum/count)
   print (average)

