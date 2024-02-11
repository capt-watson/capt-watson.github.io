# import math

# r = float(input("Enter radius: "))
# area = math.pi * r**2
# print('Area of the Circle: ', area)
# print('Area of the Circle= {:0.2f}'.format(area))   # formats the area to only two decimal places

# # If Statement

# num = 1
# if num == 1:
#     print("One")

# str = 'Yes'
# if str == 'Yes':
#     print("Yes")
#     print("This is what you said")
#     print("You are learning well")

# num = 15

# if num % 2 == 0:
#     print("Number ",num, " is even")
# else:
#     print("Number",num,"is odd")
    
# num = float(input("Enter a number: "))

# if num % 2 == 0:
#     print("Number ",num, " is even")
# else:
#     print("Number",num,"is odd")
    
# num = float(input("Enter a number:" ))

# if num >= 1 and num <= 10:
#     print("Number ",num, " is between 1 and 10")
# elif num < 1:
#     print("Number ",num, " is less than 1")
# elif num > 10:
#     print("Number ",num,"is greater than 1")
# else:
#     print("You have not entered a valid number")

# # While statement

# # While loop is useful to execute a group of statements several times repeatedly depending on whether a statement is true or false.

# x = 1

# while x <= 7:
#     print("Number",x, "is less than 7")
#     x += 1             # Keeps incrementing the value of x until the while statement is true
# print("End")
      
# x = 100

# while x <= 200:
#     if x % 2 == 0:
#         print("Number",x,"is a even number")
#     x += 1
# print("End")

# m, n = [int(i) for i in input("Enter minimum and maximum range: ").split(",")]

# x = m
# if x % 2 != 0:
#    x = x+1      # If m is not an even number then 1 is added to the x number to make it even
   
# while x >= m and x <= n:
#     print(x)
#     x += 2
# print('End')

# # The For loop

# # for loop is useful to iterrate over the elements of a sequence (e.g. list, dictionary, sets, tuples and range)

# str = "Hello"

# for i in str:
#     print(i)

# str = 'Hello'

# n = len(str)

# for i in range(n):
#     print(str[i])
    
# lst = [10, 20.5, 5, 'C', 'Norway']

# for i in lst:
#     print(i)

# lst = [10,15,20,25,30]

# sum = 0         # Important: for While and for loop, always initialize the variable.

# for i in lst:
#     print(i)
#     sum += i     # Adds the value to the previous value of the sum
# print('Sum= ',sum)

# lst = [10,15,20,25,30]

# i = 0
# sum = 0
# while i < len(lst):
#     print(lst[i])
#     sum += lst[i]
#     i += 1                  # VIMP counter for iterating through the list
#     print('Sum= ',sum)
    
# # Infinite loop
    
#     i= 1
#     while i <= 10:
#         print(i)
#         i += 1              # Comment out this line for the infine loop. To stop the infinite loop, uncomment the line
    
#     # IMP: To stop the infinite loop, we need to type CTRL + C while in terminal mode
    
# # right angle star pattern using nested loop

# for i in range(3):                      # Outer loop repeats for 3 times (0 to 2)
#     for j in range(4):                  # Inner loop repeats for 4 times (0 to 3)
#         print("i = ",i, "\t", "j = ",j)

# for i in range(1, 11):                  # To Display 10 rows
#     for j in range(1, i+1):             # no of stars = row numbers
#         print('*', end='')
#     print()                             # This prints the line whenever i value changes
    
# # Right angle star pattern using a single loop

# for i in range(1, 11):
#     print('*'*i)        # number of stars printed in each row will be equal to that row number
    
# # To Display Stars in an Equilateral Triangle shape

# n = 10                      # number of spaces to be added in the row before printing star
# for i in range(1, 11):
#     print(' '*n, end='')    # Will print the n number of spaces in each row before  printing star
#     print('* '*i)          # Each start printed will add a space to the right & number of stars printed will be equal to that row number
#     n -= 1                 # Spaces to be added in each row will keep reducing as the number of lines gets printed

# n = 10                              # Elegant style of coding
# for i in range(1, 11):
#     print(' '*(n-i) + '* '*(i))

# for x in range(1, 11):
#     for y in range(1, 11):
#         print('{:5}'.format(x*y), end='') # Number given in Replacement field decides each column width.     
#     print()

# The Else suit

# for i in range(5):
#     print('Yes')
# else:
#     print("No")

# for i in range(0):
#     print('Yes')
# else:
#     print("No")

# lst = [1,2,3,4,5]
# search = int(input("Enter a number to search: "))
# for i in (lst):
#     if search == i:
#         print('Your number is found in the list')
#         break
# else:
#     print('Your number is not found in the list')
    
# # The Break Statement

# # When 'break' is executed, the Python interpreter jumps out of the loop to process thenext stament in the program.

# x = 10

# while x >= 1:
#     print('X= ', x)
#     x -= 1
#     if x == 5:
#         break
# print('Out of the loop')

# # the Contne statement is used in a loop to go back to the beginning of the loop.

# x = 0

