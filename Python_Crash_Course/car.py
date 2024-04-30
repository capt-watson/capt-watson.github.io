
class Car:
    """A simple attempt to represent a car."""
    def __init__(self,make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.upper()
    
    def fill_petrol_tank(self):
        pass
    
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
        
class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size = 40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
        
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.\n")
        
    def battery_upgrade(self):
        if self.battery_size != 65:
            self.battery_size = 65
        
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge.\n")  
        
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        
        """Initialize attributes of the parent class. Then initialize attrib specific to an electric car"""        
        super().__init__(make, model, year)
        self.battery = Battery()
                
    def fill_petrol_tank(self):
        print('This car does not have a petrol tank\n')
