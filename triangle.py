##ex 4

##from math import sqrt
##
##class Point:
##    
##    def __init__(self,x,y):
##        self.x = x
##        self.y = y
##        
##    
##    def __repr__(x,y):
##        return "(" + str(x) + "," + str(y) + " )"
    

## ex 5
    

class Fraction:
    
    def __init__(self,num,denom):
        self.num = num
        self.denom = denom
        
    def __repr__(self):
        if self.denom != 1:
            return str(self.num) + "/" + str(self.denom)
        else:
            return str(self.num)
        
    def __eq__(self,frac2):
        return self.num/self.denom == frac2.num / frac2.denom
    
    
    def __lt__(self,frac2):
        return self.num/self.denom < frac2.num / frac2.denom
    
    
    def __mul__(self,frac2):
        return Fraction(self.num*frac2.num,self.denom*frac2.denom)
    
    def __add__(self,frac2):
        return
    
    
    def 
    
    
    
def pgcd(a,b):
    if b == 0:
        return a
    else:
         return pgcd(b,b%a)

        
