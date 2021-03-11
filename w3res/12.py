n = list(input().split())
ans = set()
for x in n:
    for y in n:
        for z in n:
            if x != y and y != z and x != z:
                ans.add(x+y+z)
print(sorted(ans))