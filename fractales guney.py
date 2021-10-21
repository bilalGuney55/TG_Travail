import turtle

## exercice 0

##for i in range(1):
##    turtle.forward(50)
##    turtle.right(90)
##    turtle.forward(200)
##    turtle.right(90)
##    turtle.forward(50)
##    turtle.right(90)
##    turtle.forward(200)
##    turtle.right(90)
##    turtle.penup()
##    turtle.forward(50)
##    turtle.left(90)
##    turtle.forward(50)
##    turtle.pendown()
##    turtle.circle(30)
    
    


##exercice 1
    


##def dessine(n):
##    if n > 0:
##        turtle.forward(n)
##        turtle.right(90)
##        import turtle
##
##def dessine(n):
##    if n > 0:
##        turtle.forward(n)
##        turtle.right(90)        
##        dessine(n-2)
##    else:
##        dessine()
##
##print(dessine(200))


## exercice 2


def koch(n,l):
   if n<=0:
        turtle.forward(l)
        
   else:
        koch(l/3,n-1)
        turtle.left(60)
        koch(l/3,n-1)
        turtle.right(120)
        koch(l/3,n-1)
        turtle.left(60)
        koch(l/3,n-1)

def flocon(l,n):
    koch(l,n)
    turtle.right(120)
    koch(l,n)
    turtle.right(120)
    koch(l,n)

    
print(koch(0,100))
print(flocon(100,0))
