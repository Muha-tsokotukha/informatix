def ReduceFrac(a,b):
    x = 2
    while x <= a and x <= b:
        if a%x == 0 and b%x == 0:
            a /= x 
            b /= x
            continue
        else: x +=1
    x = str(a)
    y = str(b)
    t = x + " " + y
    return t

q = int(input()) 
p = int(input())
print(ReduceFrac(q,p))