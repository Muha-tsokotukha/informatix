def mindiv(a):
    n = 2
    mn = 1e9
    while n <= (a**0.5 )+1:
        if a%n == 0 and mn > n:
            return n
        else : n +=1
    return a
x = int(input())
print(mindiv(x))