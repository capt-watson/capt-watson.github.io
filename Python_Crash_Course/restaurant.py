
class Restaurant:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.current_number = 0
        

    def describe_restaurant(self):
        print(f'{self.name.title()} is a {self.type.title()} restaurant.')
        
    def open_restaurant(self):
        print(f"{self.name.title()} is now open")
        
    def number_served(self,numbers):
        self.current_number += numbers
        print(f"Total customer served {self.current_number}")
        
    def make_pizza(self, toppings):
        self.toppings = toppings
        print('Making pizza with the following toppings:')            
        for topping in self.toppings:
            print(f"  - {topping.title()}")      

        
class IceCreamStand(Restaurant):
    def __init__(self, name, type):
        super().__init__(name, type)
        
        
    def get_flavors(self, flavors):
        self.flavors = flavors
        print("The flavors of the ice cream stand are:")
        for flavor in self.flavors:
            print(f" - {flavor.title()}")

