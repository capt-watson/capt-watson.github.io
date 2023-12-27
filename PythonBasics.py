# num = 5
# print(id(num))
# name = "Shekhar"
# print(id(name))

# print(id("Shekhar"))

# test = {"guava": "a tropical fruit", "python": "a programming language", "the answer": 18}

# print(test)

# print(test["the answer"])

# print(test["guava"])

# print(test["python"])

# print(list(range(10)))

# print(test.keys())

# print(test.values())

# print(test["python"])

# a,b = 5,6

# print(a)
# print(b)

# n = 7
# n = -n    # Unary Operators

# print(n)

# print(a<b)

# print(b<a)

# print(a == b)

# a = 6

# print(a == b)
# print(a >= b)
# print(a <= b)
# print(a != b)

# a = 5

# b = 4

# print(a < 8 and b < 5)      #logical operator

# print(a < 8 and b > 5)      #logical operator

# print(a < 8 or b > 5)      #logical operator

# x = True

# print(x)

# print(not x)

# x = not x

# print(x)

# print(bin(25))         # Convert from decimal format to binary format

# print(0b0101)          # Convert from binary format to decimal format. 0b denotes a binary number

# print(oct(25))          # Convert from decimal format to octal format

# print(hex(25))

# print(0xf)

# print(0b110011010)

# print(~12)

# print(12&13)

# print(12|13)

# print(12^13)

# print(10<<2)

# print(10>>2)

import math

# print(math.sqrt(25))                    # Mathmetical functions

# print(math.sqrt(15))                   # Mathmetical functions

# print(math.floor(2.9))                   # Mathmetical functions

# print(math.ceil(2.2))                   # Mathmetical functions

# print(math.pow(3,2))                   # Mathmetical functions

# print(5 // 2)                           # Integer Divison (Does not return float value)
# print(10 % 3)                           # Returns only remainder value

# print('Shekhar\'s "Laptop"')            # "\" used for ignoring the character following the backslash

# print(10*"Shekhar")

# print(r"C:\docs\navin")                 # "r" before the string means raw string, which ignores \n for new line


# M = int(input("Enter First Number: "))
# N = int(input("Enter Second Number: "))
# O = M + N
# print(O)

# ch = input("Enter a Character:  ")[0]       # Will print only character at index 0.
# print(ch)

# result = eval(input("Enter an Expression:  "))  # Will evaluate expression
# print(result)

# import sys

# x = int(sys.argv[1])        # Argument Value at index 1 entered in terminal
# y = int(sys.argv[2])        # Argument Value at index 2 entered in terminal
# z = x + y

# print(z)



# x = 8
# r = x % 2
# if r == 0:
#     print("Even numbers")
    
# else:
#     print("An Odd Number")


    
# x = 4

# if x == 1:
#     print("One")

# elif x == 2:
#     print("Two")
    
# elif x == 3:
#     print("Three")
    
# else:
#     print("Not a number")


    
i =1

# while i <= 5:
#     print("Sushama")
#     i = i+1



# i = 5

# while i >= 1:
#     print("Sushama", end="")        # Will print Sushama once and the cursor will stay on the same line
    
#     j = 1
    
#     while j <= 4:
#         print("Shekhar", end="")    # Will keep on printing string in the same line until J <= 4
#         j = j+1
        
#     i = i-1
#     print()                         # Will move to the next line after printing 1 instance of Sushama and 4 instance of Shekhar is printed on the same line
    
    
    
# x = ["Shekhar", "Sushama", 5, 10, 15, 20]
# for i in x:
#     print(i)
    
    

# x = "Shekhar"

# for i in x:
#     print(i)



# for i in range(1,11):
#     print(i)
    


# for i in  range(11,21,1):           # range (from, to, step) Note: From is inclusive of the first number while to in exclusive of the given number
#     print(i)
    
    

# for i in range(21, 10, -1):
#     print(i)
    
    
# for i in range(1, 21):
#     if i%5 != 0:
#         print(i)
    
    

# av = 5
# i = 1

# x = int(input("How many Big Macs you want?   "))
    
# while i <= x:
#     if i > av:
#         print("Out of stock")
#         break
#     print("Enjoy You Big mac")
#     i+=1
# print("Thanks for your visit")



# for i in range(1, 101): 
#     if i % 3 == 0 or i % 5 == 0:
#         continue
#     print(i)    
# print("Enjoy your Day!")


# for i in  range(1,101):
#     if i % 2 == 0:
#         pass
#     else:
#         print(i)


# for i in range(4):                              # Will print 4 line with 4 hashes each
#     for j in range(4):                          # Will print # 4 times in a single row
#         print("#", end=(""))       
#     print()
    
    
# for i in range(4):                     # Will print 4 line with 4 hashes each
#      for j in range(i+1):                          # Will print # 4 times in a single row
#         print("#", end=(""))       
#      print()


     
for i in range(4):
    for j in range(4-i):
        print("#", end=(""))
    print()
    
    
