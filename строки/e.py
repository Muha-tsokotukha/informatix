x = input()
y = x[::-1]
haf = bool(False)
l = x.find("f")
r = 0

if l != -1:
    r = x.find("f", l+1)
    haf = True
if haf == False:
    exit() 
if r != -1:
    print(l,end=" ")
    print(len(x) - (y.find("f")+1))
elif haf == True and r == -1:
    print(l)
