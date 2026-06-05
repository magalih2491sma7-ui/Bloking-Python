import turtle
def tangentCircles (ttl):
    """ Print 10 tangent circles . """
    r = 10 
    n = 10
    for i in range (1 , n + 1, 1) :
        ttl.circle (r * i)
def concentricCircles (ttl):
    """ Print 10 concentric circles . """
    r = 10
    for i in range (10) :
        ttl.circle ( r * i)
        ttl.up()
        ttl.sety (( r * i) * ( -1) )
        ttl.down()

ben = turtle . Turtle ()
ben.up() ; ben.goto(0 , 150)
ben.down() ; ben.pencolor("blue")
tangentCircles(ben)
ben.up() ; ben.goto(0 , -150)
ben.down() ; ben.pencolor("red")
concentricCircles(ben)