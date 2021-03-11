n = int(input())
Digits = list()

while n > 0:
    if n < 10:    
        Digits.append(n)
        break
    Digits.append(int(n)%10)
    n = n // 10
for x in range(len(Digits)):
    for y in range(len(Digits)):
        for z in range(len(Digits)):
            if x != y and y != z and x != z:
                print(Digits[x],Digits[y],Digits[z], sep='')