import random
#import colorgram
from turtle import Turtle, Screen

# colors = colorgram.extract('image.jpg', 10)
# all_colors = []
#
# for color in colors:
#     color = list(color.rgb)
#     color = tuple(color)
#     all_colors.append(color)

colors = [(246, 240, 244), (235, 241, 246), (1, 13, 31), (52, 25, 17), (219, 127, 106), (9, 105, 160),
          (242, 214, 69), (150, 84, 39)]


timmy = Turtle()
timmy.shape("turtle")
screen = Screen()
screen.colormode(255)

timmy.penup()
timmy.back(200)
timmy.setheading(270)
timmy.forward(200)
timmy.setheading(0)


y = -200
x = -200

for _ in range(10):
    for _ in range(10):
        timmy.dot(20, random.choice(colors))
        timmy.penup()
        timmy.forward(50)
    y += 50
    timmy.setx(x)
    timmy.sety(y)





screen.exitonclick()






