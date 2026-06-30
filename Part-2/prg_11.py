# 11. A bakery worker enters production quantity. If more than 100 items are baked, display Good production, else display Low production.
class bakery:
    def __init__(self,x):
        self.worker=int(input("enter the production quantity:"))

    def calc(self):
        if self.worker>100:
            print("good production")
        else:
            print("low production")

obj1=bakery(10)
obj1.calc()
