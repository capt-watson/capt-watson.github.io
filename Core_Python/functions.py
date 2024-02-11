
#@ Defining a function

#! def

## Define a function using keyword, 'def' followed by function name
## After function name, write paranthesis () containing paramtrs
## ''' ''' are called docstring & it gives info abt function

# def sum(a,b):
# '''This Function finds sum of two numbers'''
#     c = a+b
#     print('Sum = ',c)
    
    ## call the function
    
# sum(5, 10)
# sum(1.5, 10.75)

#@ Returning results from a function

#     ## A function doesn't return any result, we need to write
#     ## the return statementin the body of the function.
    
# def sum(a, b):
#     '''This function finds sum of 2 numbers'''
#     c = a+b
#     return c    ## return result

#     ## when we call the function as x = sum(10,15), the result
#     ## returned by the function gets stored in variable x.
# x = sum(10, 15)
# print('The Sum is: ',x)

#     ## when we call the function as y = sum(1.5,10.75), the result
#     ## returned by the function gets stored in variable y.

# y = sum(1.5, 10.75)
# print('The sum is: ', y)

# def even_odd(num):
#     if num %2 == 0:
#         print(num,'number is even')
#     else:
#         print(num, 'number is odd')
        
# even_odd(12)

# even_odd(13)

#@ Calculate factorial Values
 
#   ## n! n * n-1 * n-2 ... 1 
 
# def fact(n):
#     '''to find factorial values'''
#     prod = 1        ## initialize prod to 1
#     while n >= 1:   ## repeat as long as n >= 1
#         prod *= n   ## prod=prod*n
#         n -= 1      ## decrease n val by 1 every time
#     return prod

#     ## Display factorials of first 10 numbers
#     ## call fact() and pass numbers from 1 to 10

# for i in range(1, 11):
#     print('Factorial of {} is {}'.format(i, fact(i)))

#@ program to check if prime number or not
 
# def prime(n):
#     '''To check if prime number'''
#     x = 1   ## This will be 0 if not prime
#     for i in range(2,n):
#         if n % i == 0:      ## Divide n by all number between 2 and n-1
#             x = 0           ## if divisible by any number
#             break           ## come out of the loop
#         else:
#             x = 1           ## else take x as 1
#         return x
    
#   ## test if a number is prime or not
  
# num = int(input('Enter a number: '))
  
#   ## check if 'num' is a prime number or not
  
# x = prime(num)
# if x == 1:
#     print(num, 'is a Prime Number')
# else:
#     print(num,'is not a Prime Number')


#@ program to generate prime numbers
 
# def prime(n):
#     '''To check if prime number'''
#     x = 1   ## This will be 0 if not prime
#     for i in range(2,n):
#         if n % i == 0:      ## Divide n by all number between 2 and n-1
#             x = 0           ## if divisible by any number
#             break           ## come out of the loop
#         else:
#             x = 1           ## else take x as 1
#         return x
    
# num = int(input('How many prime numbers you need?: '))

# i = 2       ## start with value 2
# c = 1       ## Prime number counter

# while True:         ## repeat forever
#     if prime(i):    ## if i is prime, display it
#         print(i)
#         c += 1      ## Increase prime counter number
#     i += 1          ## Generate next number to test
#     if c > num:     ## If counter exceeds supplied number
#         break       ## come out of the loop
    
#@ Returning multiple values from a Function

# def sum_sub(a, b):
#     '''This function returns results of addn and subn'''
#     c = a + b
#     d = a - b
    
#     return c,d

# x, y = sum_sub(10,5)

# print('Sum = ',x)
# print('Difference = ',y)

#@ Function returning results of Addition, Subtraction, Multiplication & division

# def sum_sub_mul_div(a,b):
#     '''This function returns result of addn, subn, mult & div a & b'''
#     c = a + b
#     d = a - b
#     e = a * b
#     f = a / b
    
#     return c,d,e,f

# t = sum_sub_mul_div(10, 5)

# print('The results are: ')
# for i in t:
#     print(i, end=', ')

#@ Assign a function to a variable

# def display(str):
#     return 'Hi ' +str

# x = display('Sushama')
# print(x)

#@ Define a function inside another function

