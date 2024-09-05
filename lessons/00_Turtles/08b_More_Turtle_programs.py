"""

Copy the code from the previous lesson, 08a_More_Turtle_programs.ipynb, 
from the section "Change the Turtle Image"


Then change the code so that the turtle has a different image ( look in the 'images'
directory ) and moves to the corners of the screen in a square pattern. 
"""

import turtle


def set_turtle_image(turtle, image_name):
    """Set the turtle's shape to a custom image."""

    from pathlib import Path
    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / image_name)

    screen = turtle.getscreen()
    screen.addshape(image_path)
    turtle.shape(image_path)

# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=600)

# Create a turtle and set its shape to the custom GIF
t = turtle.Turtle()

set_turtle_image(t, "girl_red.gif")

t.penup()
t.speed(1)

for i in range(10):
    t.goto(0, 0)
    t.forward(100)
    t.forward(-100)
    t.goto(0,100)
    t.goto(0,0)
    t.forward(-100)
    t.forward(100)
    t.goto(0,-100)
    t.goto(0,0)



turtle.exitonclick()     