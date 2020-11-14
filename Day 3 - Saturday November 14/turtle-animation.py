import turtle
turtle.speed(0) # draw really fast
turtle.tracer(0, 0) # tells Python not to draw until turtle.update()

# <-- this is a comment. Python will ignore everything after one

'''
Three quotation marks is a block comment.
Python will ignore anything written between two sets of three quotation marks.
Some of the code below is commented out.
You can add or remove comments to run different parts of the code.
'''

# square
'''
turtle.goto(0,0)
turtle.goto(100,0)
turtle.goto(100,100)
turtle.goto(0,100)
turtle.goto(0,0)
turtle.update()
'''

# filled square - remember that "color" is spelled the American way
'''
turtle.pencolor('blue') # pencolor() changes the outline colour
turtle.fillcolor('red') # fillcolor() changes the interior colour
# use begin_fill() and end_fill() to tell Python when you are begining and ending the shape
turtle.begin_fill()
turtle.goto(0,0)
turtle.goto(100,0)
turtle.goto(100,100)
turtle.goto(0,100)
turtle.goto(0,0)
turtle.end_fill()
turtle.update()
'''


# Animation - drawing, erasing, and redrawing an image

def draw_square(x, y):
    turtle.pencolor('blue')
    turtle.fillcolor('red')
    turtle.begin_fill()
    # update all coordinates with x,y (ie, add x to x-coords, add y to y-coords)
    turtle.goto(x,y)
    turtle.goto(x+100,y)
    turtle.goto(x+100,y+100)
    turtle.goto(x,y+100)
    turtle.goto(x,y)
    turtle.end_fill()

def erase_square(x, y):
    turtle.pencolor('white')
    turtle.fillcolor('white')
    turtle.begin_fill()
    turtle.goto(x,y)
    turtle.goto(x+100,y)
    turtle.goto(x+100,y+100)
    turtle.goto(x,y+100)
    turtle.goto(x,y)
    turtle.end_fill()

for i in range(100):
    draw_square(i,0)
    turtle.update()
    erase_square(i,0)
