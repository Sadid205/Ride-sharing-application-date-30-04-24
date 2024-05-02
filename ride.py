from datetime import datetime
class Ride():
    def __init__(self,Start_location,End_location,Vehicle,Ride_id) -> None:
        self.Ride_id = Ride_id
        self.Start_location = Start_location
        self.End_location = End_location
        self.Driver = None
        self.Rider = None
        self.Start_time = None
        self.End_time = None
        self.Ride_Vehicle = Vehicle
        self.Estimated_fare = self.Calculate_fare(self.Ride_Vehicle.Vehicle_type)
    
    def Set_driver(self,my_Driver):
        self.Driver = my_Driver
        print(f"\nThis {my_Driver.Name} is successfully added for ride\n")
    
    def Start_ride(self):
        self.Start_time = datetime.now()
        print(f"\nSuccessfully start a ride.Here is the driver name:{self.Driver.Name} and rider name is : {self.Rider.Name}.\n")
    
    def End_ride(self):
        self.End_time = datetime.now()
        if self.Rider.Wallet<self.Estimated_fare:
            print(f"\nPlease add more {self.Estimated_fare-self.Rider.Wallet} taka in your wallet.\n")
        else:
            self.Driver.Wallet+=self.Estimated_fare
            self.Rider.Wallet-=self.Estimated_fare
            print(f"\nSuccessfully completed a ride.Here is the cost of ride : {self.Estimated_fare}.The rest of your money is : {self.Rider.Wallet} taka.\n")

    def Calculate_fare(self,Vehicle_type):
        distance = 10
        fare_per_km = {
            'car':30,
            'bike':20,
            'cng':25
        }
        return distance*fare_per_km.get(Vehicle_type.lower())
    
    def __repr__(self) -> str:
        return f"\nRide is started.Start location for this ride is : {self.Start_location} and end location is : {self.End_location}.\n"