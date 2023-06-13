import colorgram
from turtle import Turtle, Screen
from random import choice


def extract_colors(img):
    """Returns a list of rgb tuples for the 25 most used colors in an image"""
    color_list = []
    colors_used = colorgram.extract(img, 25)
    for i in range(len(colors_used)):
        rgb = colors_used[i].rgb
        r = rgb.r
        b = rgb.b
        g = rgb.g
        color_list.append((r, g, b))
    return color_list


screen = Screen()
screen.colormode(255)

tim = Turtle()
tim.up()
tim.speed("fastest")
tim.goto(-450, -450)
tim.hideturtle()

colors = extract_colors("hirst_painting.jpg")
colors.pop(0)
colors.pop(0)

y = -450
for row in range(10):
    for dot in range(10):
        tim.dot(25, choice(colors))
        tim.forward(100)
    tim.setpos(-450, (y+(100*(row + 1))))


screen.exitonclick()