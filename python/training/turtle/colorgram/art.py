import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [
    (224, 154, 102),
    (152, 76, 53),
    (60, 33, 28),
    (36, 24, 29),
    (236, 210, 166),
    (235, 195, 134),
    (108, 44, 34),
    (195, 103, 72),
    (20, 18, 26),
    (107, 74, 80),
    (91, 48, 52),
    (238, 176, 150),
    (80, 77, 97),
    (202, 119, 48),
    (189, 136, 146),
    (178, 99, 109),
    (232, 202, 209),
    (62, 59, 77),
    (227, 171, 181),
    (143, 137, 157),
    (127, 118, 145),
    (23, 26, 24),
    (218, 214, 228),
    (100, 58, 23),
]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()
