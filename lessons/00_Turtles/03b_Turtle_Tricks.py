"""
For this program, you will tell Tina the Turtle to draw 
a pentagon.

You should look at the previous program, 02_Meet_TIna.py
to see how to use the turtle commands.


"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window
tina = turtle.Turtle()                  # Create a turtle named tina

# Use tina.forward() and tina.left() to draw a pentagon
# Make each side of the pentagon a different color with 
# tina.pencolor()


tina.forward(100)
tina.left(72)
tina.forward(100)
tina.left(72)
tina.forward(100)
tina.left(72)
tina.forward(100)
tina.left(72)
tina.forward(100)
tina.left(72)

turtle.exitonclick()                    # Close the window when we click on it
