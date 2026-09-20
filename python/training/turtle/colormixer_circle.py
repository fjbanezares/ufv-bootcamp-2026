import turtle
import colorsys


def draw_one_color_circle(x, y, radius, color):
    turtle.up()
    turtle.goto(x, y - radius)
    turtle.down()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()


turtle.speed(0)
turtle.hideturtle()
turtle.bgcolor("light gray")
turtle.title("49-Color Color Wheel")
turtle.setup(700, 700)
turtle.tracer(0)
turtle.delay(0)

num_colors = 490
radius = 200
penwidth = 20 * 7 / num_colors
hue = 0

# Move turtle to starting position
turtle.up()
turtle.goto(0, -100)
turtle.down()

for i in range(num_colors):
    (r, g, b) = colorsys.hsv_to_rgb(hue, 1, 1)
    draw_one_color_circle(0, -100, radius, (r, g, b))
    turtle.up()
    turtle.forward(2 * radius)
    turtle.down()
    hue += 0.9 / num_colors
    turtle.update()

turtle.mainloop()
