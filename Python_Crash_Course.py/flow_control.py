
# import math
# import sys
# from car import ElectricCar




# print(
#     datetime.now()
#     .strftime('%d %b %Y, %I:%M:%S %p'))


# def circle_area(radius):
#     area = math.pi * radius**2
#     return area

# circle_area(1.1)
 
# print(sys.version)

# first =input('Enter your First name: ')

# second = input('Enter your Second name: ')

# print(second, first)


# num = input('Enter your numbers separated by commas:' )

# num = num.split(',')

# a = list(num)

# b = tuple(num)

# print(a)

# print(b)

# d = {
# 'aeinstein': {
# 'first': 'albert',
# 'last': 'einstein',
# 'location': 'princeton',
# },
# 'mcurie': {
# 'first': 'marie',
# 'last': 'curie',
# 'location': 'paris',
# },
# }

# for k, y in d.items():
#     print(f'\nUser Name : {k}')
    
#     fn = f'{y['first']} {y['last']}'
#     ln = f'{y['location']}'
   
#     print(f'\t Full_name : {fn.title()}')
#     print(f'\t Location: {ln.title()}')


# d = {
#     'dogs': {
#         'name': 'huckleberry',
#         'age': 2,
#         'pedigree': 'husky',
#     },
#     'cats': {
#         'name':'pussy',
#         'age': 1,
#         'pedigree': 'persian',
#     },
#     'birds': {
#         'name':'griswald',
#         'age' : 1,
#         'pedigree': 'peruvian',
#     },
# }

# for k, v in d.items():
#     print(f'\nAnimal name: {k}')
    
#     nm = f'{v['name']}'
#     ag = f'{v['age']}'
#     pd = f'{v['pedigree']}'
    
#     print(f'\tName: {nm.title()}')
#     print(f'\tAge: {ag.title()}')
#     print(f'\tPedigree: {pd.title()}')

# car = input('Which type of car you wish to purchase? ')

# print('Let me see if we have',car,'in stock')

# prompt = "\n Please tell me something and I'll repeat after you."
# prompt += "\n Enter 'quit' to end the program. "

# name = prompt
# while name != 'quit':
#     name = input(prompt)
#     print(name)


# prompt = "\n Please tell me something and I'll repeat after you."
# prompt += "\n Enter 'quit' to end the program. "


# Flag = True

# while Flag:
#     name = input(prompt)
#     if name == 'quit':
#         Flag = False
#     else:
#         print(name)


# flag = True

# while flag:
#     topping = input('Enter required toppings for your pizza or quit to exit: ')
#     if topping == 'quit':
#         flag = False
#     else:
#         print('Topping of',topping,' is being added to your Pizza')


# flag = True

# while flag:
#     age = input("Please enter your age or 'quit' to Quit: ")
#     if age == 'quit':
#         flag = False
#     elif age.isnumeric():
#         age = int(age)
#         if age < 3:
#             print("This child gets Free ticket")
#         elif age >= 3 and age < 12:
#             print('Your Ticket price US$ 10 per ticket')
#         else:
#             print('You ticket price is US$ 15 per ticket')


# uc_users = ['alice', 'brian', 'candace']

# c_users = []

# while uc_users:
#     current_user = uc_users.pop() ## last element from the list removed. Loop stops once list is empty
#     print(f"Verifying Users: {current_user.title()}")   ## Will print removed user's name
#     c_users.append(current_user)        ## removed user's name will be appended to c_users []

# print("\nThe following users have been confirmed")

# for c_user in c_users:      ## Will loop through the c_users list and print their names
#     print(c_user.title())


#^ Removing All Instances of Specific Values from a List

# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']

# print(pets)

# while 'cat' in pets:   ## must use while loop as we are deleting elements from the list while loop is in progress
#     pets.remove('cat') ## The while loop stops as soon as all the 'cats' from the list are removed.
    
# print(pets)


#^ Filling a Dictionary with User Input

# responses = {}

# ## set a flag to indicate that the polling is active

# polling_active = True

# while polling_active:
#     ## Prompt the person's name and response
#     name = input("\nWhat is your name? ")
#     response = input("Which mountain would you like to climb someday? ")
    
#     ## store the responses in a dictionary
    
#     responses[name] = response
    
#     ## Find out if anyone else is going to take the poll
    
#     repeat = input("Would you like to let another person respond? (yes/no)")
#     if repeat == 'no':
#         polling_active = False
    
#     ## Polling is complete. Show the results

# print("\n--- Poll Results ---")
# for name, response in responses.items():
#     print(f"{name} would like to climb {response}")


# sandwich_orders = ['grilled sandwich','pastrami', 'chicken sandwich', 'french sandwich','pastrami','club sandwich', 'burger sandwich','pastrami']

# finished_sandwiches = []

# print('\nSorry, The Deli has run out of pastrami.\n'.title())

# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')

# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()
#     print(f"\nI made your {current_sandwich.title()} sandwich.")
#     finished_sandwiches.append(current_sandwich)

# print("\n\n\n---- Finished Sandwiches ----")
# for sandwich in finished_sandwiches:
#     print('\n',sandwich.title())


# responses = {}

# polling_active = True

# while polling_active:
#     name = input('\nWhat is your name?')
#     response = input('If you could visit one place in the world, where would you go? ')
    
#     responses[name] = response
    
#     repeat = input('Would you like to let another person respond? (yes/no)')
#     if repeat == 'no':
#         polling_active = False
        
# print('\n--- Poll Results ---')

# for name, response in responses.items():
#     print(f'{name.title()} would like to go to {response.title()}.')


# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()

# ## When you call a function that returns a value, you need to provide a variable that the return value can be assigned to. In this case, the returned value is assigned to the variable musician

# musician = get_formatted_name('michael', 'jackson')
# print(musician)

# def build_person(first_name, last_name, age=None):
#     person = {'first': first_name, 'last': last_name}
#     if age:
#         person['age'] = age     ## Will assign age value to the person key = age
#     return person

# musician = build_person('jimi', 'hendrix', age=27)
# print(musician)

# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# while unprinted_designs:
#     currently_printing = unprinted_designs.pop()
#     print(f"printing Model: {currently_printing.title()}")
#     completed_models.append(currently_printing)
    
# print("\n\nThe following models have been printed:\n")
# for completed_model in completed_models:
#     print(completed_model.title())


# def make_pizza(*toppings):
#     """Print a list of toppings that have been requested"""
    
# ## '*' in def parameter tells Python to make a tuple called 'toppings', containing all the values this function receives.



# # make_pizza('extra cheese', 'black olives')

# #^ Mixing Positional a'nd Arbitrary Arguments

# def make_pizza(size, *toppings):
    
#     ## If you want a function to accept several different kinds of arguments, the parameter that accepts an arbitrary number of arguments must be placed last in the function definition.
    
#     """summary of the pizzas we are making"""
    
#     print(f'\nMaking {size} inch pizza with the following toppings:')
    
#     for topping in toppings:
#         print(f" - {topping.title()}")
    
# # make_pizza(16, 'pepperoni')
# make_pizza(12, 'extra cheese', 'black olives')


#^ Using Arbitrary Keyword Arguments

# def build_profile(first, last, **user_info):
#     """Build a dictionary containing everything we know about a user."""
    
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info

# user_profile = build_profile('veronica', 'smith', location='mississippi', field='data science')

# for key, value in user_profile.items():
#     print(f"{key.title()} = {value.title()}")

# # print(user_profile)

#^ __init__() Method

#! A function that’s part of a class is called a method.

#% The __init__() method 2 is a special method that Python runs automatically whenever we create a new instance based on the Dog class. Every method call associated with an instance automatically passes self, which is a reference to the instance itself; it gives the individual instance access to the attributes and methods in the class.

#* When we make an instance of Dog, Python will call the __init__() method from the Dog class.

#% When we make an instance of Dog, Python will call the __init__() method from the Dog class. We’ll pass Dog() a name and an age as arguments; self is passed automatically, so we don’t need to pass it.

#& The two variables defined in the body of the __init__() method each have the prefix self. Any variable prefixed with self is available to every method in the class, and we’ll also be able to access these variables through any instance created from the class.

#% The line self.name = name takes the value associated with the parameter name and assigns it to the variable name, which is then attached to the instance being created. Variables that are accessible through instances like this are called attributes.

#$ The Dog class has two other methods defined: sit() and roll_over() 4. Because these methods don’t need additional information to run, we just define them to have one parameter, self.

#* The Dog class has two other methods defined: sit() and roll_over() 4. Because these methods don’t need additional information to run, we just define them to have one parameter, self. The instances we create later will have access to these methods. In other words, they’ll be able to sit and roll over.

#^ Making an Instance from a Class


# class Dog:
#     """A simple attempt to model a dog."""
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def sit(self):
#         print(f"{self.name.title()} is now sitting")
#     def roll_over(self):
#         print(f"{self.name.title()} rolled over!")

# my_dog = Dog('officer griswald', 6)
# your_dog = Dog('Lucy', 3)           #! Here, my_dog is an instance (object) created by the Dog class

# print(f"my dog's name is {my_dog.name.title()} and he is {my_dog.age} years old.")

#% Here, we tell Python to create a dog whose name is 'Willie' and whose age is 6. 

#! When Python reads this line, it calls the __init__() method in Dog with the arguments 'Willie' and 6. The __init__() method creates an instance representing this particular dog and sets the name and age attributes using the values we provided. Python then returns an instance representing this dog. We assign that instance to the variable my_dog.

#& A capitalized name like Dog refers to a class, and a lowercase name like my_dog refers to a single instance created from a class.

#^ Accessing Attributes

#$ We access the value of my_dog’s attribute name 2 by writing:

