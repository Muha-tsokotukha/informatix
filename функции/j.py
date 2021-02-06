def isprime(x):
    if x == 2:
        return True
    n = 2
    while n <= x**0.5+1:
        if x % n == 0:
            return False
        n +=1
    return True
a = int(input())

print("YES" if isprime(a) else "NO" )