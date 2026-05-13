# 1. Create an abstract class:
# Vehicle
# abstract method: move()

# Create subclasses:
# Car
# Bicycle

# Each must implement move() differently.
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def mov(self):
        pass
    
class Car(Vehicle):
    def __init__(self, name, speed):
        self.name = name
        self.speed= speed
        
    def mov(self):
        return self.speed * 2
        
class Bike(Vehicle):
    def __init__(self, type, speed):
        self.type = type
        self.speed = speed
        
    def mov(self):
        return self.speed + 2
    
car1 = Car("Huyndai", 5)
bike1 = Bike("Road bike", 5)

def display_speed(vehicle):
    print(vehicle.mov())

print(car1.mov())
print(bike1.mov())

display_speed(car1)
display_speed(bike1)

# 2. Create an abstract class:
# FileHandler
# abstract methods: 
# read()
# write()

# Create subclasses:
# TextFileHandler
# JsonFileHandler

# They can just print messages instead of reading real files.
class FileHandler(ABC):
    @abstractmethod
    def read(self, name, path):
        pass
    def write(self, name, path):
        pass
        
class TextFileHandler(FileHandler):
        
    def read(self,name, path):
        print(f"reading text file: {name} at {path}")
        
    def write(self,name, path):
        print(f"writing text file: {name} at {path}")
        
class JsonFileHandler(FileHandler):
    
    def read(self,name, path):
        print(f"reading JSON file {name} at {path}")
        
    def write(self,name, path):
        print(f"write JSON file {name} at {path}")

handlerJson = JsonFileHandler()
handlerText = TextFileHandler()

handlerJson.read("JSON", "source/adv")

def display_content(file_handler, name, path):
    handlerText.read(name, path)
    
display_content(TextFileHandler, "notes.txt", "/doc")
    
# 3. Create an abstract class:
# Account
# abstract method: calculate_fee()

# Create subclasses:
# SavingsAccount
# PremiumAccount

# Each returns a different fee.

class Account(ABC):
    @abstractmethod
    def calculate_fee(self):
        pass
    
class SavingAccount(Account):
    miniumBalance = 150
    
    def __init__(self, accountBalance):
        self.accountBalance = accountBalance
        
    def calculate_fee(self):
        if (self.accountBalance < SavingAccount.miniumBalance):
            fees = 12
        else: fees = 0
        return fees
    
class CheckingAccount(Account):
    def calculate_fee(self):
        fees = 25
        return fees

def display_fee(account):
    print(account.calculate_fee())
      
tam_savingaccount = SavingAccount(160)
tam_checkingaccount = CheckingAccount()


display_fee(tam_savingaccount)
display_fee(tam_checkingaccount)

print("===============")

# 4. abstract Employee
# Create:
# abstract class Employee
# abstract method calculate_salary()

# Subclasses:
# FullTimeEmployee
# PartTimeEmployee

# Each should calculate salary differently.

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
    
class FullTimeEmployee(ABC):
    hourly_rate = 30
    def calculate_salary(self, working_hours):
        salary = working_hours * self.hourly_rate
        return salary
    
class PartTimeEmploye(ABC):
    hourly_rate = 18
    def calculate_salary(self, working_hours):
        salary = working_hours * self.hourly_rate
        return salary
    
def print_salary(employee, working_hours):
    print (employee.calculate_salary(working_hours))

tam = FullTimeEmployee() 
john = PartTimeEmploye()
print(tam.calculate_salary(23))
print("=======================")
print_salary(tam, 23)
print_salary(john, 23)

# 5. abstract Media
# Create:
# abstract class Media
# abstract method play()

# Subclasses:
# Song
# Video

# Each implements play() differently.

class Media(ABC):
    def play(self):
        pass
    
class Song(Media):
    def __init__(self, songName):
        self.songName = songName
        
    def play(self):
        print(f"Playing {self.songName} ")
        
class Video(Media):
    def __init__(self, videoName):
        self.videoName = videoName
        
    def play(self, videoName):
        print(f"Playback {videoName}")

def play(media):
    print(media.play())

song1 = Song("Enemy")
song1.play()

play(song1)