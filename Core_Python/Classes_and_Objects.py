## General format

## class Classname(object):
##    '''docstring describing the class'''
##    attributes
##    def __init__(self):
##    def method1():
##    def method2():

#@ Creating a Class

#! A class is with the keyword 'class' and then writing the classname.
#! After the classname, 'object' is written inside (parenthesis).
#! This object represents base class name.
#! Writing 'object' is not compulsory since it is implied.

#* Instance variables and instance method
# class Student:
#     #* This is a special method called constructor.
#     #* The below block defines attributes
#     def __init__(self):
#         self.name = 'Sushama Upadhyay'
#         self.age  = 60
#         self.marks = 900
        
# #* This is an instance method.
# #* The below block defines a method
#     def talk(self):
#         print('Hi, I am',self.name)
#         print('My age is',self.age)
#         print('My marks are',self.marks)

# #* creates an instance of student class. Here s1 is instance name.
# s1 = Student()

# #* Calls the method using the instance
# s1.talk()


#@ Constructor

#* A constructor is a special method that is used to initialize the
#* instance variables of a class.

#! In the constructor, we create the instance variables and initialize 
#! them with some starting values.

#! The first parameter of the constructor will always be 'self' variable
#! that contains the memory address of the instance.

#% A constructor is called at the time of creating an instance. e.g given below:
#% s1 = student()

#% Here s1 is the name of the instance.

#% The empty parenthesis after the class name 'Student'. This empty parentheses represent
#% that we are not passing any values to the constructor.

#* Create a student class with a constructor having more than one parameter.

# class Student:
#     def __init__(self, n= '', m=0):
#         self.name = n
#         self.marks = m
#     ## Given below is an instance method
#     def display(self):
#         print('Hi',self.name)
#         print('Your Marks are',self.marks)
        
# s = Student()

# ## constructor is called without any arguments


# s.display()

# ## Constructor is called with 2 arguments

# s1 = Student('Shekhar Upadhyay',990)
# s1.display()

#@ Self Variable

#! 'Self' is a default variable that contains the memory address of the instance of the
#! current 'class'.

#! We use 'self' to refer to all the instance variables and instance methods.

#! When an instance is created, the instance name e.g. s1 = student(). Here 's1' contains
#! the memory location of the instance. This memory location is internally and by default
#! passed to 'self'.

#! Since 'self' knows the memory address of the instance, it can refer to all members of the
#! instance. for e.g

#% def __init__(self)

#! Here, 'self' can be used to refer to the instance variables inside the constructor.
#! e.g. 'Sushama Upadhyay, 60 & 900

#! 'self' can be used as first parameter in the instance method as:

#% def talk(self)

#! Here talk() is instance method as it acts on the instance variables. If this method wants
#! to act on the instance variables, it should know the memory location of the instance
#! variables. That memory location is by default available to the talk() method through 'self'

#@ Constructor

#! A constructor is a special method that is used to initialize the instance variables of a
#! class.

#! The first parameters of the constructor will always be 'self' variable that contains the
#! the memory address of the instance. e.g:

#% def __init__(self):
#%      self.name = 'Vishnu'
#%      self.marks = '900'

#! in the above examples, the constructor will be called when an instance s1 = Student() is
#! created. Instance variable 'name' takes the memory address of the instance from 'self' 
#! and stores the variable 'Vishnu' in it.

#! To pass some values to the constructor, we can write a constructor with some parameters
#! in addition to 'self' as:

#% def __init__(self, n= '', m=0):
#%      self.name = n
#%      self.marks = m

#! here 'n' and 'm' are 'formal' arguments whose default value is given as 'none' & 0 (zero)
#! If we do not pass any values to constructor at the time of creating an instance, the
#! default values of these formal arguments are stored into 'name' and 'marks' variables.
#! e.g. output:

#~ Hi 
#~ Your Marks are 0

#! when we pass 'actual' arguments to the constructor, the arguments 'n' and 'm' are stored
#! into name and marks variables.

#% s1 = Student('Shekhar Upadhyay', 900)
#% s1.display()

#~ Hi Shekhar Upadhyay
#~ Your Marks are 990

#@ Types of Variables

#! Instance Variables
#! Class Variables or Static variables

#@ Instance variables

#! Instance variables are defined and initialized using a constructor with 'self'
#! parameter. 

#! To access instance variables, we need instance methods with 'self' as first parameter.

# class Sample:
#     def __init__(self):
#         self.x = 10
        
#     def modify(self):
#         self.x += 1

# s1 = Sample()
# s2 = Sample()

# print('x in s1= ',s1.x)
# print('x in s2= ',s2.x)

# #% modify x in s1

# s1.modify()

# print('x in s1= ',s1.x)
# print('x in s2= ',s2.x)

