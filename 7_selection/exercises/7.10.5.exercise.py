'''
In the turtle bar chart program, what do you expect to happen
if one or more of the data values in the list is negative?
Go back and try it out. Change the program so that when it
prints the text value for the negative bars, it puts the
text above the base of the bar (on the 0 axis).
'''

'''
Modify the turtle bar chart program from the previous chapter
so that the bar for any value of 200 or more is filled with
red, values between [100 and 200) are filled yellow, and bars
representing values less than 100 are filled green.
'''

import turtle

def drawBar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill() # start filling this shape
    if height < 0:
        t.write(str(height))
    t.left(90)
    t.forward(height)
    if height >= 0:
        t.write(str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill() # stop filling this shape



xs = [48, -50, 200, 240, 160, 260, 220] # here is the data
maxheight = max(xs)
minheight = min(xs)
numbars = len(xs)
border = 10

tess = turtle.Turtle() # create tess and set some attributes
tess.color("blue")
tess.fillcolor("red")
tess.pensize(3)

wn = turtle.Screen() # Set up the window and its attributes
wn.bgcolor("lightgreen")
if minheight > 0:
    lly = 0
else:
    lly = minheight - border

wn.setworldcoordinates(0-border, lly, 40*numbars+border, maxheight+border)


for a in xs:
    drawBar(tess, a)

wn.exitonclick()


