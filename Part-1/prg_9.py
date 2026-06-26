# 9. Write a program to get the marks of 3 subjects and find the percentage. Display the percentage.
class marks:
    def __init__(self,x):
        self.m1=int(input("enter the 1st sub marks:"))
        self.m2=int(input("enter the 2nd sub marks:"))
        self.m3=int(input("enter the 3rd sub marks:"))

    def calc(self):
        self.total=(self.m1+self.m2+self.m3)/300
        self.perc=self.total*100

    def display(self):
        print("Percentage:",self.perc)

obj1=marks(34)
obj1.calc()
obj1.display()
