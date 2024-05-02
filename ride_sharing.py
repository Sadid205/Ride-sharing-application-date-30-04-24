from rider import Rider
from driver import Driver
class Ride_sharing():
    def __init__(self,Company_name) -> None:
        self.Company_name = Company_name
        self.Riders = {}
        self.Drivers = {}
        self.Rides = {}
   
    def Sign_Up(self,Driver_or_Rider):
        if isinstance(Driver_or_Rider,Rider)==True:
            for _,value in self.Riders.items():
             if value.Email==Driver_or_Rider.Email:
                print(f"\nYou have already an account for this {Driver_or_Rider.Email} email.Please login.\n")
                return
            self.Riders[Driver_or_Rider.User_id] = Driver_or_Rider
            print(f"\nSuccessfully sign up for rider.Here is the rider name : {Driver_or_Rider.Name} and Email : {Driver_or_Rider.Email}.\n")
        elif isinstance(Driver_or_Rider,Driver)==True:
            for _,value in self.Drivers.items():
             if value.Email==Driver_or_Rider.Email:
                print(f"\nYou have already an account for this {Driver_or_Rider.Email} email.Please login.\n")
                return
            self.Drivers[Driver_or_Rider.User_id] = Driver_or_Rider
            print(f"\nSuccessfully sign up for rider.Here is the rider name : {Driver_or_Rider.Name} and Email : {Driver_or_Rider.Email}.\n")
        else:
            print("\nSign up failed!.Please provide a driver or rider instance for sign up.\n")

    def Login(self,Email,Password):
            for _,myRider in self.Riders.items():
                if myRider.Email==Email:
                    if myRider.Password==Password:
                        print(f"\nWelcome {myRider.Name} .You have successfully logged in your account.Now you are ready for ride.\n")
                        return myRider
            for _,myDriver in self.Drivers.items():
                if myDriver.Email==Email:
                    if myDriver.Password==Password:
                        print(f"\nWelcome {myDriver.Name} .You have successfully logged in your account.Now you are ready for drive.\n")
                        return myDriver
            print(f"\nMaybe this {Email} account does not exist in {self.Company_name} application database or you have given wrong email or password.Please create an account.\n")
            return None

    def __str__(self) -> str:
        return f"\nThis {self.Company_name} company has {len(self.Drivers.keys())} drivers and {len(self.Riders.keys())} riders.\n"