#~ Output:

#~ x in s1=  10
#~ x in s2=  10
#~ x in s1=  11
#~ x in s2=  10

#@ Class Variables 

#! Unlike instance variables, class variables are the variables whose single copy available
#! to all instances of the class. 

#! If one copy of the class variable in an instance is modified, it will modify all the
#! copy of in other instances.

#! for e.g. if 'x' is a class variable and we create 3 instances, the same copy of 'x' is
#! passed to these 3 instances. When we modify the 'x' in any instance using a 'class method'
#! the modified copy is sent to other two instances.

#! in the example given below, the class variable 'x' is defined in the class and & initialized
#! with value 10. 

#! A method by name 'modify' is used to modify the value of 'x'. This method is called
#! 'class method' since it is acting on the class variable.

#! To mark this method as class method, we should use built-in decorator statement @classmethod.

#! class variables are defined directly in the class.

#! To access class variables from outside the class, use: classname.variable e.g Sample.x

# class Sample:
    ## this is a class variable
    # x = 10
    
    # ## This is a class method
    # @classmethod            ## This is a decorator
    # def modify(cls):        ## 'cls' must be first parameters
    #     cls.x += 1          ## 'cls' refers to class variable
        
## create 2 instances

# s1 = Sample()
# s2 = Sample()

# print('x in s1= ', s1.x)
# print('x in s2= ', s2.x)

# ## modify x in s1

# s1.modify()
# print('x in s1= ', s1.x)
# print('x in s2= ', s2.x)

#~ x in s1=  10
#~ x in s2=  10
#~ x in s1=  11
#~ x in s2=  11

#@ Namespaces

#% A namespace represents a memory block where names are mapped (or linked) to objects.

#! A class maintains its own namespace, called 'class namespace'.
#! In the class namespace, the names are mapped to class variables.

#! Similarly, every instance will have its own namespace, called 'instance namespace'. In the
#! instance namespace, the names are mapped to instance variables.

#@ Types of Methods

#% Instance Methods

#% (a) Accessor methods
#% (b) Mutator methods

#% Class method

#% Static Method

#@ Instance method

#% Exercise

#* Student class with instance methods to process the data of several students

# class Students:
#     ## This is constructor
#     def __init__(self, n = '', m= 0):
#         self.name = n
#         self.marks = m
        
#     ## This is instance method
#     def display(self):
#         print('Hi' , self.name)
#         print('Your marks are:', self.marks)
    
#     ## calculate grades based on marks
#     def calculate(self):
#         if self.marks >= 600:
#             print('You got First Class\n')
#         elif self.marks < 600 and self.marks >= 500:
#             print('You got Second Class\n')
#         elif self.marks < 500 and self.marks >= 350:
#             print('You got Third Grade\n')
#         else:
#             print('You have got screwed\n')
            

# ## Create an instance object with some data from the user

# n = int(input('how many students: '))

# for i in range(n):
#     name = input('Enter Your name')
#     marks = int(input('Enter your Marks: '))            
#     s = Students(name, marks)
#     s.display()
#     s.calculate()
#     i += 1
    
#@ Accessor & mutator method

#% Exercise

#* Using Mutator method to store data and assessor method to retrieve data from instance.

# class Student:    
#         ## mutator Method
#     def setname(self, name):
#         self.name = name
        
#     ## Accessor Method
#     def getname(self):
#         return self.name
    
#     ## mutator method
#     def setmarks(self, marks):
#         self.marks = marks
        
#     ## accessor method
#     def getmarks(self):
#         return self.marks
    
# ## Create an instance with user provided data

# n = int(input('How many students'))

# for i in range(n):
#     s = Student()
#     name = input('Enter Your Name:')
#     s.setname(name)
#     marks = int(input('Enter Your marks'))
#     s.setmarks(marks)

# ## retrieve data using Student Class Instance
#     print('Hi',s.getname())
#     print('Your marks are:',s.getmarks(),'\n')
#     i += 1
    
#@ Class method

#% Exercise

#! Use class method to handle the common feature of all the instance of Bird class.

# class Bird:
#     ## This is a class var
#     wings = 2
    
#     ## This is a class method
#     @classmethod
#     def fly(cls, name):
#         print('{} flies with {} wings'.format(name, cls.wings))
        
# ## Display information for 2 birds

# Bird.fly('Hawk')
# Bird.fly('Sparrow')

# #@ Static Methods

#! Static methods are used when some processing is related to the class but does not need the
#! class or its instances to perform any work.

#! e.g: Counting number of instance var, changing an attribute in another class etc

#! A static method accepts some value, process them & returns the result.

#% Static methods are written with a Decorator @staticmethod above them

#% Static methods are  called by classname.method().

#% Exercise

