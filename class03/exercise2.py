# create a class User
# give 2 attributes (username, password)
# both in password setter and init
# if password is less than 4 character long, return an error

class User:
    def __init__(self, username, password):
        #Option A
        if(len(password)<4):
            print("password is too short")
        else:
            self.username = username
            self.password = password
            
        #Option B:
        # self.username = username
        # self.password = self.set_password(password)
            
    def set_password(self, password):
        if(len(password)<4):
            print("invalid password, it must contain at least 4 character")
        else:
            self.password = password


    
user1 = User("tam","1234")
user1.set_password("12")
