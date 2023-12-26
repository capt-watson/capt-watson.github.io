# class Computer:

#     def __init__(self,cpu,ram):
#         self.cpu = cpu
#         self.ram = ram        
        
        
#     def config(self):
#         print("Config is", self.cpu, self.ram)
        
# com1 = Computer("i5",16)
# com2 = Computer("Ryzen 3",8)

# com1.config()
# com2.config()

    # def __init__(self):
    #     self.name = "Shekhar"
    #     self.age = 64
        
    # def update(self):
    #     self.age = 62
        
#     def compare(self,other):
#         if self.age == other.age:
#             return True
#         else:
#             return False
        
# c1 = Computer()
# c2 = Computer()

# c1.age = 64

# c2.name = "Sushama"
# c2.age  = 59

# if c1.compare(c2):
#     print("They are of the same age")
# else:
#     print("They are of different age")
    
# c1.update()

# print(c2.name)

# import math

# # Define a class called Circle to represent a circle

# class Circle:
    
#     # initialize the circle object with a given radius
#     def __init__(self,radius):
#         self.radius = radius
        
# # Calculate and return the area of the circle using the formula: π * r^2
        
#     def calculate_area(self):
#         return math.pi*self.radius**2
    
# # Calculate and return the perimeter (circumference) of the circle using the formula: 2π * r

#     def calculate_perimeter(self):
#         return 2*math.pi*self.radius
    
#     # Prompt the user to input the radius of the circle and convert it to a floating-point number
    
# radius = float(input("input the Radius of the Circle:    "))
    
#     # Create a Circle object with the provided radius
    
# circle = Circle(radius)
    
#     # Calculate the area of the circle using the calculate_area method
    
# area = circle.calculate_area()
    
#     # Calculate the perimeter of the circle using the calculate_perimeter method
    
# perimeter = circle.calculate_perimeter()
    
#     # Display the calculated area and perimeter of the circle
    
# print("Area of Circle:", area)
    
# print("perimeter of the circle:", perimeter)




    
# # Import the date class from the datetime module to work with dates

# from datetime import date

# # Define a class called Person to represent a person with a name, country, and date of birth

# class Person:
    
#     # initialize the person object with a given name, country, and date of birth
    
#     def __init__(self, name, country, date_of_birth):
#         self.name = name
#         self.country = country
#         self.date_of_birth = date_of_birth
        
#     # Calculate the age of the person based on their date of birth
    
#     def calculate_age(self):
#         today = date.today()
#         age = today.year - self.date_of_birth.year
#         if today < date(today.year, self.date_of_birth.month, self.date_of_birth.day):
#             age -= 1
#         return age
    
# # Create three Person objects with different attributes

# person1 = Person("Shekhar","USA", date(1959, 6, 18))
# person2 = Person("Sushama","USA", date(1964, 7, 1))
# Person3 = Person("Ashish","Australia", date(1986, 4, 8))
# person4 = Person("Akash","Sweeden", date(1987, 8, 2))

# # Access and print the attributes and calculated age for each person

# print("Person1: ")
# print("Name: ", person1.name)
# print("Country: ", person1.country)
# print("Date Of Birth: ", person1.date_of_birth)
# print("Age: ", person1.calculate_age())

# print("Person2: ")
# print("Name: ", person2.name)
# print("Country: ", person2.country)
# print("Date Of Birth: ", person2.date_of_birth)
# print("Age: ", person2.calculate_age())

# print("Person3: ")
# print("Name: ", Person3.name)
# print("Country: ", Person3.country)
# print("Date Of Birth: ", Person3.date_of_birth)
# print("Age: ", Person3.calculate_age())

# print("Person4: ")
# print("Name: ", person4.name)
# print("Country: ", person4.country)
# print("Date of Birth: ", person4.date_of_birth)
# print("Age: ", person4.calculate_age())



# # Define a class called Calculator to perform basic arithmetic operations

# class Calculator:

# # Define a method for addition that takes two arguments and returns their sum
#     def add(self, x, y):
#         return x+y

# # Define a method for subtraction that takes two arguments and returns their difference
#     def subtract(self, x, y):
#         return x-y

# # Define a method for multiplication that takes two arguments and returns their product
#     def multiply(self, x, y):
#         return x*y

