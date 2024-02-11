
#! Access the base class constructor from sub class

# class Father:
#     def __init__(self):
#         self.property = 20000000
        
#     def display_property(self):
#         print('Father\'s property = ', self.property)
        
# class Son(Father):
#     pass    ## We do not want to write anything in sub class.

# s = Son()

# s.display_property()

## Like variables and methods, the constructors in the super class are
## also available to the sub class object by default.


#@ Overriding Super Class Constructors and methods

#! Override super class constructor and method in sub class

# class Father:
#     def __init__(self):
#         self.property = 50000000
    
#     def display_property(self):
#         print('Father\'s property = ',self.property)
        
# class Son(Father):
#     def __init__(self):
#         self.property = 15000000
#     def display_property(self):
#         print('Child\'s property= ',self.property)
    
## create sub class instance and display father's property

# s = Son()
# s.display_property()

## In the above example, we created constructor and method with exactly
## same name as those of Super Class. 

## due to this, the base class constructor and method are not available
## to the sub class object (overridden)

#@ the super() method

#% Super() is a built in method which is useful to call the super class
#% constructor or methods from sub class. 

#* super().__init__()  ## call super class constructor
#* super().__init__(arguments) ## call super class constructor & pass arguments.
#* super().method()  ## call super class method

#% Exercise

#! Call the super class constructor in the sub class using super().

# class Father:
#     def __init__(self, property=0):
#       self.property = property
        
#     def display_property(self):     ## Overridden by son's display_property()
#         print('Father\'s property = ', self.property)
        
# class Son(Father):
#     def __init__(self,property1=0,  property=0):
#         super().__init__(property)
#         self.property1 = property1
        
#     def display_property(self):
#         print('Total property of child= ', self.property1 + self.property)
        
# s = Son(15000000, 250000000)
# s.display_property()

#! Access base class constructor and method in the sub class

# class Square:
#     def __init__(self, x):
#         self.x = x
        
#     def area(self):
#         print('Area of Square= ',self.x*self.x)
        
# class Rectangle(Square):
#     def __init__(self,x,y):
#         super().__init__(x)     ## Sends the value of x to the base  class for processing
#         self.y = y
        
#     def area(self):
#         super().area()      ## gets the area of square from base()
#         print('Area of Rectangle: ',self.x*self.y)
        
# a,b = [float(x) for x in input('Enter two measurements: ').split( )]

# r = Rectangle(a,b)
# r.area()

#@ Types of Inheritance

#! Deriving one or more subclasses from a single base is called 'Single Inheritance'.

#% Exercise

#! Program showing single inheritance. Here two sub classes are derived from a single base class.
# class Bank:
#     cash = 100000000
#     @classmethod
#     def available_cash(cls):
#         print(cls.cash)
        
# class BoB(Bank):
#     pass

# class SBI(Bank):
#     cash = 20000000
#     @classmethod
#     def available_cash(cls):
#         print(cls.cash + Bank.cash)
        
# a = BoB()
# a.available_cash()

# s = SBI()
# s.available_cash()

#@ Multiple Inheritance

#% Deriving sub classes from multiple(or more than)

#! Program to implement multiple inheritance using two base classes.

# class Father:
#     def height(self):
#         print('Height is 6.00 feet')
        
# class Mother:
#     def color(self):
#         print('Color is white')
        
# class Child(Father, Mother):
#     pass

# c = Child()

# print('Child\'s inherited qualities are: ')
# c.height()
# c.color()

#% Exercise

class A:
    def __init__(self):
        self.a = 'a'
        print(self.a)
        super().__init__()
        
class B:
    def __init__(self):
        self.b = 'b'
        print(self.b)
        super().__init__()
        
class C(A,B):
    def __init__(self):
        self.c = 'c'
        print(self.c)
        super().__init__()
        
## Access the super class instance vars from c

o = C()     ## Calls the constructor of C and 'c' is displayed. 
            ## Then super().__init__() will call constructor of left side class of (A,B) 
            ## which is  A is called and 'a' is displayed. But inside constructor of A,
            ## we again called its super class constructor super().__init__(). Since the
            ## object is the super class for A, an attempt to execute object class constructor
            ## will be done. But object does not have any constructor. So the search will
            ## continue to right hand side of the object class (A, B). this is class B. Hence
            ## B's constructor is executed and 'b' is displayed. After that the statement
            ## super().__init__() will attempt to execute constructor of B's super class.
            ## That is nothing but 'object class.'Since object class is already visited,
            ## the search stops here.As a result, the output will be 'c', 'a', 'b'.
            
            ## Searching in this manner for constructors or methods is called
            #% ''Method Resolution Order (MRO)''             
