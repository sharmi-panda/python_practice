# 14. A driver enters vehicle speed. If speed < 40, display Too slow, if 40–80 display Normal driving, else display Overspeeding.
class vehicle:
    def __init__(self,x):
        self.speed=int(input("enter the vehicle speed"))

    def calc(self):
        if self.speed<40:
            print("too slow")
        elif self.speed in range (40,81):
            print("normal driving")
        else:
            print("overspeeding")

obj1=vehicle(23)
obj1.calc()
