# 6. Write a program to get the total days from the user and convert them into years, weeks, and days.
class world:
    def __init__(self,x):
        self.days=int(input("enter the days"))

    def calc(self):
        self.year=self.days//365
        self.remain_year=self.days%365
        self.week=self.remain_year//7
        self.day=self.remain_year%7
        print("year:",self.year)
        print("weeks:",self.week)
        print("days:",self.day)

obj1=world(49)
obj1.calc()
