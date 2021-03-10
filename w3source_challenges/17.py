a = list(map(int,input().split()))
summ = a[0]+a[1]
i = 0
r = True
for i in range(2,len(a)):
    if summ != a[i]:
        r = False
        break
    summ += a[i-1]
print('Yes' if r else 'No')