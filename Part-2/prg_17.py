# 17. A cricket player enters runs scored. If runs < 50 display Average, 50–100 display Good, above 100 display Excellent.
class player:
    def __init__(self,x):
        self.runs=int(input("enter the runs scored:"))

    def calc(self):
        if self.runs<50:
            print("average")
        elif self.runs in range (50,101):
            print("good")
        else:
            print("excellent")

obj1=player(7)
obj1.calc()