#! Since display() has to receive another function as its parameter, it should be
#! defined with another function 'fun' as parameter.

# def display(str):
#     def message():
#             return 'How are you, Darling'
    
#     result = message()+str
#     return result

# print(display(' Sushama'))

#@ Pass a function as parameter to another function

# def display(sun):
#     return 'Love You'+sun
# def message():
#     return ' Sushama Darling'

# print(display(message()))

#@ Function can return another function

# def display():
#     def message():
#         return 'How are you?'
#     return message

# x = display()
# print(x())

#@ Pass by Object Reference

#@ Pass an integer to a function and modify it

# def modify(x):
#     '''reassign a value to a variable'''
#     x = 15
#     print(x, id(x))
    
# x = 10
# modify(x)
# print(x, id(x))

#! 15 140704681596136
#! 10 140704681595976

## as it is evident that although the value was modified by modify(), the new value
## was placed at different object. This is due to the fact that integers, floats, strings
## and tuples are immutable and hence can't be modified. When we try to change their
## value, a new object is created with the modified value.

# def modify(lst):
#     '''Add a new element to the list'''
#     lst.append(9)
#     print(lst, id(lst))
    
# lst = [1,2,3,4]
# modify(lst)
# print(lst, id(lst))

## Values are passed to functions by object references. 

## object created inside a function is not accessible outside that function.

# def modify(lst):
#     '''To create a new list'''
#     lst = [10, 20, 30]
#     print(lst, id(lst))
    
# lst = [1,2,3,4]
# modify(lst)
# print(lst, id(lst))

# def sum(a,b):       #! a, b are formal arguments
#     c = a+b
#     return c

# x = sum(10, 15)     #! 10, 15 are actual arguments
# print(x)

#@ Keyword arguments
## Keyword arguments are arguments that identify the parameters by their names.

## def grocery(item, price):

## At the time of calling this function, we have to pass two values and we can
## mention which value is for what. e.g
## grocery(item='Sugar', price=50.75)

## Here keyword is 'item' and its value, then another keyword 'price' and its value.

## We can change the order of the arguments as:

## grocery(price=88.00, item='Oil') 

# def grocery(item, price):
#     '''to display given arguments'''
#     print('Item = %s' % item)
#     print('Price = %.2f' % price)
    
# grocery(item= 'Sugar', price= 50.75)    ## Keyword arguments
# grocery(price= 88.00, item= 'Oil')      ## keyword arguments

#@ Default Arguments

#* def grocery(item, price=40.00)

## here the first argument is 'item' whose default value is not mentioned.
## Second argument is 'price' whose default value is mentioned to be 40.00.

## A default argument is an argument that assumes a default value if a value
## is not provided in the function call for that argument.

# def grocery(item, price=40.00):
#     '''To display the given arguments'''
#     print('Item= %s' % item)
#     print('Price= %.2f' % price)
    
# #* Call grocery() and pass arguments

# grocery(item= 'Sugar', price= 50.75)
# grocery(item= 'Sugar') ## Default value of the price is used

#@ variable length arguments

## If the programmer wants to develop a function that can accept 'n' arguments, that
## possible i Python. 

#! Variable length argument is written with a '*' symbol before it in func definition

#* def add(farg, *args):

## Here 'farg' stands for formal argument and *args represents variable length arg

## We can pass 1 or more values to this 'args' and it will store them all in a tuple

# def add(farg, *args):
#     '''to add given numbers'''
#     print('Formal argument= ', farg)
    
#     sum =0
#     for i in args:
#         sum += i
#     print('Sum of all numbers = ', (farg+sum))
    
# #* call add() and pass arguments

# add(5, 10)
# add(5, 10, 20, 30)


#* def display(farg, **kwargs):

#! here '**kwargs' is called keyword argument. 

## Keyword internally represents a dictionary object.

## it means when we provide values for '**kwargs', we can pass multiple pairs of
## values using keyword as:

#* display(5, rno=10)

## Here 5 is stored as 'farg'. 'rno' is stored as key and its value '10' is stored
## as value in the dictionary that is referenced by 'kwargs'.

# def display(farg, **kwargs):
#     '''to display given values'''
#     print('Formal argument = ', farg)
    
