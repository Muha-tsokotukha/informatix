x = int(input())
y = int(input())
k = 1
while 1:
    if x >= y:
        print(k)
        exit()
    x += x*0.1
    k+=1