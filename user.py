from abc import ABC,abstractmethod
class User(ABC):
    def __init__(self,Name,Email,Address,Password,User_id) -> None:
        self.Name = Name 
        self.Email = Email
        self.Address = Address
        self.Password = Password
        self.User_id = User_id
    
    @abstractmethod
    def Display_profile(self):
        raise NotImplementedError
 