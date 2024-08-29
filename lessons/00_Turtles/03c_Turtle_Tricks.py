"""
For this program, you will tell Tina the Turtle to draw 
multiple shapes.

Draw two circles, filled with different colors, 
and in different places on the screen. 

You should look at the previous program, 02_Meet_TIna.py
to see how to use the turtle commands.

"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window
tina = turtle.Turtle()                  # Create a turtle named tina

# Use tina.circle() to draw a circle, and tina.goto() to move tina to a new location
# Use tina.begin_fill(), tina.end_fill(), and tina.fillcolor() to fill in the shapes

tina.color('light blue')
tina.begin_fill()
tina.circle(50, steps=50)
tina.end_fill()

tina.penup()
tina.forward(-200)

tina.color('light green')
tina.begin_fill()
tina.circle(50, steps=50)
tina.end_fill()

tina.penup()
tina.goto(-100,150)

tina.color('light pink')
tina.begin_fill()
tina.circle(50, steps=50)
tina.end_fill()
tina.hideturtle()
turtle.exitonclick()                    # Close the window when we click on it
