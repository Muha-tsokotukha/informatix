f = open('input.txt','r')
txt = f.read()
words = txt.split()
freaq = dict()

for x in words:
    cnt = 0
    for y in x:
        if freaq.get(y) == None:
            freaq[y] =1
        else: freaq[y] += 1
#print(freaq)
for x in freaq:
    print( x,"-", freaq[x] )