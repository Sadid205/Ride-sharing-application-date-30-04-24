from ride import Ride
from vehicle import Vehicle
import random
class Ride_matching():
    def __init__(self,Available_drivers) -> None:
        self.Available_drivers = Available_drivers        
    def Find_driver(self,Ride_request,Vehicle_type):
        for _,driver in self.Available_drivers.items():
           if driver.Current_location!=None:
                if driver.Current_location.lower()==Ride_request.Rider.Current_location.lower():
                    if driver.Vehicle_type.lower()==Vehicle_type.lower():
                        if Vehicle_type.lower()=='car':
                            new_vehicle =  Vehicle('Car','ABC456',30)
                            new_ride_id = random.randint(10**3,10**4-1)
                            new_ride = Ride(Start_location=Ride_request.Rider.Current_location,End_location=Ride_request.End_location,Vehicle=new_vehicle,Ride_id=new_ride_id)
                            driver.Accept_ride(new_ride)
                            return new_ride
                        elif Vehicle_type.lower()=='bike':
                            new_vehicle = Vehicle('Bike','1234BH',50)
                            new_ride_id = random.randint(10**3,10**4-1)
                            new_ride = Ride(Start_location=Ride_request.Rider.Current_location,End_location=Ride_request.End_location,Vehicle=new_vehicle,Ride_id=new_ride_id)
                            driver.Accept_ride(new_ride)
                            return new_ride
                        else:
                            print(f"\nThis {Vehicle_type} is not available in this company.\n")
        print("\nIn your current location,We can not found any driver for ride.Please try later.\n")
        return None


           

        