# Class 1 -- Playlist Class:
# Attributes:
# name
# song_count
# Methods:
# add_song()
# remove_song()
# show_info()

class Playlist:
    def __init__(self, name, song_count = 0):
        self.name = name
        self.song_count = song_count
        self.song_list = []
        
    def add_song(self,song_name):
        if song_name in self.song_list:
            print(f"the song '{song_name}' already added")
        else:
            self.song_count = self.song_count + 1
            self.song_list.append(song_name)
            print(f"the song named '{song_name}' has been add to {self.name} playlist. Total songs in the playlist: {self.song_count}")      
        return self.song_count
    
    def remove_song(self, song_name):
        if song_name in self.song_list:
            self.song_list.remove(song_name)
            self.song_count = self.song_count -1
            print(f"the song named '{song_name}' has been removed from {self.name} playlist. Total songs in the playlist: {self.song_count}")
        else:
            print(f"not found '{song_name}' in the playlist '{self.name}'")
        return self.song_count
    
    def show_info(self):
        print(f"Total songs in the playlist '{self.name}': {self.song_count}. Song list: {self.song_list}")

# testing       
# playlist1 = Playlist("today")
# playlist1.show_info()
# playlist1.add_song("you are my sunshine")
# playlist1.add_song("heavy")
# playlist1.add_song("we are the world")
# playlist1.remove_song("you are my sunshine")
# print(playlist1.song_list)
# playlist1.show_info()

# Class 2 -- ShoppingCart Class
# Attrbutes:
# owner
# item_count
# Methods:
# add_item(quantity)
# remove_item(quantity)
# show_cart()

class ShoppingCart:
    def __init__(self, ownername, item_count = 0):
        self.owner = ownername
        self.item_count = item_count
        self.items = []
        
    def add_item(self, quantity, item_name):
        if quantity > 0:
            self.item_count = self.item_count + quantity
            self.items.append(item_name)
        else:
            print(f"Please add quantity")
        return self.item_count
    
    def remove_item(self, quantity,item_name):
        if item_name in self.items:
            self.item_count = self.item_count - quantity
            self.items.remove(item_name)
        else:
            print(f"item {item_name} not found")
        return self.item_count
    
    def show_cart(self):
        print(f"{self.owner} cart has {self.items}, total of {self.item_count} items")
        


# tamCart = ShoppingCart("TamCart")
# print(tamCart.owner)
# tamCart.add_item(2, "water bottle")
# tamCart.show_cart()
# tamCart.remove_item(1, "water bottle")
# tamCart.show_cart()

# Class 3 -- UserAccount
# Attributes:
# username
# active (state)
# login_count (how many times have they logged in)
# methods:
# activate()
# deactivate()
# login()
# show_status()

class UserAccount:
    def __init__(self, username, state = False, login_count = 0):
        self.username = username
        self.state = state
        self.login_count = login_count
    
    def activate(self):
        if self.state == True:
            print(f"{self.username} already actived")
        else:
            self.state = True
            print(f"{self.username} has been activated")
            
    def deactivate(self):
        if self.state == True:
            self.state = False
            print(f"{self.username} is deactivated")
        else:
            print(f"{self.username} already deactivated")
    
    def login(self):
        if self.state == True:
            self.login_count += 1
            print(f"{self.username} logged in sucessfully")
        else:
            print(f"{self.username} could not login")
    
    def show_status(self):
        print(f"{self.username} is {self.state}. Number of logins: {self.login_count}")
        

tam = UserAccount("Tam")
tam.activate()
tam.activate()
tam.login()
tam.show_status()
tam.deactivate()
tam.login()