# 4.Write a program to get the number of apples and price per apple. Display the total cost.
class app:
    def __init__(self,x):
        self.apple=int(input("enter the no.of apple"))
        self.price=int(input("enter the price per apple"))

    def cal(self):
        self.total=self.apple*self.price

    def display(self):
        print("Bill:",self.total)

obj1=app(10)
obj1.cal()
obj1.display()