#     for x,y in kwargs.items():                  ## items() will give pairs of items
#         print('Key = {}, Value = {}'.format(x,y))
        
# #* pass 1 formal argument and 2 keyword arguments

# display(5, rno=10)
# print()

# #* pass 1 formal argument and 4 keyword arguments

# display(5, rno=10, name='Shekhar')

#@ Local and Global variables

## When a variable is declared inside a function, it becomes a local variable.
## A local variable value is available only in that function and not outside
## that function.

# def myfunction():
    
#     a=1     #* this is a local variable
#     a+=1    #* increment it by 1
#     print(a)        #* displays 2
    
# myfunction()
# print(a)        #* 'a' is not defined 

## When a variable is declared above a function, it becomes a global variable.
## such variables are available to all the functions written after it.

# a=1

# def myfunction():
    
#     b=2     #* this is a local var
#     print('a = ',a)
#     print('b = ',b)
    
# myfunction()
# print(a)
# print(b)       #* 'b' is not defined

#@ Global keyword

# a = 1

# def myfunction():
#     a=2         #* This is a local var
#     print('a =', a)     #* Display local var
    
# myfunction()
# print('a =',a)         #* display global var

## To use global variable inside a function, use the keyword 'global' before the
## variable in the beginning of the function body.

#*  global a

# a = 1

# def myfunction():
#     global a        #* this is a global var
#     print('global a= ', a)      #* display global var
    
#     a = 2           #* modify global variable value
#     print('modified a= ',a)     #* display new value

# myfunction()
# print('global a= ',a)

#@ same name for global and local var

# a=1

# def myfunction():
    
#     a=2         #* This is a local var
#     x = globals()['a']      #* get global var into x
#     print('global var a= ',x)
#     print('local var a= ',a)
    
# myfunction()
# print('global var a= ',a)

#@ function to accept a group of numbers & their total average

# def calculate(lst):
#     '''To find total & average'''
#     n = len(lst)    
#     sum=0   
#     for i in lst:
#         sum += i
#         avg = sum/n
#         print(i, end=' ')
#     return sum, avg
    
# lst = [int(x) for x in input('Enter numbers: ').split()]
    
# x, y = calculate(lst)
# print('\nTotal = ', x)
# print('Average = ', y)

#@ accept a group of strings from keyboard and display them using display()

# def display(lst):
#     '''To display strings'''
#     for i in lst:
#         print(i, end=' ')

# lst = [x for x in input('Enter strings separated by comma: ').split(',')]

# display(lst)

#@ Recursive Functions

#! A function that calls itself is known as 'recursive function'.

## factorial(3) = 3 * factorial(2) = 3 * 2 * factorial(1)
## = 3 * 2 * 1 * factorial(0) = 3 * 2 * 1 * 1 = 6

# #* factorial(n) = n * factorial(n-1)

# def factorial(n):
#     '''To find factorial of n'''
#     if n==0:
#         result =1
#     else:
#         result = n*factorial(n-1)
#     return result

# for i in range(1,11):
#     print('Factorial of {} is {}'.format(i, factorial(i)))

#@ Tower of Hanoi problem

#* def towers(n, a, c, b): 
## n represents number of disks to move
## Variables a,c,b indicate that the disks needs to be moved from pole A to Pole C by
## taking help of intermediate pole B


def towers(n, start, end, aux):
    print(f' DEBUG: starting hanoi ({n}, {start}, {aux}, {end})')    
    ## towers(n, source, destination, auxillary)
    if n==1:            #* This is known as base case
        print(' Move disk %i from pole %s to pole %s' % (n,start,end))
    else:
        towers(n-1,start,aux,end)
        print('Move disk %i from pole %s to pole %s' % (n, start, end))
        towers(n-1, aux,end,start)
    print(f'DEBUG: Exiting hanoi ({n}, {start}, {end}, {aux})')     

n = int(input('Enter number of disks: '))
towers(n, 'Start', 'End', 'Aux')  ## call the function
 
#!  Move disk 1 from pole Start to pole End
#! Move disk 2 from pole Start to pole Aux
#!  Move disk 1 from pole End to pole Aux
#! Move disk 3 from pole Start to pole End
#!  Move disk 1 from pole Aux to pole Start
#! Move disk 2 from pole Aux to pole End
#!  Move disk 1 from pole Start to pole End

