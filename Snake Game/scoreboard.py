from turtle import Turtle



class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("White")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score:{self.score} HighScore: {self.high_score}", align="center", font=("Arial", 24, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode ="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    #def gameover(self):
        #self.goto(0, 0)
        #self.write("GAME OVER", align="center", font=("Arial", 24, "normal"))

    def score_count(self):
        self.score +=1
        self.update_score()
