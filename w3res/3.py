a = list(map(int, input().split()))
k = 0
while len(a) > 0:
    k = (2+k)%len(a)
    print(a[k])
    a.pop(k)