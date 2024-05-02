from user import User
class Driver(User):
    def __init__(self, Name, Email, Address, Password,Vehicle_type,User_id) -> None:
        super().__init__(Name, Email, Address, Password, User_id)
        self.Vehicle_type = Vehicle_type
        self.Current_ride = None
        self.Wallet = 0
        self.Current_location = None

    def Display_profile(self):
        print(f"\nHere is the your name : {self.Name},email : {self.Email} and location : {self.Current_location}.Your current balance is : {self.Wallet} and vehicle type is : {self.Vehicle_type}.\n")

    def Load_cash(self,Amount):
        self.Wallet=Amount
        print(f"\nYou have successfully load {self.Wallet} taka in your wallet.\n")

    def Update_location(self,Current_location):
        self.Current_location=Current_location
        print(f"\nYou have successfully set your current location.Your current location is : {self.Current_location}\n")

    def Accept_ride(self,Ride):
        Ride.Set_driver(self)
        self.Current_ride = Ride
        print(f"\nSuccessfully accepted your ride request by {self.Name} and vehicle type is {self.Vehicle_type}.\n")

    def Reach_destination(self):
        if self.Current_ride!=None:
            self.Current_ride.End_ride()
            print(f"\nSuccessfully complete a ride from {self.Current_ride.Start_location} to {self.Current_ride.End_location}.\n")
            self.Current_ride = None
        else:
            print(f"\nThis driver can not drive any ride.Here is the rider name {self.Name}.Please attend a ride.\n")
