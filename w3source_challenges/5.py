sqAndM = input().split()
m =  int(sqAndM[1])
sq =  int(sqAndM[1])
yes = True
while sq > 0:
    if sq == 1:
        break
    if sq%m != 0:
        yes = False
        break
    sq /= m
print("Yes" if yes else "No")