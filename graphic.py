import turtle # graphic libraray for drawing a shape and create graphic
import colorsys # use for color

t = turtle.Turtle() # create t object that used for color manipultion
s = turtle.Screen().bgcolor('black') # create screen object set it backgraound color black
t.speed(0) # set the drawing speed max
n = 100 # define n variable of 100
h = 0 # define h variable of 0
for i in range(360): # create loop for 360 cicular iterate
    c = colorsys.hsv_to_rgb(h,1,0.8) # convert the hue value h to rgb color using HSV and stored into c
    h+= 1/n # increament the hue value in next iterator and create a smooth color change
    t.color(c) # set the turtle color computed RGB color
    t.left(1) # rotate the turtle 1 degree left
    t.fd(1) # move the turtle forwad by 1 unit
    for j in range(2): # iterate twice
        t.left(1) # rotate the turtle 1 degree to the left
        t.circle(100) # draw a circle with a radious of 100 units