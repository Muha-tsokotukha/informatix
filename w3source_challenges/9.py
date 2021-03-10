a = list(map(int,input().split()))
ans = set()
i = 0
for i in range(0, len(a)):
    for j in range(i+1,len(a)):
        for k in range(j+1,len(a)):
            if a[i]+a[j]+a[k] == 0:
                temp = sorted((a[i],a[j],a[k]))
                t = tuple(temp)
                ans.add(t) 
   
print(*ans)