# 13. Write a program to get any amount and calculate the 10% discount. Display the discounted price.
class price:
    def __init__(self,x):
        self.amount=float(input("enter the amount"))

    def calc(self):
        self.discount=self.amount*(10/100)
        print("Discounted price",self.discount)

obj1=price(10)
obj1.calc()
