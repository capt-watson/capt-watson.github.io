
# Program with two functions
# def add(x, y):
#     '''
#     This function adds two numbers and finds their sum
#     It displays the sum as result.'''
#     print("Sum: ",x + y)    
# def message():
#     '''
#     This function displays a message.
#     This is a Welcome message to the user.
#     '''
#     print("Welcome to Python")
# # Now call the function    
# add(5, 10)
# message()

# x = -57  This is an integer

# num = 55.6789  This is a float number

# Python program to add two complex numbers

# c1 = 2.5+2.5j
# c2 = 3.0-0.5j

# c3 = c1 + c2

# print("Sum:  ",c3)

# int(x) is used for converting the number x into int type.
 
# x = int(15.56)  # will display 15     
# print(x)

# num = float(15)
# print(num)

# # Complex(x) is used for converting the number x into complex number with real part x and imaginary part zero. for example:

# n = complex(10)
# print(n)

# # Complex(x,y) is used to convert x and y into a complex number such that x will be the real part and y will be the imaginary part.

# a = 10
# b = -5
# print(complex(a,b))

# # A program to convert numbers from Octal, binary and hexadecimal systems into a decimal number system. base 2 indicates a binary number and base 16 indicates a hexadecimal number

# python program to convert into decimal number system

# n1 = 0o17
# n2 = 0B1110010
# n3 = 0x1c2

# n = int(n1)
# print("Octal 17 = ", n)

# n = int(n2)
# print("Binary 1110010 = ", n)

# n = int(n3)
# print("Hexadecimal 1c2 = ", n)

# str = "1c2"         # string str contains a hexadecimal number
# n = int(str, 16)    # hence base is 16. Convert str into int
# print(n)


# s1 = "17"
# s2 = "1110010"
# s3 = "1c2"

# n = int(s1, 8)
# print("Octal 17 = ", n)

# n = int(s2, 2)
# print("Binary 1110010 = ", n)

# n = int(s3, 16)
# print("Hexadecimal 1c2 = ", n)


# a = 10
# b = bin(a)
# print(b)        # displays 0b1010

# b = oct(a)
# print(b)        # displays 0o12

# b = hex(a)      # displays 0xa
# print(b)

# # slice operator []

# s = 'Welcome to core Python'
# print(s)

# print(s[0])         # prints 0th character from s

# print(s[3: 7])         # prints from 3rd character to 6th character from s

# print(s[11:])         # prints from 11 character onwards till the end

# print(s[:2])         # prints from s till the 2nd character from s

# print(s[-1])         # prints first character from the end

# print(s[::-1])           # prints reverse string from s

# print(s*2)              # repetition Operator

# elements = [10, 20, 0, 40, 15]      # This is a list of byte numbers

# x = bytes(elements)                 # Convert the list into a byte array.

# print(x[0])                         # display 0th element i.e. 10

# x[0] = 55                           # We can't modify or edit any elements in the byte type array.

# for i in x:
#     print(i)

# # bytearray is similar to byte data type. However, unlike byte data types, bytearray type can be modified
# elements = [10, 20, 0, 40, 15]
# x = bytearray(elements)               # Convert the list into a bytearray type array.
# print(x[0])

# x[0] = 88                             # replace 0th element by 88
# x[1] = 99                             # replace 1st element by 99

# for i in x:
#     print(i)
    
# list = [10, -20, 15, 5, 'Andrew', "Mary"]        # List is mutable
# # print(list)

# print(list[-2])

# tpl = (10, -20, 15, 5, 'Andrew', "Mary")

# tpl[0] = 5                                        # Tuple is immutable. It is read only.

# print(tpl)


# r = range(10)    # Range is Immutable. It represents a sequence of numbers. It is used for repeating a for loop for a specific number of times

# for i in r:
#     print(i)

# r = range(30, 40, 2)       # This will create a range object with a starting number of 30, ending at 39 with a step size of 2.

# for i in r:
#     print(i)
    
# lst = list(range(10))
# print(lst)                  # Will print a list of number between 1 and 9.


#  # A set is an unordered collection of numbers. The elements may not appear in the same order as they are entered into the sets.
#  # A Set does not accept duplicate elements.

#  # Set datatype

# s = {10, 20, 30, 20, 50}
# print(s)                    # The output will not have number 20 twice. {10, 20, 50, 30}. Also order is not same as entered.

# ch = set("Hello")
# print(ch)               # o/P = {'H', 'e', 'o', 'l'}

