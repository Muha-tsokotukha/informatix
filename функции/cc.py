def isPointInSquare(x, y):
    return (1 >= x**2) and (1 >= y**2) 
 
x = float(input())
y = float(input())
if isPointInSquare(x,y):
    print("YES")
else: print("NO")
