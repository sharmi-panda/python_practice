# 7. A user enters temperature in Celsius. If temperature is below 20, display Cold, if between 20–30 display Warm, else display Hot.
class temp:
    def __init__(self,x):
        self.celsius=float(input("enter the celsius:"))

    def calc(self):
        if self.celsius<20:
            print("cold")
        elif self.celsius in range (20,31):
            print("warm")
        else:
            print("hot")

obj1=temp(20)
obj1.calc() 
