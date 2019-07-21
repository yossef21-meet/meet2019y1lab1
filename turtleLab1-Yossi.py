import turtle 

# Everything that comes after the # is a 
# comment.
# It is a note to the person reading the code.
# The computer ignores it.
# Write your code below here...
turtle.penup() #Pick up the pen so it doesn’t 
               #draw
turtle.goto(-200,-100) #Move the turtle to the 
 #position (-200, -100) 
 #on the screen
turtle.pendown() #Put the pen down to start
                 #drawing
#Draw the M:
turtle.goto(-200,-100+200) 
turtle.goto(-200+50,-100) 
turtle.goto(-200+100,-100+200)
turtle.goto(-200+100,-100)

#E
turtle.penup()
turtle.forward(50)
turtle.pendown()
turtle.forward(100)
turtle.backward(100)
turtle.left(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.backward(100)
turtle.left(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)

#Second E
turtle.penup()
turtle.right(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(50)
turtle.pendown()
turtle.forward(100)
turtle.backward(100)
turtle.left(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.backward(100)
turtle.left(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)

#T
turtle.penup()
turtle.forward(50)
turtle.pendown()
turtle.forward(150)
turtle.backward(75)
turtle.right(90)
turtle.forward(200)

# ...and end it before the next line.
turtle.mainloop() 
# turtle.mainloop() tells the turtle to do all
# the turtle commands above it and paint it on the screen.
# It always has to be the last line of code!
