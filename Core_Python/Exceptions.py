
#! Errors in Python

#*      Compile Time Errors
#*      Runtime Errors
#*      Logical Errors

#@ Compile Time Errors

#& These are syntactical errors found in the code.

#! Examples 1 - Compile Time - Typo error

# x = 1
# if x == 1       ## missing :
#      print('Where is colon?')

#~ Cell In[1], line 14
#~ if x == 1       ## missing :
#~ SyntaxError: expected ':'

#! Example 2 - Compile Time - Indentation Error

# x = 10
# if x%2 == 0:
#      print(x,' is divisible by 2')
#           print(x,'is even number')     ## Incorrect indentation
          
#~   Cell In[2], line 26
#~   print(x,'is even number')     ## Incorrect indentation
#~   IndentationError: unexpected indent

#@ Runtime Errors

#! Example of Runtime error

# def concat(a,b):
#      print(a+b)
     
# ## Call concat() and pass arguments
# concat('Hai', 25)

## since the data types are not the same, PVM shows 'TypeError'

#~ TypeError: can only concatenate str (not "int") to str

#! Another example of Runtime error

# animal = ['Dog', 'cat', 'Horse', 'Monkey']
# print(animal[4])

## As there is no element at index 4, PVM gives error

#~ IndexError: list index out of range

#@ Logical Errors

#& These errors depict flaws in the logic of the program/

#* Logical errors are not detected either by Python compiler PVM.

#! An example of logical error

# def increment(sal):
#      sal = sal*15/100
#      return sal

## Call increment() and pass salary

# sal = increment(12000)
# print('Incremented salary= %.2F'% sal)

# ## Since the increment in the salary is not added back to sal, we get:
# #~ Incremented salary= 1800.00

# ## However, if the increment is added back to the sal as shown below:
# ## we get the correct answer

# def increment(sal):
#      sal += sal*15/100
#      return sal

# sal = increment(12000)
# print('Incremented salary= %.2F'% sal)

#~ Incremented salary= 13800.00

#! Runtime errors which can be handled by the programmer are called exceptions.

#% Exercise

#! Understanding the effect of an exception

## Open a file

# f = open('myfile', 'w')

## do some processing on the file

## accept a,b values, store the result of a/b into the file

# a,b = [int(x) for x in input('Enter Two numbers: ').split()]

# c = a/b

# f.write('Writing %d into myfile' %c)

# ## close the file

# f.close()

# print('File Closed')

#~ Here the PVM detects this 'division by zero' error and terminates the program
#~ in line 104 at c = a/b.

#& This causes the opened file to be left open and hence posing data security risk

#@ Exceptions

#! An Exception is a runtime error which can be handled by the programmer.

#* If the programmer can guess an error in the program and can do something to
#* eliminate the harm caused by the error, then it is called an 'exception.'

# #% If the programmer can not do anything in case of an error, then it is called
#% an 'error' and not an 'exception.'

#! A program to handle the ZeroDivisionError exception

# try:
#      f = open('myfile','w')
#      a,b = [int(x) for x in input('Enter two numbers: ').split()]
     
#      c = a/b
#      f.write('Writing %d into myfile' %c)
     
# except ZeroDivisionError:
#      print('Division by zero happened')
#      print('Please do not enter 0 in the input')
     
# finally:
#      f.close()
#      print('File closed')
     
#% Python Built in exceptions list:

#! ArithmeticError       OverflowError, ZeroDivisionError, FloatingPointError

#! AssertionError        Raised when assert statement gives error

#! AttributeError        Raised when attribute reference or assignment fails

#! EOFError              Raised when input() reaches end of file condition without
#!                       reading any data.

#! FloatingPointError    Raised when floating point operation fails

#! GeneratorExit         Raised when generator's close() method is called

#! IOError               It is raised when the file opened is not found or when
#!                       writing data disk is full

#! ImportError           Raised when an import statement fails to find the module
#!                       being imported.

#! IndexError            Raised when a sequence index or subscript is out of range.

#! KeyError              Raised when a mapping dictionary key is not found in the
#!                       set of existing keys.

#! KeyboardInterrupt     Raised when the user hit the interrupt key () normally
#!                       Control+C or Delete

#! NameError             Raised when an identifier is not found locally or globally

#! NotImplementedError   Derived from 'RuntimeError'. In user defined base classes,
#!                       abstract methods should raise this exception when they
#!                       require derived classes to override the method.

#! OverflowError         Raised when the result of an arithmetic operation  is too
#!                       large to be represented. This can not occur for long integers
#!                       which would rather raise memory error.

#! RuntimeError          Raised when an error is detected that doesn't fall in any
#!                       of the other categories.