# # Define a method for division that takes two arguments and returns the result if denominator is not zero
#     def divide(self, x, y):
#         if y != 0:
#             return x/y
#         else:
#             return("can not divide by zero.")

# # Create an instance of the Calculator class
# calculator = Calculator()

# x = float(input("Enter the first number =  "))
# y = float(input("Enter the second number =  "))

# # Perform addition and print the result
# result = calculator.add(x, y)
# print("Sum = ", result)

# # Perform subtraction and print the result   
# result = calculator.subtract(x, y)
# print("Difference = ", result)

# # Perform multiplication and print the result
# result = calculator.multiply(x, y)
# print("Multiplication = ", result)

# # Perform division and print the result
# result = calculator.divide(x, y)
# print("division = ", result)      




# # Define a class called Node to represent a node in a binary search tree (BST)

# class Node:
    
#     # Initialize the Node object with a value, and set the left and right child pointers to None
    
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
        
#     # Define a custom __str__ method to convert the node's value to a string
    
#     def __str__(self):
#         return str(self.value)
    
# # Define a class called BinarySearchTree to represent a binary search tree
    
# class BinarySearchTree:
    
#     # Initialize the BST with an empty root node
#     def __init__(self):
#         self.root = None
        
#     # Insert a value into the BST
    
#     def insert(self, value):
        
#         # If the root is None, create a new node with the given value as the root
    
#         if self.root is None:
#             self.root = Node(value)
#         else:
#             self._insert_recursive(self.root, value)
        
#         # Helper method to recursively insert a value into the BST
        
#     def _insert_recursive(self, node, value):
#         if value < node.value:
#             if node.left is None:
#                 node.left = Node(value)
#             else:
#                 self._insert_recursive(node.left, value)
#         elif value > node.value:
#             if node.right is None:
#                 node.right = Node(value)
#             else:
#                 self._insert_recursive(node.right, value)
                
#     # Search for a value in the BST
    
#     def search(self, value):
#         return self._search_recursive(self.root, value)
    
#     # Helper method to recursively search for a value in the BST and return the node if found
    
#     def _search_recursive(self, node, value):
#         if node is None or node.value == value:
#             return node
#         elif value == node.value:
#             return node
#         elif value < node.value:
#             return self._search_recursive(node.left, value)
#         else:
#             return self._search_recursive(node.right, value)
        
#     # Create an instance of BinarySearchTree
    
# bst = BinarySearchTree()

# # Insert values into the BST

# bst.insert(5)
# bst.insert(3)
# bst.insert(7)
# bst.insert(2)
# bst.insert(4)
# bst.insert(6)
# bst.insert(8)
# bst.insert(11)
# bst.insert(15)
# bst.insert(19)
# bst.insert(20)


# x = int(input("Enter a number to search:  "))


# # Search for elements in the BST and print the results

# print("Searching For Elements:  ")
# print(bst.search(x))

# class student:
    
#     school = "Marwari Vidyalaya High School"
#     def __init__(self,m1, m2, m3):
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3

#     def avg(self):
#         return (self.m1 + self.m2 + self.m3) / 3

# # Accessor methods

#     def get_m1(self):
#         return self.m1

# # Mutator methods

#     def set_m1(self, value):
#         return self.m1 - value

# # Class methods
#     @classmethod
    
#     def get_school_name(cls):
#         return cls.school
    
# # Static methods

#     @staticmethod

#     def info():
#         print("This is class X B of the Marwari Vidyalay High School")



# s1 = student(55, 85, 70)
# s2 = student(98, 67, 88)

# print(s1.avg())
# print(s2.avg())

# print(student.get_school_name())
# student.info()


class Student:
    
    def __init__(self):
        self.name = "Ashish"
        self.subs = self.subjects()
        return
    def show(self):
        print("Name: ", self.name)
        self.subs.display()
        
    class subjects:
        def __init__(self):
            self.sub1 = "English"
            self.sub2 = "Maths"
            self.sub3 = "Science"
            return
        
        def display(self):
            print("Subjects: ", self.sub1, self.sub2, self.sub3)
            
S1 = Student()

S1.show()       

import pandas as pd

print(pd.__version__)
