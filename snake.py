from turtle import Turtle

position =[(0, -23), (0, -46), (0, -69)]


class Snake:
    def __init__(self):
        self.box_list = []
        self.create_snake()

    def create_snake(self):
        for n in position:
            self.add_segment(n)

    def add_segment(self, pos):
        new_box = Turtle(shape="square")
        new_box.penup()
        new_box.color("white")
        new_box.goto(pos)
        self.box_list.append(new_box)

    def extend(self):
        self.add_segment(self.box_list[-1].position())

    def move(self):
        for n in range(len(self.box_list) - 1, 0, -1):
            x = self.box_list[n - 1].xcor()
            y = self.box_list[n - 1].ycor()
            self.box_list[n].goto(x, y)
        self.box_list[0].forward(20)

    def up(self):
        if self.box_list[0].heading() != 270:
            self.box_list[0].setheading(90)

    def down(self):
        if self.box_list[0].heading() != 90:
            self.box_list[0].setheading(270)

    def right(self):
        if self.box_list[0].heading() != 180:
            self.box_list[0].setheading(0)

    def left(self):
        if self.box_list[0].heading() != 0:
            self.box_list[0].setheading(180)