#! StopIteration         Raised by an iterator's next() method to signal that no more
#!                       elements.

#! SyntaxError           Raised when the compiler encounters a syntax error.
#!                       Import or exec statements and output() & eval() may raise this.

#! IndentationError      Raised when indentation is not specified properly.

#! SystemExit            Raised by sys.exit() function. When it is not handled, Python exits

#! TypeError             Raised when operation or function is applied to an object of
#!                       inappropriate type.

#! UnboundLocalError     Raised when reference is made to a local variable in a function
#!                       or a method, but no value has been bound to that variable.

#! ValueError            Raised when build-in operation or function receives an argument
#!                       that has right datatype but wrong value

#! ZeroDivisionError     Raised when the denominator is zero in a division or modulus ops

#% Exercise

#* A program to handle syntax error given by eval() function

# try:
#      date = eval(input('Enter date: '))
# except SyntaxError:
#      print('Invalid date entered')
# else:
#      print('You entered: ', date)
     
## eval() function accepts inputs in the form of list, tuple or dictionary and evaluates
## the input property.

## When a group of numbers are entered separating them by commas, they are understood as a
## tuple by eval() function.


#! A program to handle IOError produced by open() function.

# try:
#      name = input('Enter a file name: ')     ## Enter a filename.py from your file folder
#      f = open(name, 'r')
# except IOError:
#      print('File not found: ',name)
# else:
#      n = len(f.readlines())
#      print(name, 'has', n, 'lines')
#      f.close()
     
#! A python program to handle multiple  exceptions
## function to find total and average list of elements

# def avg(list):
#      tot = 0
#      for x in list:
#           tot += x
          
#      avg = tot/len(list)
#      return tot, avg

# ## Call the avg and pass the list

# try:
#      t,a = avg([1,2,3,4,5,6])
#      print('Total = {}, Average = {}'.format(t,a))
# except TypeError:
#      print('Type Error, please provide numbers. ')
# except ZeroDivisionError:
#      print('Zero Division Error, please do not give empty list')


#@ Except Block

#! A program to understand the usage of 'try' with 'finally' blocks

# try:
#      x = int(input('Enter a number: '))
#      y = 1 / x
# finally:
#      print('We are not catching the exception.')
     
# print('The inverse of',x, 'is: ',y)

#@ The assert Statement

#* The assert statement is useful to ensure that a given condition is True. If not True,
#* raises AssertionError.

#! A Python program using the assert statement & catching AssertionError

# try:
#      x = int(input('Enter a number between 5 and 10: '))
#      assert x >=5 and x <=10
#      print('The number entered is: ', x)
# except AssertionError:
#      print('Please enter number only between 5 & 10')

#! Python program to use the assert statement with a message

# try:
#      x = int(input('Enter a number between 5 & 10: '))
#      assert x >= 5 and x <= 10, 'Your entered number is not between 5 & 10'
#      print('The number entered is: ',x) 
# except AssertionError as obj:
#      print(obj)

#@ User defined exceptions

#! A Python program to create our own exception and raise it when needed

## Create our own class as a sub class to Exception class

class MyException(Exception):
     def __init__(self, arg):
          self.msg = arg
## Write code where this exception may raise
## to raise exception, use raise statement
def check(dict):
     for k,v in dict.items():
          print('Name= {:15s} Balance = {:10.2f}'.format(k,v))
          if v<2000.00:
               raise MyException('Balance amount is less than 2000 in the account of '+k)

bank = {'Raj': 5000.00, 'Aarav': 100000.00, 'Abdul': 1500.00}

try:
     check(bank)
except MyException as me:
     print(me)

#@ Logging the Exceptions

#! Logging of errors helps programmer debug the program effectively.

#* Python program that creates a log file with errors and critical messages.

# import logging

# ## store messages into mylog.txt file
# ## store only messages with level equal to or more than that of Error.

# logging.basicConfig(filename='mylog.txt', level=logging.ERROR)

# ## These messages are stored into the file

# logging.error('There is an error in the program.')
# logging.critical('There is a problem in the design')

# ## These logs are not stored

# logging.warning('The project is going slow.')
# logging.info('You are a junior programmer.')
# logging.debug('Line no. 10 contains syntax error.')

#! Python program to store the messages issued by any exception into the
#! file.

# import logging

# ## store logging messages into log.txt file

# logging.basicConfig(filename='log.txt', level=logging.ERROR )

# try:
#      a = int(input('Enter a number: '))
#      b = int(input('Enter another number: '))
#      c = a/b
# except Exception as e:
#      logging.exception(e)    ## Exception message is stored in obj 'e'
# else:
#      print('The result of division is: ',c)
