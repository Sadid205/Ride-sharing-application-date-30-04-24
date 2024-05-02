from user import User
from ride_request import Ride_request
from ride_matching import Ride_matching
import random
class Rider(User):
    def __init__(self, Name, Email, Address, Password,User_id) -> None:
        super().__init__(Name, Email, Address, Password,User_id)
        self.Current_ride = None
        self.Wallet = 0
        self.Current_location = None
    def Display_profile(self):
        print(f"\nHere is the your name : {self.Name},email : {self.Email} and location : {self.Current_location}.Your current balance is : {self.Wallet}.\n")

    def Load_cash(self,Amount):
        self.Wallet=Amount
        print(f"\nYou have successfully load {self.Wallet} taka in your wallet.\n")

    def Update_location(self,Current_location):
        self.Current_location=Current_location
        print(f"\nYou have successfully set your current location.Your current location is : {self.Current_location}\n")

    def Request_ride(self,Ride_sharing,Destination,Vehicle_type):
        new_ride_request = Ride_request(self,End_location=Destination)
        new_ride_matching = Ride_matching(Available_drivers=Ride_sharing.Drivers)
        new_ride = new_ride_matching.Find_driver(Ride_request=new_ride_request,Vehicle_type=Vehicle_type)
        if new_ride!=None:
            new_ride.Ride_id = random.randint(10**3,10**4-1)
            Ride_sharing.Rides[new_ride.Ride_id] = new_ride
            self.Current_ride = new_ride
            self.Current_ride.Rider = self
            print(f"\nSuccessfully accepted your ride request.Here is the rider name : {self.Current_ride.Rider.Name} and the driver name is : {self.Current_ride.Driver.Name}.\n")
        else:
            print("\nThis time ride is not available.Please try later.\n")