# while x < 10:
#     x += 1
#     if x > 5:
#         continue
#     print(x)
# print('Out of the loop')

# # The Pass Statement does not do anything.It is used with if statement or inside a loop to represent no operation.

# x = 0

# while x < 10:
#     x += 1
#     if x > 5:       # Here the pass statement nullifies the effect of the if statement
#         pass
#     print(x)
# print('Out of the loop')

# # Assert statement used for checking if a particular condition is fulfilled or not.

# x = int(input("Enter a number greater than 0: "))

# assert x>0, 'Wrong number entered'
# print('You have entered= ',x)

# # Assertion Error shown is called an exception. An exception is an error that occurs during runtime.
# # To handle them, we use 'try and except statements.


# x = int(input("Enter a number greater than 0: "))
# try:
#     assert(x>0)
#     print('You have entered= ',x)
# except AssertionError:
#     print('You have entered a wrong number')    # This is executed in the case of an exception
    
# # Return statement
# # Keyword 'def' definition of the function. We should write name of this function after 'def' keyword. then variables should be writtend in paranthesis

# # def sum(a,b):
# #   function body

# def sum(a,b):
#     print(a+b)
    
# # A function is executed only when it is called.
# # At the time of call sum function, we should pass values to the variables a and b.

# sum(7,5)

# def sum(a,b):
#     print('sum= ',a+b)

# sum(7,5)        # One can pass as many values as possible.
# sum(1.5, 2.5)

# def sum(a,b):
#     return a+b

# res = sum(5,10)         # Here we are calling the sum function and passing variables value as 5 & 10.
# print('The sum is: ',res)

# Program to display prime numbers

# max = int(input('Upto which number?'))

# for num in range(2, max+1):     # generates numbers from 2 onwards till max.
#     for i in range(2, num):     # represents numbers from 2 to num-1
#         if (num % i) == 0:      # if num is divisible by i
#             break               # It is not a prime, hence go back and check next number
#     else:
#         print(num)              # It is a prime and hence display
        
# # Fibonacci number generator

n = int(input('How many Fibonacci numbers? '))

f1 = 0      # This is the first Fibonacci number
f2 = 1      # This is the second Fibonacci number

c = 2      # Count the number of Fibonacci numbers. 2 in the starting number

if n==1:
    print(f1)
elif n==2:
    print(f1, '\n', f2, sep='')
else:
    print(f1, '\n', f2, sep='')
    while c<n:
        f = f1+f2       # Add two Fibonacci numbers to get a new number
        print(f)                         
        f1 = f2         # f2 value is taken from previous loop.
        f2 = f          # f value is from the previous loop
        c += 1          # Increment the number
 #   f1   f2    f
 #   0  +  1  =  1        f2 value goes down to become new f1 and f value goes down to become new f220
 #   1  +  1  =  2
 #   1  +  2  =  3
 #   2  +  3  =  5
 #   3  +  5  =   8
 #   5  +  8  =  13

# Evaluate Sine Series

# Formula to calculate the sine value is given by:

# t= (=1)*t*r*r/(i*(i+1))               VIMP Formula

# x, n = [int(i) for i in input("'Enter angle value, no. of iterations: ").split(',')]
# r = (x*3.14159)/180         # Convert to radians

# t = r                       # this becomes the first term

# sum = r

# print('Iteration= %d\tSum= %f' % (1,sum))

# i=2                         # Denominator for the second term

# for j in range(2, n+1):
#     t = (-1)*t*r*r/(i*(i+1))  # Second Term. (-1) represents positive & negative value
#     sum = sum+t;              # Add it to sum
#     print('iteration= %d\tSum= %f' % (j, sum))
#     i += 2      # Increase i value by 2 for denominator for next term

# Python program to find Cosine values of a given angle in Degreesby evaluating Cosine series

# Cosine Formula = t = (-1*)*t*r**2/(i*(i+1))

# x, n = [int(i) for i in input("'Enter angle value, no. of iterations: ").split(',')]

# r = (x*3.14159)/180         # Convert from Degrees to radians

# t = 1                      # this becomes the first term

# sum =1                    # Till now sum is 1 only

# print('Iteration= %d\tSum= %f' % (1,sum))

# i=1                         # Denominator for the second term

# for j in range(2, n+1):
#     t = (-1)*t*r**2/(i*(i+1))  # Second Term. (-1) represents positive & negative value
#     sum = sum+t;              # Add it to sum
#     print('iteration= %d\tSum= %f' % (j, sum))
#     i += 2      # Increase i value by 2 for denominator for next term
    
# # Python program to evaluate exponential series

# value of e = 2.718281828. Hence e^2 = 7.389056

# x, n = [int(i) for i in input("Enter power of e, no. of iteration: ").split(',')]

# t = 1       # This becomes our 1st term

# sum = t

# print('iteration= %d\tSum= %f' % (1, sum))

# for j in range(1,n):        # Repeat for 1st to nth term
#     t = t*x/j               # Find the next term
#     sum = sum+t;            # Add it to sum
#     print('iteration= %d\tSum= %f' % (j+1, sum))          
