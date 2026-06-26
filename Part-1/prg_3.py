# 3. write a program to get an amount from the user and add 18% Gst to it.Display the total amount including gst
class gst1:
    def __init__(self,x):
        self.amount=float(input("enter the amount:"))

    def cal(self):
        self.gst=self.amount*(18/100)
        self.total=self.amount+self.gst

    def display(self):
        print("Bill:",self.total)

obj1=gst1(10)
obj1.cal()
obj1.display()        
