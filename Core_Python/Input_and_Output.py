# Print("String") statement

print("This is the \nFirst line")       # Here \n indicates new line. \ is called escape sequence charater

print("This is the \tFirst Line")       # \t inserts a tab space

print("This is the \\nFirst Line")       # \\ nullifies the effect of \ escape sequence character

print("This is the \\tFirst Line")       # \t nullifies the effect of \ escape sequence character

print("Aarav"*3)                           # Repeats the string for a given number of times

print("My Home City = " + "Mumbai")

# Print(Variable list) Statement

a, b, c = "Hello", "Dear", "How are you?"

print(a)                # Here all the outputs are printed on seperate lines

print(b)

print(c)

print(a, b)

print(a, b, sep=":")                        # sep="," or sep=":" means seperator and character inserted between string is used as seperator

print("Hello ", end="")                 # end="" represents line ending with a blank and hence next printout will appear on the same line
print("Dear ", end="")
print("How are you? ", end="")

print("Hello ", end="\t")                 # end="\t" seperates outputs a tab space and hence next printout will appear on the same line
print("Dear ", end="\t")
print("How are you? ", end="")

# Print object statement

lst = [1, "Shekhar", "Emily"]
print(lst)

d = {'Amritsari Kulche':50, 'Chhole':100, "Paneer Tikka": 180}
print(d)

 # Print("String",Variable list) Statement

a = 2
print(a," is an even number.")

print("You typed", a,"as an input")

 # Print("Formatted string" % (Variables list))   % sign means output of string is formatted

x = 10
print("value= %i" % x)          # Here %i represents an integer, %d represents a decimal number, %f represents a float number and %s represents a string. No pranthesis Single Variable

x, y = 10, 15
print("x= %i  y= %d" % (x, y))

name = "Shekhar"
print("Hi %s" % name)           # %s formats variable in a string format

print("Hi %10s" % name)         # %10s allots 10 spaces and then right aligns the string with spaces

print("Hi %-10s" % name)         # %10s allots 10 spaces and then left aligns the string with spaces

print("Shekhar %c, %c" % (name[0], name[1])) # Print 0th and 1st character from variable. %c format displays a single character

print("Shekhar %s" % name[0:2])     # Slicing operator is used to display the required characters from the string

num = 123.456789
print("The value is: %f" % num)

print("The value is: %8.2f" % num)    # %8.2f creates 8 spaces and then places a decimal point and prints the next 2 fracction digits

print("The value is: %.2f" % num)    # %.2f creates 0 spaces before the gigits and then places a decimal point and prints the next 2 fracction digits

n1, n2, n3 = 1, 2, 3

print("Number1 = {0}".format(n1))       # {} represents the replacement field

print("Number1 = {0}, number2 = {1}, number3 = {2}".format(n1, n2, n3))       # {} represents the replacement field. Number in the replacement field is an index number

print("Number1 = {1}, number2 = {0}, number3 = {2}".format(n1, n2, n3))       # when replacement field number is changed, the order of the number displayed will also be changed

print("Number1 = {two}, number2 = {one}, number3 = {three}".format(one = n1, two = n2, three = n3))  # when replacement field number is changed, the order of the number displayed will also be changed

print("Number1 = {}, number2 = {}, number3 = {}".format(n1, n2, n3))  # when replacement field number is used without mentioning either index or names, braces will assume sequence of values as they are given.

name, salary = "Shekhar", 500000.75
print("Hello {0}, your salary is {1}".format(name, salary))

print("Hello {n}, your salary is {s}".format(n = name, s = salary))

print("Hello {:s}, your salary is {:.2f}".format(name, salary))

print("Hello %s, your salary is %.2f" % (name, salary))

 # User Input Function. This function takes a value from the keyboard and returns it as a string.

str = input("Enter your name: ")      # This function will wait till we enter a string

print(str)

str = float(input('Enter a number: '))        # str is converted into a int
print(str)

str = input("Enter a string: ")
print("You enetered: ", str)

ch = input("Enter a char: ")
print("You entered: ", ch)

ch = input("Enter a char: ")
print("You entered: ", ch[0])

x = int(input("Enter First number: "))
y = int(input("Enter Second number: "))
print('You entered: ', x, y)

x = int(input("Enter First number: "))
y = int(input("Enter Second number: "))
print('You entered:  %d, %d' % (x,y) )

x = int(input("Enter First number: "))
y = int(input("Enter Second number: "))
print('The Sum of ',x, 'and',y, 'is:', x+y)
print('The sum of {} and {} is {}'.format(x,y, x+y))

x = int(input("Enter First number: "))
y = int(input("Enter Second number: "))
print('The Sum of {0} and {1} is: {2}'.format(x,y, x+y))
print('The sum of {0} and {1} is: {2}'.format(x,y, x*y))
print('The sum of {0} and {1} is: {2} and product of {0} and {1} is: {3}'.format(x,y, x+y, x*y)) 

str = input('Enter Hexadecimal Number: ')
n = int(str, 16)                # Inform the number is base 16
print('Hexadecimal To Decimal= ', n)

str = input('Enter an Octal Number: ')
n   = int(str, 8)               # Inform the number is base 8
print('Octal to Decimal= ', n)

str = input('Enter a Binary Number: ')
n   = int(str, 2)               # Informs the number is base 2
print('Binary to Decimal= ', n)

a, b = [int(x) for x in input('Enter Two Numbers: ').split()]   # Split() will divide the two numbers string whereever a space is found between two values.
print(a,b)                                                      # The square brackets [] around the total expression indicates the input is accepted as elements of a list.

a, b, c = [int(x) for x in input('Enter Three Numbers: ').split()]   # Split() will divide the two numbers string whereever a space is found between two values.
print('Sum= ', a+b+c)

lst = [x for x in input('Enter Three Names: ').split(',')]   # Split() will divide the two numbers string whereever a space is found between two values.
print('You Entered these names:\n ', lst)

a, b = 5, 10
result = eval('a + b - 4')          # Evaluate the expression
print(result)

x = eval(input('Enter an Expression: '))
print('Result= %d' % x)

lst = eval(input('Enter a List: '))
print("List= ", lst)


lst = eval(input('Enter a List: '))
print("List= ", lst)

tpl = eval(input('Enter A Tuple: '))
print("tpl: ", tpl)

import sys

n = len(sys.argv)       # n is the number of arguments
args = sys.argv         # args list contains arguments
print('No. of command line args= ', n)
print('The args are: ', args)
print('The args one by one: ')
for a in args:
    print(a)

import sys

sum = int(sys.argv[1]) + int(sys.argv[2])

import math as m

x = m.sqrt(16)
print(x)

