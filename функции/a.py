def dist( x1,y1,x2,y2 ):
    return( ( ((x2-x1)**2) + ((y2-y1)**2) )**(0.5)  ) 

a = float(input())
b = float(input())
c = float(input())
d = float(input())
print(dist(a,b,c,d))