def isPointInSquare(x, y):
    return  (abs(x) <= 0.5 and abs(y) <= 0.5 )or ( x**2 == 1 and y**2 == 0 ) or (y**2 == 1 and x**2 == 0)
a = float(input())
b = float(input())
if isPointInSquare(a,b):
    print("YES")
else: print("NO")