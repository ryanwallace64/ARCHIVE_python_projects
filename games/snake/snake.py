from turtle import Turtle
STARTING_LOCATIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 12
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_segment(self, location):
        """Add a segment at input location"""
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(location)
        self.segments.append(new_segment)

    def create_snake(self):
        """Create a new 3-segment snake in the center of screen"""
        for location in STARTING_LOCATIONS:
            self.create_segment(location)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def move(self):
        """Move snake forward by MOVE_DISTANCE"""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def extend(self):
        """Add 1 segment to the snake body"""
        self.create_segment(self.segments[-1].pos())
        self.create_segment(self.segments[-1].pos())

    def up(self):
        """Turn North"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Turn South"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Turn West"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Turn East"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
