nums = list(map(int, input().split()))
cntZero = 0
for x in nums:
    if x == 0:
        nums.remove(x)
        cntZero+=1
while cntZero > 0:
    nums.append(0)
    cntZero -= 1
print(*nums)