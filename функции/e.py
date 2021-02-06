def isincircle( x,y,x1,y1,r ):
    return (x-x1)**2 + (y-y1)**2 <= r**2

a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
if isincircle(a,b,c,d,e):
    print("YES")
else : print("NO")