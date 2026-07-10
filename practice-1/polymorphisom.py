class EmailNotification:
    def send(self):
        print(f"Send email notification!")
        
class SmsNotification:
    def send(self):
        print(f"Send sms notification!")

class PushNotification:
    def send(self):
        print(f"Send push notification!")
        

class Notify:
    def execute(self, notification):
        notification.send()
    
    
email = EmailNotification()
sms = SmsNotification()
push = PushNotification()


notify = Notify()
notify.execute(email)
notify.execute(sms)