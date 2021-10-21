import turtle

def fractal_2(l,n):
    if n <= 0:
        turtle.forward(l)
    else :
        fractal_2(l/2,n-1)
        turtle.right(45)
        fractal_2(l/2,n-1)
        