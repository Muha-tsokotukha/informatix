import math
ans = 0
m = 10
k = 1
while k <= 10:
    ans += (1/m**2)
    k += 1
    m -= 1

print( math.sqrt(ans*6)  )
