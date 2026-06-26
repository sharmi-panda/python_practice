# 2. A shopkeeper offers a discount: if a customer’s bill is above ₹500 display 10% discount applied, otherwise No discount.
class offer:
    def __init__(self,x):
        self.amount=float(input("enter the amount:"))

    def calc(self):
        if self.amount>500:
            self.discount=self.amount*(10/100)
            print("10% discount applied:",self.discount)
        else:
            print("No discount")

obj1=offer(9)
obj1.calc()    