# print(f"my dog's name is {my_dog.name.title()} and he is {my_dog.age} years old.")


#^ Calling Methods

# my_dog.sit()

# my_dog.roll_over()

#% To call a method, give the name of the instance (in this case, my_dog) and the method you want to call, separated by a dot. When Python reads my_dog.sit(), it looks for the method sit() in the class Dog and runs that code.


#^ Creating Multiple Instances

# my_dog.sit()
# your_dog.sit()

# my_dog.roll_over()
# your_dog.roll_over()

    
# restaurant_1 = Restaurant('Grand Marriott','vegetarian')

# restaurant_2 = Restaurant('Hotel Taj', 'Continental')

# restaurant_3 = Restaurant('white Regency', 'Mexican')


# restaurant_1.describe_restaurant()

# restaurant_1.open_restaurant()

# restaurant_2.describe_restaurant()

# restaurant_2.open_restaurant()

# restaurant_3.describe_restaurant()

# restaurant_3.open_restaurant()


# class User:
#     def __init__(self, name, last, age, nationality):
#         self.name = name
#         self.last = last
#         self.age = age
#         self.nationality = nationality
        
#     def describe_user(self):
#         print(f"\nGuest name is {self.name.title()}, last name is {self.last.title()}, age is {self.age} and is of {self.nationality.title()} nationality")
        
#     def greet_user(self):
#         print(f"\nHello! {self.name.title()}, welcome to the hotel Singapore Plaza\n")
        
# user_1 = User('veronica', 'smith', 16, 'American')
# user_2 = User('betty', 'douglas', 17, 'American')
# user_3 = User('andrew', 'washington', 18, 'American')

# user_1.describe_user()
# user_1.greet_user()

# user_2.describe_user()
# user_2.greet_user()

# user_3.describe_user()
# user_3.greet_user()

class Car:
    def __init__(self,make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}\n"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has covered {self.odometer_reading} kilometers till now\n")
        
    def update_odometer(self, mileage):
        """Set the odometer reading to the given value. Reject the change if it attempts to roll the odometer back.."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You cannot rollback the odometer reading\n')
            
    def increment_odometer(self, miles):
        self.odometer_reading += miles
        
#     #! This method takes in a mileage value and assigns it to self.odometer_reading.
    
    
# my_new_car = Car('audi', 'a4', 2024)

# my_used_car = Car('maruti', '800DLX', 1987 )

# print(my_new_car.get_descriptive_name())

# # my_new_car.read_odometer()

# #^ Modifying Attribute Values

# #& Modifying an Attribute’s Value Directly

# my_new_car.odometer_reading = 101

# #! This line tells Python to take the instance my_new_car, find the attribute odometer_reading associated with it, and set the value of that attribute to 23:

# # my_new_car.update_odometer(99)

# my_used_car.update_odometer(150_000)
# my_used_car.read_odometer()

# #& Incrementing an Attribute’s Value Through a Method

# my_used_car.increment_odometer(111)
# my_used_car.read_odometer()

# # my_new_car.read_odometer()

   
# restaurant = Restaurant('kfc', 'fast_food')

# restaurant.number_served(15)

# restaurant.number_served(100)


# class Office:
#     def __init__(self, name):
#         self.name = name
#         self.attempt = 0
        
#     def increment_login_attempts(self, attempt):
#         self.attempt += attempt
#         print(f"Total login attempts so far {self.attempt}\n")
        
#     def reset_login_attempts(self):
#         self.attempt = 0
#         print(f"Attempt Counter has been reset to {self.attempt} \n")
    
# user = Office('Google')

# user.increment_login_attempts(1)

# user.increment_login_attempts(1)
# user.increment_login_attempts(1)
# user.increment_login_attempts(1)
# user.increment_login_attempts(1)

# user.reset_login_attempts()


        
# my_EC = ElectricCar('tesla','Model S', 2012)

# print(my_EC.get_descriptive_name())

# my_EC.battery.describe_battery()

# my_EC.battery.get_range()

# my_EC.fill_petrol_tank()
    
# restaurant = Restaurant('kfc', 'fast_food')

# # restaurant.number_served(15)

# # restaurant.number_served(100)
       
#     ## In the above example, child class inherits name, type parameters from its parent class and hence no need to assign them to self variables.
#     ## But if we want to add more parameters to the child class, then we need to assign new parameters to self variables.
    
#     ## Inherited super class 'super().__init__()' method does not require 'self' as parameter in parenthesis but must have other parameters mentioned in the parent class.)
        
        
# flavors = ['vanilla', 'chocolate', 'strawberry']
        
# iStand = IceCreamStand('amul ice cream', 'ice cream',flavors)

# iStand.get_flavors()

# iStand.describe_restaurant()

# iStand.open_restaurant()

        
# my_EC = ElectricCar('tesla','Model S', 2012)

# my_EC.battery.battery_upgrade()

# my_EC.battery.get_range()

