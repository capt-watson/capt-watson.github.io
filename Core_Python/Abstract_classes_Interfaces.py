
#! An abstract method is a method whose action is redefined in the sub classes as per the
#! requirements of the objects.They do not have method body.

#~ To mark a method as abstract, we should use the decorator @abstractmethod. 
#~ Abstract method usually do not have body

#% A concrete method is a method with body.

#! A class with an abstract method is called an Abstract class.

#% All abstract classes should be derived from meta class ABC which belongs to abc
#% (abstract base class) module. Hence we should import this module into our program.

#! A meta class is a class that defines the behavior of the other classes.

#% Exercise

#* Program to create an abstract class and sub classes which implement the abstract method
#* of the abstract class.

# from abc import ABC, abstractmethod
# import math

# class MyClass(ABC):
#     @abstractmethod
#     def calculate(self, x):
#         pass        ## Empty body, no code
    
# ## This is sub class of MyClass

# class Sub1(MyClass):
#     def calculate(self, x):
#         print('Square Value= ',x*x)
        
# ## This is another sub class of MyClass

# class Sub2(MyClass):
#     def calculate(self, x):
#         print('Square Root= ',math.sqrt(x))
        
# ## This is one more sub class of MyClass

# class Sub3(MyClass):
#     def calculate(self, x):
#         print('Cube Value= ',x**3)
        
# ## Create Sub1 class object and call calculate() method

# obj1 = Sub1()
# obj1.calculate(16)

# ## Create Sub2 class object and call calculate() method

# obj2 = Sub2()
# obj2.calculate(16)

# ## Create Sub3 class object and call calculate() method

# obj3 = Sub3()
# obj3.calculate(16)

#! A program to create a Car Abstract class that contains an instance variable,
#! a concrete method and two abstract methods

# from abc import ABC, abstractmethod

# class Car(ABC):
#     def __init__(self, regno):
#         self.regno = regno
        
#     def openTank(self):         ## This is a concrete method
#         print('Fill up the Fuel into the tank')
#         print('For the car with reg. no: ', self.regno)
        
#     @abstractmethod
#     def steering(self):
#         pass
    
#     @abstractmethod
#     def breaking(self):
#         pass

# ## This is a sub class for abstract Car class

# class Maruti(Car):
#     def steering(self):
#         print('Maruti uses manual steering')
#         print('Drive the car')
        
#     def breaking(self):
#         print('Maruti uses hydraulic breakes')
#         print('Apply breaks and stop it')
        
# ## Create an object to Maruti and use its features

# m = Maruti(2000)
# m.openTank()
# m.steering()
# m.breaking()

# ## This is a sub class for abstract Car class

# from abs import Car

# class Santro(Car):
#     def steering(self):
#         print('Santro Uses Power steering')
#         print('Drive the car safely')
        
#     def breaking(self):
#         print('Santro uses air breaks')
#         print('Apply the breaks & stop the car')
        
# ## Create an object to santro and use its features

# s = Santro(2209)
# s.openTank()
# s.steering()
# s.breaking()


#@ Interfaces in Python

#! Program to develop an interface that connects to any database

#& Interface is nothing but the sub classes which actually perform
#& the task.

# from abc import ABC, abstractmethod

# class MyClass(ABC):
#     @abstractmethod
#     def connect(self):      ## Defining method headers only. No body
#         pass
    
#     @abstractmethod
#     def disconnect(self):  ## Defining method headers only. No body
#         pass
    
# ## This is a sub class which acts as an interface. This interface is provided by Third Party
# ## vendors. For e.g here Oracle Corp will provide a sub class where the code related to
# ## connecting and disconnecting with their database will be provided as given below:

# class Oracle(MyClass):
#     def connect(self):
#         print('Connecting to Oracle Database')
        
#     def disconnect(self):
#         print('Disconnecting from Oracle Database...')
        
# ## This is an another sub class acting as an interface. This interface is provided by Third Party
# ## vendors.For e.g here Sybase Corp will provide a sub class where the code related to
# ## connecting and disconnecting with their database will be provided as given below:

# class Sybase(MyClass):
#     def connect(self):
#         print('Connecting to Sybase Database...')
        
#     def disconnect(self):
#         print('Disconnecting from Sybase database...')
        
# class Database:
#     ## Accept database name as a string from the user
#     str = input('Enter Database name: ')
    
#     ## Convert this string into a classname
#     Classname = globals()[str]
    
#     ## Create an object to this class
#     x = Classname()
    
#     ## call the connect() & disconnect methods
#     x.connect()
#     x.disconnect()
    
    #~ We assume that the printer name is generally stored in the config.txt file at the
    #~ time of installing the printer driver software.
    
    #% So open a notepad and create a file with the name config.txt and store a single
    #% that represents the printer driver name as: Epson
    
    #% and then save the file. Alternatively, we can store the name IBM in the config.txt
    #% file. 
    
    #! The name of the printer available in the config.txt file can be read from the file
    #! using readline() method as:
    
    #* with open('config.txt', 'r') as f:
    #*      str = f.readline()           ## read printer name from 'f' and store into str.
    
    #% This reads one line from the file containing the string 'Epson' which was already
    #% stored by us in the config.txt file.
    
    #! Python program which contains a printer interface and its sub classes to send text
    #! to any printer
    
from abc import ABC,  abstractmethod
    
## Create an interface
    
class Printer(ABC):
     @abstractmethod
     def printit(self, text):
         pass
     
     @abstractmethod
     def disconnect(self):
         pass
     
## This is sub class for IBM printer

class IBM(Printer):
    def printit(self, text):
        print(text)
        
    def disconnect(self):
        print('Printing completed on IBM printer')

## This is sub class for Epson printer

class Epson(Printer):
    def printit(self, text):
        print(text)
        
    def disconnect(self):
        print('Printing completed on Epson Printer')
        
class UsePrinter:
    ## Accept printer name as a string from configuration file
    with open("config.txt", "r") as f:
        str = f.readline()

#     ## Convert the string into classname    
    classname = globals()[str]

## Create an object to this class

    x = classname()

## Call the printit() and disconnect() methods

    x.printit('Hello, your document has been sent to the printer')
    x.disconnect()

#@ Abstract class vs Interfaces

#! Generally, abstract class is written when there are some common
#! features shared by all the objects as they are.

#% on the other hand, the programmer uses an interface if all the
#% features need to implemented differently for different objects.

#& In this case, the programmer designs the Whole seller as an
#& interface and Retailers and Retailer 2 become sub classes.