#&  DEBUG: starting hanoi (3, Start, Aux, End)
#&  DEBUG: starting hanoi (2, Start, End, Aux)
#&  DEBUG: starting hanoi (1, Start, Aux, End)
#&  Move disk 1 from pole Start to pole End
#& DEBUG: Exiting hanoi (1, Start, End, Aux)
#& Move disk 2 from pole Start to pole Aux
#&  DEBUG: starting hanoi (1, End, Start, Aux)
#&  Move disk 1 from pole End to pole Aux
#& DEBUG: Exiting hanoi (1, End, Aux, Start)
#& DEBUG: Exiting hanoi (2, Start, Aux, End)
#& Move disk 3 from pole Start to pole End
#&  DEBUG: starting hanoi (2, Aux, Start, End)
#&  DEBUG: starting hanoi (1, Aux, End, Start)
#&  Move disk 1 from pole Aux to pole Start
#& DEBUG: Exiting hanoi (1, Aux, Start, End)
#& Move disk 2 from pole Aux to pole End
#&  DEBUG: starting hanoi (1, Start, Aux, End)
#&  Move disk 1 from pole Start to pole End
#& DEBUG: Exiting hanoi (1, Start, End, Aux)
#& DEBUG: Exiting hanoi (2, Aux, End, Start)
#& DEBUG: Exiting hanoi (3, Start, End, Aux)


#! Hanoi Tower Step by step explanation:

#! The loop starts with n = 3 and since n != 1, straight jumps to 'else' cond.
#! with status as (3, start, Aux & End), goes back to call function.

#! Now function loops again to 'else' cond as n != 1 and status as (2, Start, End, Aux)
#! which it got from call function input.

#! Now as n becomes 1 and its status changes again from (2, start, end, aux) to
#! (1, start, aux, end), it jumps out of the loop after printing the result from 'if' cond

#! Now the 'else' has starting position as (2, start, end, aux) received from call cond.
#! This then changes the print variables from (n, start, end) to (n, start, aux).
#! Note. print condition under 'else' is programmed to accept only first and last
#! variables from status and prints - Move disk 2 from pole Start to pole Aux.

#! Next, the loop moves to the next line in 'else' cond where n becomes 1
#! and jumps straight to call function with status as (1, End, Start, Aux)
#% This is due to the fact that in the previous loop under 'else' cond, the loop
#% had started from variable start and went on to the 'end' variable.

#% Hence when the n became 1 for the second time, the loop right shifted to start from
#% (End, Start, Aux) i.e. start at the end and end at the Aux.

#! As the n has become 1 once again, the loop jumps back to 'if' cond and prints
#! 'Move disk 1 from pole End to pole Aux' as only 1st and last variables taken for print






#@ Anonymous function or Lambdas

## A function() without name is called 'Lambda or Anonymous Function'

#* def square(x):
#*     return x*x       This is normal or regular function with a defined name

#* lambda x: x*x        This is a lambda function

#* lambda argument_list: expression (function body)

# f = lambda x: x*x           ## Lambda function
# value = f(5)                ## Call lambda function

# print('Square of 5: ',value) 

#@ Lambda function to calculate sum of two function

# f = lambda x,y : x+y
# z = f(1.5, 10)

# print('Sum is: ', z)

#@ Lambda function to find bigger number among two given number

# max = lambda x, y : x if x > y else y       ## Lambda Function

# a,b = [int(n) for n in input('Enter two numbers: ').split(' ')]
# print('Bigger Number = ', max(a,b))         ## Calling lambda function


#@ Using Lambda with filter() function

#* filter(function.sequence)

## Here function may return either True or False. 
## A sequence represents a list, string or tuple
## function is applied to every elements of the sequence

#* function inside filter() to test odd even number

# def is_even(x):
#     if x%2 == 0:
#         return True
#     else:
#         return False

# lst = [10, 23, 45, 46, 70, 99]

# lst1 = list(filter(is_even, lst))

# print(lst1)


# #@ Rewrite using Lambda function

# lst = [10, 23, 45, 46, 70, 99]

# f = list(filter(lambda x: (x%2 == 0),lst))

# print(f)



#@ Using Lambda with map() function