#! Create a static method that counts the number of instances created for a class.

# class Myclass:
#     ## This is a class var or static var
#     n=0
    
#     ## Constructor that increments n when instance is created
    
#     def __init__(self):
#         Myclass.n = Myclass.n+1
        
#     ## This is a static method to display the no. of instances
#     @staticmethod
#     def noObjects():
#         print('No. of instances created: ', Myclass.n)
        
# ## create 3 instances

# obj1 = Myclass()
# obj2 = Myclass()
# obj3 = Myclass()

# Myclass.noObjects()

#% exercise

#! Create a static method that calculates the square root value of a given number

# import math

# class Sample:
#     @staticmethod
#     def calculate(x):
#         result = math.sqrt(x)
#         return result
    
# ## Accept a number from the user

# num = float(input('Enter a number: '))

# ## Call the static method and pass num

# res = Sample.calculate(num)
# print('The Square Root of {} is {:.2f}'.format(num, res))

#% Exercise

#! Create a Bank class where deposits and withdrawal can be handled by using instance methods.

# import sys

# class Bank(object):
#     ## bank related transactions
    
    ## To initialize name and balance instance vars
    # def __init__(self, name, balance=0.0):
    #     self.name = name
    #     self.balance = balance
        
    # ## To add deposit amount to balance
    
    # def deposit(self, amount):
    #     self.balance += amount
    #     return self.balance
    
    # ## to deduct withdrawal amount from balance
    
    # def withdrawal(self, amount):
    #     if amount > self.balance:
    #         print('You do not have enough balance, so no withdrawal')
    #     else:
    #         self.balance -= amount
    #     return self.balance
    
## using the Bank Class

## Create an account with the given name and balance 0.00

# name = input('Enter Your name: ')

# b = Bank(name)

# while True:
#     print('d - Deposit, w- Withdrawal, e-Exit')
#     choice = input('Enter what would you like to do? ')
#     if choice == 'e' or choice == 'E':
#         sys.exit()
#     ## Amount to be deposited or withdrawal
#     amt = float(input('Enter deposit or withdrawal amount: '))
    
#     ## Do the transaction
#     if choice == 'd' or choice== 'D':
#         print('Balance after deposit: ',b.deposit(amt))
#     elif choice == 'w' or choice == 'W':
#         print('Balance after withdrawal: ',b.withdrawal(amt))
        
#@ Passing members of one class to another class

#! create Emp class and make all the members of the emp class available to another class
#! i.e. to 'MyClass'

# class Emp:
#     ## This is a constructor
#     def __init__(self, id, name, salary):
#         self.id = id
#         self.name = name
#         self.salary = salary
    
#     ## this is an instance method
#     def display(self):
#         print('Id: ',self.id)
#         print('Name: ', self.name)
#         print('Salary: ',self.salary)
        
    
# ## this class displays emp details
# class Myclass:
#     ## method to receive Emp details
#     @staticmethod
#     def mymethod(e):
#         ## increment salary of e by 5000
#         e.salary += 5000
#         e.display()
        
# ## create Emp class instance e
# e = Emp(10, 'Raj Kumar', 45000)

# ## Call static method of Myclass and pass e

# Myclass.mymethod(e)

#! Calculate power value of a number with the help of a static method

# class Myclass:
#     ## method to calculate x to the power of n
#     @staticmethod
#     def mymethod(x, n):
#         result = x**n
#         print('{} to the power of {} is {}'.format(x, n, result))
        
# ## Call the static method
# Myclass.mymethod(5, 3)
# Myclass.mymethod(5, 4)


#@ Inner class

#! Create DOB class within Person class

# class Person:
#     def __init__(self):
#         self.name = 'Charles'
#         self.db = self.Dob()
        
#     def display(self):
#         print('Name: ', self.name)
        
        
#     ## This is inner class
    
#     class Dob:
#         def __init__(self):
#             self.dd = 18
#             self.mm = 5
#             self.yy = 1959
            
#         def display(self):
#             print('DOB = {} {} {}'.format(self.dd, self.mm, self.yy))
            
        
# ## Creating a person class object

# p = Person()
# p.display()

## Creating inner class object

# x = p.db
# x.display()

#@ Another example of inner class

class Person:
    def __init__(self):
        self.name = 'Charles'
        
    def display(self):
        print('Name: ', self.name)
        
    ## This is inner class
    class Dob:
        def __init__(self):
            self.dd = 18
            self.mm = 5
            self.yy = 1959
        
        def display(self):
            print('DoB is= {}/{}/{}'.format(self.dd, self.mm, self.yy))
            
## creating a person class object

p = Person()
p.display()

## Create DoB class object as sub object to person class object

x = Person().Dob()
x.display()
print(x.yy)     ## displays only the year