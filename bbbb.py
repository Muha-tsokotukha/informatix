a = int(input())
b = int(input())
c = int(input())
d = int(input())
i = a
for i in range(a,b+1):
    if i%d == c:
        print(i, end=" ")