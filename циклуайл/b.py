n = int(input())
x = 2
while x<= n:
    t = True
    if n%x == 0:
        i = 2
        while i <= x**0.5:
            if x%i == 0:
                t = False
                break
            i+=1
        if t == True:
            print(x)
            exit()
    x += 1
