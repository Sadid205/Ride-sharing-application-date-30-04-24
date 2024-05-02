from abc import ABC
class Vehicle(ABC):
    # speed = {'Car':30,
    #          'Bike': 40,
    #          'CNG':20
    #          }
    def __init__(self,Vehicle_type,License_plate,rate) -> None:
        self.Vehicle_type = Vehicle_type
        self.License_plate = License_plate
        self.rate = rate


class Car(Vehicle):
   def __init__(self, Vehicle_type, License_plate, rate) -> None:
       super().__init__(Vehicle_type, License_plate, rate)

class Bike(Vehicle):
    def __init__(self, Vehicle_type, License_plate, rate) -> None:
        super().__init__(Vehicle_type, License_plate, rate)