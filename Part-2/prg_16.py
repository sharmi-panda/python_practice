# 16. A shopkeeper enters quantity of milk purchased. If quantity is greater than 5 liters, give Free coupon, else display Thank you for purchase.
class shop:
    def __init__(self,x):
        self.milk=int(input("quantity of milk purchased:"))

    def calc(self):
        if self.milk>5:
            print("free coupon")
        else:
            print("Thank you for purchase")

obj1=shop(19)
obj1.calc()
