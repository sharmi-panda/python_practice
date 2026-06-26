# 1. A student enters their exam score. If the score is 35 or above, display Pass, otherwise Fail.
class student:
    def __init__(self,x):
        self.mark=float(input("enter the mark:"))

    def calc(self):
        if self.mark>=35:
            print("pass")
        else:
            print("fail")
obj1=student(10)
obj1.calc()
