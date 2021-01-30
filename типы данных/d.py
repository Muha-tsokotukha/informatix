ans = 4
n = 1
m = 9
while m > 0:
    if m%2 == 0:
        ans += 4/(n+2)
        n += 2
        m-=1
    else:
        ans -= 4/(n+2)
        n += 2
        m-=1

print(ans)
