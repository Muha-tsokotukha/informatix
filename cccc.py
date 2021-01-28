import math
a = int(input())
b = int(input())
i = 1
for i in range(1,b+1):
    if i*i>=a and i*i<=b:
        print(i*i, end=" ")