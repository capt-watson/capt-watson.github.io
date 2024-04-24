

# from restaurant import Restaurant, IceCreamStand
# from user import Admin
# from car import Car, ElectricCar
# from random import randint, choices

# class Restaurant:
#     def __init__(self, name, type):
#         self.name = name
#         self.type = type
#         self.current_number = 0
        
#     def describe_restaurant(self):
#         print(f'{self.name.title()} is a {self.type.title()} restaurant.')
        
#     def open_restaurant(self):
#         print(f"{self.name.title()} is now open")
        
#     def number_served(self, numbers):
#         self.current_number += numbers
#         print(f"Total customer served {self.current_number}")    
        
#     def make_pizza(self, toppings):
#         self.toppings = toppings
#         print('Making pizza with the following toppings:')            
#         for topping in self.toppings:
#             print(f"  - {topping.title()}")   
        
# class IceCreamStand(Restaurant):
#     def __init__(self, name, type):
#         super().__init__(name, type)
        
        
#     def get_flavors(self, flavors):
#         self.flavors = flavors
#         print("The flavors of the ice cream stand are:")
#         for flavor in self.flavors:
#             print(f" - {flavor.title()}")

# toppings = ['Extra Cheese', 'black olives', 'parsley']
        
# rc = Restaurant("Dominos","Pizzeria")

# rc.number_served(10)
# rc.number_served(5)
# rc.number_served(9)
# rc.number_served(7)

# rc.describe_restaurant()

# rc.make_pizza(toppings)

flavors = ['vanilla', 'chocolate', 'strawberry']

# iStand = IceCreamStand('amul ice cream', 'ice cream parlour')

# iStand.get_flavors(flavors)

# iStand.number_served(10)
# iStand.number_served(4)
# iStand.number_served(7)
# iStand.number_served(5)
# iStand.number_served(12)

# iStand.describe_restaurant()

# iStand.open_restaurant()

# global privileges

# privileges = ["can add post", "can delete post", "can ban user"]

# priv = Admin("veronica", "smith", 26, 'American')

# priv.greet_user()

# priv.describe_user()

# priv.privileges.show_privileges()

# my_new_car = Car('mercedes-amg','eqs-53', 2023)

# print(my_new_car.get_descriptive_name())

# # my_new_car.update_odometer(18)

# # print(my_new_car.odometer_reading)

# my_Ec = ElectricCar('bmw', 'i4', 2024)

# print(my_Ec.get_descriptive_name())

# # my_i4.battery.describe_battery()

# # my_i4.battery.get_range()

# randint(1,6)

players = ['charles', 'martina', 'michael', 'florence', 'betty']

first_up = choices(players)  #! This function takes in a list or tuple and returns a randomly chosen element:

first_up

# class Die:
#     def __init__(self, sides):
#         self.sides = sides
        
#     def roll_die(self):
#         return randint(1, self.sides)

# die_6 = Die(6)

# die_10 = Die(10)

# die_20 = Die(20)


# for i in range(1, 11):
#     print(die_6.roll_die(), end='  ')
#     print(die_10.roll_die(), end='  ')
#     print(die_20.roll_die())



#~ 3  2  1
#~ 1  2  10
#~ 6  8  19
#~ 1  7  14
#~ 6  1  7
#~ 6  1  4
#~ 1  4  6
#~ 5  6  15
#~ 6  1  19
#~ 1  4  16

lottery = ('s', 9, 4, 'g', 5, 'y', 8, 18, 'u', 'r', 7, 6, 59, 'q', 'e')

num = choices(lottery, k=4)

# print("Today's winning number is:", num )

# for i in num:
#     print(i, end = ' ')

wt = ['r', 'g', 'q', 9]

count = 0

flag = True

while flag:
    num = choices(lottery, k=4)
    count += 1
    if wt == num:
        print(f"Winning number found in {count} attempts.")
        flag = False

#~ Winning number found in 37024 attempts.

