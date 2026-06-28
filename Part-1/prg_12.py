# 12. Write a program to convert kilometers per hour (km/h) into meters per second (m/s).
class distance:
    def __init__(self,x):
        self.kilo=float(input("enter the kilometers per hour:"))

    def calc(self):
        self.meter=self.kilo/3.6
        print("Meter per second:",round(self.meter,2))

obj1=distance(60)
obj1.calc()
