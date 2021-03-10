n = int(input())
x = 1
while x < n:
    if x*x == n:
        print(x)
        exit()
    if x*x > n:
        print(x-1)
        exit()
    else : x += 1
