x = input()
print(x[2])
print(x[len(x)-2])
print( x[0],x[1],x[2],x[3],x[4], sep="" )
i = 0
for i in range(0, len(x)-2):
    print(x[i], end="")
j = 0
print("")
for j in range(0, len(x)):
    if j%2==0:
        print(x[j], end="")
print("")
j = 0
for j in range(0, len(x)):
    if j%2!=0:
        print(x[j], end="")
print("")
print(x[::-1])
y = x[::-1]
k = 0
for j in range(0, len(y)):
    if j%2==0:
        print(y[j], end="")
print("")
print(len(x))
