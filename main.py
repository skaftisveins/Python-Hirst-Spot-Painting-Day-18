import turtle as turtle_module
import random

turtle_module.colormode(255)

screen = turtle_module.Screen()
screen.bgcolor('SteelBlue')

raphael = turtle_module.Turtle()
raphael.hideturtle()
raphael.penup()
raphael.setheading(225)
raphael.forward(300)
raphael.setheading(0)
num_of_dots = 100
# raphael.goto(-300, -300)

raphael.color('white')
raphael.shape('turtle')
raphael.speed('fastest')

color_list = [(25, 108, 164), (194, 38, 81), (238, 161, 49), (234, 215, 85), (226, 237, 228), (223, 137, 176), (144, 108, 56), (102, 197, 219), (206, 166, 29), (20, 57, 132), (214, 73, 90), (239, 89, 50), (141, 208, 227), (118, 192, 140),
              (3, 186, 176), (106, 107, 199), (138, 29, 73), (4, 161, 86), (98, 51, 36), (22, 156, 210), (232, 165, 184), (175, 185, 221), (29, 90, 95), (233, 172, 161), (152, 213, 190), (242, 205, 8), (89, 48, 31), (39, 46, 81), (26, 97, 94)]

randomized_color = random.choice((color_list))

def draw_hirst_painting(size_of_dot):
    """Paint a painting with 10 x 10 rows of dots. Each dot is around 20 in size and spaced appart by around 50 paces"""
    for dot_count in range(1, num_of_dots+1):
        
        # 1a. Draw dots 10 each row
        raphael.dot(size_of_dot, random.choice(color_list))
        raphael.forward(50)
        
        # 2. Draw dots 10 x 10
        if dot_count % 10 == 0:
            raphael.setheading(90)
            raphael.forward(50)
            raphael.setheading(180)
            raphael.forward(500)
            raphael.setheading(0)


draw_hirst_painting(30)

screen.exitonclick()
