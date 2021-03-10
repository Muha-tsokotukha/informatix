n = int(input())
power = True
while n>0:
    if n == 1:
        break
    if n%2 != 0 and n != 1:
        power = False
        break
    n/=2
print("Yes" if power else 'No')