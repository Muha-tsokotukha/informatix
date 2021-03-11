nums = list(map(int, input().split()))
moda = dict()
for x in nums:
    if moda.get(x) == None:
        moda[x] = 1
    else: moda[x] += 1
mx = 0
mxn = 0
for y in moda:
    if moda[y] > mx:
        mx = moda[y]
        mxn = y
print(mxn)