#*     map(function.sequence)      It iterates through the list

#@  Find squares of elements in the list

# def squares(x):
#     return x*x
# lst = [1, 2, 3, 4, 5]

# lst1 = list(map(squares,lst))       

# print(lst1)


# #@ Finding squares of elements using lambda function

# lst = [1, 2, 3, 4, 5]

# f = list(map(lambda x: (x*x), lst))

# print(f)


## Map() on more than 1 list

#*   map(lambda x, y: x*y, lst1, lst2)


# #@ Find products of elements of two lists

# lst1 = [1, 2, 3, 3, 5]
# lst2 = [10, 20, 30, 40, 50]         #! Both lists have to be of same length

# lst3 = list(map(lambda x, y: x*y, lst1, lst2))

# print(lst3)

#@ Using Lambdas with reduce() function

#    #* reduce(function, sequence)

# from functools import *

# lst = [1, 2, 3, 4, 5]

# result = reduce(lambda x,y: x*y, lst)       #! reduce() belongs to functools

# print(result)


#@ another example of reduce()

# sum = reduce(lambda a, b: a+b, range(1, 51))
# print(sum)


#@ Function Decorators

#* Function decorator is a function that accepts function as parameters and returns a
#* function.

# def decor(fun):
#     def inner():
#         value = fun()       #* access value returned by fun()
#         return value + 2    #* Increase the value by 2
#     return inner            #* returns the output of the inner function to decor()

# def num():
#     return 18

# ## Call decorator function and pass num

# result_fun = decor(num)     ## result_fun represents inner function()

# print(result_fun())


# @decor                      ## apply decorator decor to foll function()
# def num():
#     return 1959

# print(num())


# #@ Another example of Decor function

# def decor(fun):
#     def inner():
#         value = fun()
#         return value + 18
#     return inner

# @decor          ## Add decor to the below function
# def num():
#     return 25

# print(num())

#@ Create 2 decorators

#* A decorator that increments the value of a function by 20

# def decor(fun):
#     def inner():
#         value = fun()
#         return value + 20
#     return inner

# #* A decorator that doubles the value of a function

# def decor1(fun):
#     def inner():
#         value = fun()
#         return value*2
#     return inner

# ## Function to which the above decorators are applied

# def num():
#     return 10

# result_fun = decor(decor1(num))

# print(result_fun())


#@ Apply two decorators to num() using @ symbol.

# def decor(fun):
#     def inner():
#         value = fun()
#         return value+20
#     return inner

# def decor1(fun):
#     def inner():
#         value = fun()
#         return value*2
#     return inner

# @decor
# @decor1

# def num():
#     return 100

# print(num())


#@ Generators

# def mygen(x,y):
#     while x <= y:
#         yield x
#         x +=1         ## yield returns the final value to the function mygen
        
# g = mygen(5, 10)

# # for i in g:         
# #     print(i, end=' ')

# # To store the values obtained from generator into list:    

# # lst = list(g)

# print(next(g))      ## next() display the first element from the list.
# print(next(g))      ## To display the remaining element, repeatedly call the next()
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

#@ Generator that returns characters from A to C.

# def mygen():
#     yield 'A'
#     yield 'B'
#     yield 'C'
    
# g = mygen()

# print(next(g))
# print(next(g))
# print(next(g))

#@ Structured Programming

#@ python program to calculate gross salary and net salary of an employee

# #! dearness allowance

# def da(basic):
#     '''da is 80% of basic salary'''
#     da = basic*0.8
#     return da

# #! House rent allowance

# def hra(basic):
#     '''hra is 15% of basic'''
#     hra = basic*0.15
#     return hra

# #! Provident Fund

# def pf(basic):
#     '''pf is 125 of basic'''
#     pf = basic*0.12
#     return pf

# #! Income Tax

# def it(gross):
#     '''10 % of gross'''
#     it = gross*0.1
#     return it

# #@ This is the main program

# #! Calculate the gross salary

# basic = float(input('Enter your basic salary: '))

# gross = basic + da(basic) + hra(basic)
# print('Your gross salary is: {:10.2f}'.format(gross))

# #! Calculate net salary

# net = gross - pf(basic) -it(gross)
# print('Your net salary is: {:10.2f}'.format(net))