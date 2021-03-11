x = list(sorted(list(map(int, input().split()))))
y = list(sorted(list(map(int, input().split()))))
z = list(sorted(list(map(int, input().split()))))
ans = set()
n = int(input())
for a in x:
    for b in y:
        for c in z:
            if a+b+c == n:
                ans.add(tuple([a,b,c]))
print(ans)