from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        with open("text_file.txt", mode="r") as f:
            self.hi_score = int(f.read())
            self.score = 0
            self.penup()
            self.hideturtle()
            self.color("White")
            self.goto(0, 260)
            self.update()

    def update(self):
        self.write(f"Score: {self.score} Highest Score: {self.hi_score}", align="center", font=("Arial", 24, "normal"))

    def highest_score(self):
        if self.score > self.hi_score:
            with open("text_file.txt", mode="w") as file:
                file.write(str(self.score))

    def recall(self):
        self.score += 1
        self.clear()
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 24, "normal") )
