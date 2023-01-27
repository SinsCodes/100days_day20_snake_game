from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self,position):
        seg_1 = Turtle()
        seg_1.shape("square")
        seg_1.color("white")
        seg_1.penup()
        seg_1.goto(position)
        self.segments.append(seg_1)

    def extend(self):
        self.add_segment(self.segments[-1].position())


    def move(self):

        for seg in range(len(self.segments) - 1, 0, -1):
            x=self.segments[seg - 1].xcor()
            y=self.segments[seg - 1].ycor()
            self.segments[seg].goto(x, y)
        self.head.forward(MOVE_DISTANCE)

        # self.head[0].left(90)

    def up(self):
        if self.head.heading()!= DOWN:
            self.head.setheading(UP)


    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)


    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)


    def right(self):
        if self.head.heading()!= LEFT:
            self.head.setheading(RIGHT)








