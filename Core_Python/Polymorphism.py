
## If a variable object or method exhibits different behavior in
## different contexts, it is called polymorphism.

## Python has built-in polymorphism.

## Polymorphism in Python:

## Duck typing philosophy of Python

## Operator overloading

## Method overloading

## Method overriding

#@ Duck typing philosophy of Python

#% Python variables are names or tags that point to memory locations where data is stored.

#* duck typing example

## Dog Class contains bark() method

# class Dog:
#     def bark(self):
#         print('Bow, Wow!')
        
# ## Duck class contains talk() method

# class Duck:
#     def talk(self):
#         print('Quack, quack!')
        
# ## Human class contains talk() method

# class Human:
#     def talk(self):
#         print('Hello, Hi!')
        
# ## This method accepts an object and calls talk() method

# def call_talk(obj):
#     obj.talk()
    
# ## Call call_talk() method and pass an object

# x = Duck()
# call_talk(x)

# x = Human()
# call_talk(x)

# x = Dog()
# call_talk(x)

#~ Quack, quack!
#~ Hello, Hi!
#~ AttributeError: 'Dog' object has no attribute 'talk'

#@ Checking the object type(or class) is called 'Strong Typing.' Previous example was
#@ 'Duck Typing'

#% hasattr(object, attribute)

# def call_talk(obj):
#     if hasattr(obj, 'talk'):    ## if obj has talk() method then
#         obj.talk()              ## call it on the object
#     elif hasattr(obj, 'bark'):  ## if obj has bark() method then
#         obj.bark()              ## call it
        
#% Exercise

#! program to check the object type to know whether the method exists in object or not.

#* Strong Typing Example

# class Dog:
#     def bark(self):
#         print('Bow, wow!')
        
# class Duck:
#     def talk(self):
#         print('Quack, quack!')
        
# class Human:
#     def talk(self):
#         print('Hello, Hi!')
        
# ## This method accepts an object and calls talk() method

# def call_talk(obj):
#     if hasattr(obj, 'talk'):
#         obj.talk()
#     elif hasattr(obj, 'bark'):
#         obj.bark()
#     else:
#         print('Wrong obj passed')

# ## Depending on type of object, talk() method is executed

# x = Duck()
# call_talk(x)

# x = Human()
# call_talk(x)

# x = Dog()
# call_talk(x)

#@ Operator Overloading

#! When an operator performs different actions, it is said to exhibit polymorphism.

#% Exercise

#* Use Addition operator to act on different types of objects

#* Overloading the operator
## Using + on integers to add them

# print(10+15)

# ## Using + on strings to concatenate them

# s1 = 'Red'
# s2 = ' Fort'

# print(s1+s2)

# ## Using + on lists to make a single list

# a = [10, 20, 30]
# b = [5, 15, -10]

# print(a+b)

#! If any operator performs additional actions than what it is meant for, it is called
#! 'operator overloading.'

#% Exercise

#! Program to overload the addition operator (+) to make it act on class objects.

# class BookX:
#     def __init__(self, pages):
#         self.pages = pages
        
#     def __add__(self, other):
#         return self.pages + other.pages 
    
# ## Here self.pages represents the numeric content of first class and other.pages represents
# ## the numeric content of second class
            
# class BookY:
#     def __init__(self, pages):
#         self.pages = pages
        
# b1 = BookX(100)
# b2 = BookY(150)

# print('Total Pages = ', b1+b2)

#% Operators & corresponding Magic Methods (To add object's attributes)

## Operator             Magic Method
##    +                 object.__add__(self, other)
##    -                 object.__sub__(self, other)
##    *                 object.__mul__(self, other)
##    /                 object.__div__(self, other)
##    //                object.__floordiv__(self, other)
##    %                 object.__mod__(self, other)
##    **                object.__pow__(self, other[,modulo])
##    +=                object.__iadd__(self, other)
##    -=                object.__isub__(self, other)
##    *=                object.__imul__(self, other)
##    /=                object.__idiv__(self, other)
##    //=               object.__ifloordiv__(self, other)
##    %=                object.__imod__(self, other[,modulo])
##    **=               object.__ipow__(self, other)
##    <                 object.__lt__(self, other)      lt means less than
##    <=                object.__le__(self, other)      le means less or equal to
##    >                 object.__gt__(self, other)      gt means greater than
##    >=                object.__ge__(self, other)      ge means greater than or equal to
##    ==                object.__eq__(self, other)      eq means equal to
##    !=                 object.__ne__(self, other)     ne means not equal to

#% Exercise

#! program to overload greater than (>) operator to make it act on class objects.

# class Ramayan:
#     def __init__(self, pages):
#         self.pages = pages
        
#     def __gt__(self, other):
#         return self.pages > other.pages
    
# class Mahabharat:
#     def __init__(self, pages):
#         self.pages = pages
        
# b1 = Ramayan(1000)
# b2 = Mahabharat(1800)

# if b1 > b2:
#     print('Ramayan has more pages')
# else:
#     print('Mahabharat has more pages')
    
    
#! Program to overload the multiplication (*) operator to act on objects

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
        
#     def __mul__(self, other):
#         return self.salary*other.days       ## Salary per day
    
# class Attendance:
#     def __init__(self, name, days):
#         self.name = name
#         self.days = days
        
# x1 = Employee('Raju', 1000.00)
# x2 = Attendance('Raju', 25)

# print('This month\'s salary = ',x1*x2)

#@ Method Overloading

#! If a method is written such that it can perform more than 1 task, it is called method
#! overloading

#@ As method overloading is not available in Python, we can achieve method overloading
#@ by writing same method with several parameters.

#@ In the example given below, sum() method is performing more than one task. Hence it is an
#@ overloaded method.

#% Exercise

#! Program to show method overloading to find sum of two or three numbers. 

# class MyClass:
#     def sum(self, a=None, b=None, c=None):
#         if a!= None and b != None and c!= None:
#             print('Sum of three numbers = ', a+b+c)
#         elif a!= None and b != None:
#             print('Sum of two= ',a+b)
#         else:
#             print('Please enter two or three arguments')
            
# ## Call sum using object

# m = MyClass()
# m.sum(100)
# m.sum(10.5, 25.55)
# m.sum(10, 15, 20)


#@ Method Overriding

#! When there is a method in the super class, writing the same method
#! in sub class so that it replaces the super class method, is called
#! 'method overriding.'

#% Exercise

#! Program to override the super class method in sub class

import math

class Square:
    def area(self,x):
        print('Square area = %.4f' % (x*x))
        
class Circle:
    def area(self, x):
        print('Circle area= %.4f' % (math.pi*x*x))

## call area() using sub class object

c = Circle()
c.area(15)

b = Square()
b.area(15)

## In the above example, area method is performing two different tasks
## depending on the object type. This is an example of polymorphism.

