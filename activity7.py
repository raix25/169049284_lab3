# Import Turtle graphics library
import turtle
num= int(input("Enter the number of heart you want to see:"))
colors = ['pink', 'red', 'white'] #different colors for alteration

# Set up the Turtle screen and turtle
screen = turtle.Screen()
pattern_turtle = turtle.Turtle()
pattern_turtle.speed(10)

# Loop to draw the pattern
for i in range(num):
    pattern_turtle.penup()
    pattern_turtle.goto(0,0) #to keep heart at the center 
    pattern_turtle.pendown()
    pattern_turtle.begin_fill()
    pattern_turtle.color(colors[i % len(colors)]) #to alternate the color

    pattern_turtle.left(140)
    size = 180 - (i*20) #to make smaller heart after each loop
    pattern_turtle.forward(size) #for the first line of heart
    pattern_turtle.circle(-size/2,200) #reducing size of arc of the heart 
    pattern_turtle.setheading(60)
    pattern_turtle.circle(-size/2,200) 
    pattern_turtle.forward(size)
    pattern_turtle.end_fill()

    pattern_turtle.setheading(0)

turtle.exitonclick()