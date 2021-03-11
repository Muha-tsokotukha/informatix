f = open('input.txt','r')
txt = f.read()
words = txt.split()
freaq = dict()

for x in words:
    cnt = 0
    if freaq.get(x) != None:
        continue
    else:
        for y in words:
            if x == y: cnt+=1
    freaq[x] = cnt
print(freaq)