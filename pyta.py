from turtle import *
speed(500)
angle = 30
color('#3f1905')
def arbre(n,longueur):
    if n==0:
        color('green')
        forward(longueur) 
        backward(longueur) 
        color('#3f1905')
    else:
        width(n)
        forward(longueur/3) 
        left(angle) 
        arbre(n-1,longueur*2/3)
        right(2*angle) 
        arbre(n-1,longueur*2/3)
        left(angle) 
        backward(longueur/3) 
hideturtle() 
up() 
right(90)  
forward(300) 
left(180) 
down() 
arbre(11,700) 
showturtle() 
mainloop()


