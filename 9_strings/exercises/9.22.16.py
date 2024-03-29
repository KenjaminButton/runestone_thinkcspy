'''
Try the Peano-Gosper curve. Use 60 degrees.:

    FX
    X -> X+YF++YF-FX--FXFX-YF+
    Y -> -FX+YFYF++YF+FX--FX-Y

'''

import turtle

def createLSystem(numIters, axiom):
    startString = axiom
    endString = ""
    for i in range(numIters):
        endString = processString(startString)
        startString = endString

    return endString

def processString(oldStr):
    newstr = ""
    for ch in oldStr:
        newstr = newstr + applyRules(ch)

    return newstr

def applyRules(ch):
    newstr = ""
    if ch == 'X':
        newstr = 'X+YF++YF-FX--FXFX-YF+'   # Rule 1
    elif ch == 'Y':
        newstr = '-FX+YFYF++YF+FX--FX-Y'
    else:
        newstr = ch     # no rules apply so keep the character

    return newstr

def drawLsystem(aTurtle, instructions, angle, distance):
    for cmd in instructions:
        if cmd == 'F':
            aTurtle.forward(distance)
        elif cmd == 'B':
            aTurtle.backward(distance)
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)

def main():
    inst = createLSystem(5, "FX")   # create the string
    print(inst)
    t = turtle.Turtle()           # create the turtle
    wn = turtle.Screen()
    t.up()
    t.back(200)
    t.right(90)
    t.forward(100)
    t.left(90)
    t.down()
    t.speed(9)

    drawLsystem(t, inst, 60, 5)   # draw the picture
                                  # angle 90, segment length 5
    wn.exitonclick()

main()
