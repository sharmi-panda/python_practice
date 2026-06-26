# 5. A company offers bonus: If an employee worked more than 5 years, display bonus 5000, otherwise bonus 2000.
class company:
    def __init__(self,x):
        self.year=int(input("enter the no.of years worked:"))

    def calc(self):
        if self.year>5:
            print("5000 bonus")
        else:
            print("2000 bonus")

obj1=company(5)
obj1.calc()
