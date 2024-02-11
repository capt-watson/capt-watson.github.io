
from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self, reg_no):
        self.reg_no = reg_no
        
    def openTank(self):         ## This is a concrete method
        print('Fill up the Fuel into the tank')
        print('For the car with reg. no: ', self.reg_no)
        
    @abstractmethod
    def steering(self):
        pass
    
    @abstractmethod
    def breaking(self):
        pass
