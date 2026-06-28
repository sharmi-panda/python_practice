# 7. Write a program to get the total seconds from the user and convert them into hours, minutes,and seconds.
class time:
    def __init__(self,x):
        self.sec=float(input("enter the seconds:"))

    def calc(self):
        self.hour=self.sec//3600
        self.remaining_sec=self.sec%3600
        self.min=self.remaining_sec//60
        self.secs=self.remaining_sec%60

    def display(self):
        print("hour:",self.hour)
        print("minutes:",self.min)
        print("secs:",self.secs)

obj1=time(30)
obj1.calc()
obj1.display()
