# implement a basic notification system
# 1. I want an interface / abstract class of Notification
# abstract method -> send(self, message)

# 2. two concrete implementation of this class

# EmailNotification class
# SMSNotification class

# 3. then use them here

from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass
    
class EmailNotification(Notification):
    def __init__(self, email):
        self.email = email
            
    def send(self, message):
        print(f"Sending EMAIL {self.email}: {message}")
    
class SMSNotification(Notification):
    def __init__(self, number):
        self.number = number
        
    def send(self, message):
        print(f"Sending SMS {self.number}: {message}")

def send_notification(notification, message):
    notification.send(message)
    
email_notification = EmailNotification("test@test.com")
sms_notification = SMSNotification("34345454")

send_notification(email_notification, "you have a new email")
send_notification(sms_notification, "you have a new message")