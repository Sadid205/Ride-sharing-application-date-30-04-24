from rider import Rider
from ride import Ride
from ride_sharing import Ride_sharing
from driver import Driver
import random
Jete_cai = Ride_sharing("Jete Cai")


while True:
    print("Press 1 for sign up")
    print("Press 2 for login")
    print("Press 3 exit")
    press = int(input("Please press any number from 1 to 3 : "))
    if press==1:
        while True:
            print("Press 1 for sign up as a rider")
            print("Press 2 for sign up as a driver")
            print("Press 3 for exit")
            press = int(input("Please press any number form 1 to 3 : "))
            if press==1:
                Name = input("Please enter your name : ")
                Email = input("Please enter your email : ")
                Address = input("Please enter your address : ")
                Password = input("Please enter your password : ")
                User_id = random.randint(10**3,10**4-1)
                new_rider = Rider(Name=Name,Email=Email,Address=Address,Password=Password,User_id=User_id)
                Jete_cai.Sign_Up(Driver_or_Rider=new_rider)
            elif press==2:
                Name = input("Please enter your name : ")
                Email = input("Please enter your email : ")
                Address = input("Please enter your address : ")
                Password = input("Please enter your password : ")
                Vehicle_type = input("Please enter your vehicle type :")
                User_id = random.randint(10**3,10**4-1)
                if Vehicle_type.lower()=="car":
                    new_driver = Driver(Name=Name,Email=Email,Address=Address,Password=Password,Vehicle_type=Vehicle_type,User_id=User_id)
                    Jete_cai.Sign_Up(Driver_or_Rider=new_driver)
                elif Vehicle_type.lower()=="bike":
                    new_driver = Driver(Name=Name,Email=Email,Address=Address,Password=Password,Vehicle_type=Vehicle_type,User_id=User_id)
                    Jete_cai.Sign_Up(Driver_or_Rider=new_driver)
                else:
                    print(f"\nThis {Jete_cai.Company_name} company does not allow {Vehicle_type} vehicle for sharing your ride.Please use 'bike' or 'car'.\n")
            elif press==3:
                break
            else:
                print("\nPlease enter a valid input from 1 to 3\n")
    elif press==2:
        while True:
            print("Press 1 for login as a rider")
            print("Press 2 for login as a driver")
            print("Press 3 for exit")
            press = int(input("Please press any number from 1 to 3 : "))
            if press==1:
                Email = input("Please enter your email : ")
                Password = input("Please enter your password : ")
                new_rider = Jete_cai.Login(Email=Email,Password=Password)
                if new_rider!=None:
                    while True:
                        print("Press 1 for display profile")
                        print("Press 2 for load cash in your wallet")
                        print("Press 3 for update your location")
                        print("Press 4 for request a ride")
                        print("Press 5 for exit")
                        press = int(input("Please enter any number from 1 to 5 : "))
                        if press==1:
                            new_rider.Display_profile()
                        elif press==2:
                            cash = int(input("Please enter your amount : "))
                            new_rider.Load_cash(Amount=cash)
                        elif press==3:
                            location=input("Please enter your current location : ")
                            new_rider.Update_location(Current_location=location)
                        elif press==4:
                            if new_rider.Current_location==None:
                                print("\nPlease add your current location to find a driver.\n")
                            else:
                                destination = input("Please enter your destination : ")
                                vehicle = input("Please enter which vehicle would you like to ride : ")
                                new_rider.Request_ride(Ride_sharing=Jete_cai,Destination=destination,Vehicle_type=vehicle)
                        elif press==5:
                            break
                        else:
                            print("\nPlease inter a valid input from 1 to 5\n")
            elif press==2:
                Email = input("Please enter your email : ")
                Password = input("Please enter your password : ")
                new_driver = Jete_cai.Login(Email=Email,Password=Password)
                if new_driver!=None:
                    while True:
                        print("Press 1 for display profile")
                        print("Press 2 for load cash in your wallet")
                        print("Press 3 for update your location")
                        print("Press 4 reach destination")
                        print("Press 5 for exit")
                        press = int(input("Please enter any number from 1 to 5 : "))
                        if press==1:
                            new_driver.Display_profile()
                        elif press==2:
                            cash = int(input("Please enter your amount : "))
                            new_driver.Load_cash(Amount=cash)
                        elif press==3:
                            location=input("Please enter your current location : ")
                            new_driver.Update_location(Current_location=location)
                        elif press==4:
                           new_driver.Reach_destination()
                        elif press==5:
                            break
                        else:
                            print("\nPlease inter a valid input from 1 to 5\n")
            elif press==3:
                break
            else:
                print("\nPlease inter a valid input from 1 to 3\n")
    elif press==3:
        break
    else:
       print("\nPlease inter a valid input from 1 to 3\n") 
    