a = list(sorted(map(int,input().split())))
indAns = 0
b = dict()
for x in a:
    if b.get(x) != None:
        b[x] += 1
    else: b[x] = 1
for y in b:
    if b[y] != 2:
        print(y)
        exit()