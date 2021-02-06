def rec(a,n):
    if n == 0:
        return 1
    return  a*rec( a,n-1 ) 
x = int(input())
y = int(input())
print( rec(x,y) )