n = input()
while int(n) - 10 >= 0:
    n = str(n)
    summ = 0
    for x in n:
        summ+=int(x)
    n = summ
print(n)