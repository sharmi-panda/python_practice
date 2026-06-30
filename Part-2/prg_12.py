# 12. A game player enters score. If score ≥ 100, display Level Up, else display Keep playing.
class player:
    def __init__(self,x):
        self.score=int(input("enter the player score:"))

    def calc(self):
        if self.score>=100:
            print("level up")
        else:
            print("keep playing")

obj1=player(19)
obj1.calc()