# lst = [1,2,5,4,3]
# s = set(lst)                # Convert list into a set.
# print(s)
# print(s[0])
# print(s[0:2])               # We cannot retrieve an element using indexing or slicing operations as set data types are unordered.

# s.update([50,60])           # We can append additional elements into the set.
# # print(s)

# s.remove(50)              # We can remove all elements from the set. Remember to put the desired number in round bracket.
# print(s)

#  # Frozen datatypes
#  # The element of the frozen datatype unlike the set datatype, can not be modified.

# s = {50, 60, 70, 80, 90}
# # print(s)

# # fs = frozenset(s)       # Convert the above set datatype into a frozen datatype
# # print(s)

# fs = frozenset("abcdefg")   # Another way of creating a frozen datatype by passing a string.
# print(fs)                   # Note: Update() and remove() will not work on frozen datatypes

#  # Mapping Types

# # Dictionary datatype ia an example of a map. The 'dict' represents a 'dictionary' that contains a elements such that the first element
# # represents the key and the second element becomes its value. Key and value should be separated by colon ( : ) and every pair should
# # be separated by a comma. All the elements should be enclosed inside curly brackets {}.

d = {10:'Sushama', 11: 'Ashish', 12:'Aakash', 13:'Aarav', 14:'Ranveer'}

# d = {}          # An empty dictionary

# d[10] = 'Sushama'
# d[11] = 'Ashish'

# print(d)
# print(d[11])            # Will return value at key 11.

# print(d.keys())         # Will return all the keys from the said dict.

# d[10] = "Darling"       # Dict is mutable.
# print(d)

# del d[14]               # Dict is mutable
# print(d)

#  # Literals in Python

#  # A literal is a constant value that is stored into a variable in a program.

# a = 15      # Here 'a' is a variable into which a constant value '15' is stored. Hence, the value 15 is called 'literal' 
            # Since 15 indicates integer value, it is called 'integer literal'.
            
#  # Types of literals in Python

#  # Numeric Literals   
#  # Boolean Literals   
#  # String Literals   

#  # Numeric Literals: These literals represent numbers. 

#  # 450, -15                   Integer Literal   
#  # 3.14286, -10.6, 1.25E4     Float Literal   
#  # 450, -15  0x5A1m           Hexadecimal Literal   
#  # 0o557                      Octal Literal   
#  # 0B110101                   Binary Literal   
#  # 18+3J                      Complex Literal

## Boolean literals : True or False

#  # String Literals


#  # A group of characters is called a string literal.

# x = 5          # 10 = 0000 1010 & 11 = 0000 1011 Hence x&y = 0000 101clea0 = 10 in decimal number
# y = 11
# print("~x =", ~x)       # To get the complement number, add 1 to the first number and add a minus (-) sign to it.

# print('x & y = ', x & y)
# print('x | y = ', x | y)
# print('x ^ y = ', x ^ y)    # "^" is pronounced as "Cap". This produces true only when both the inputs are not the same.
# print('x << y = ', x << 2)    # Bitwise Left shift. This operator shifts the binary elements of x to left by 2. Knocks out 2 digits on the left and adds 2 zeros on the right.
# print('x >> y = ', x >> 2)    # Bitwise Right shift. This operator shifts the binary elements of x to Right by 2. Knocks out 2 digits on the right and adds two zeros on the left.

#  # Membership Operator    "in" and "not in" operator

# names1 = ["Simon", "Watson", "James", "Anne", "Simpson"]
# names2 = "Watson"
# names3 = "Shekhar"

# for name in names1:
#     print(name)

# if(names2 in names1):
#     print("Yes")
# else:
#     print("Not Found")

# if(names3 not in names1):
#     print("Not Found")
# else:
#     print("Name Found")

# # Identity Operator

# a = 18
# b = 18

# if(a is b):
#     print("a and b have same identity")
# else:
#     print("a and b do not have same identity")

# one = [1,2,3,4]
# two = [1,2,3,4]

# # if(one is two):
# #     print("One and Two have same identity")     # Here 'is' and 'is not' operators fo not compare the values of the object but compare only tthe memory locations of the objects.
# # else:
# #     print("One and Two do not have same identity")
    
# # print(id(one))
# # print(id(two))

# if(one == two):
#     print("One and Two values are same")
# else:
#     print("One and Two values are not same")
    
import math as m

# x = m.sqrt(16)
# print(x)

# from math import factorial, sqrt

# x = sqrt(16)
# y = factorial(5)

# print("x =", x)
# print("y = ", y)

r = 15
area = m.pi*r**2

print("Area of Circle= ", area)