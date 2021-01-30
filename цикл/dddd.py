x = int(input())
d = int(input())
cnt = 0
while x>0:
    if d == x%10:
        cnt += 1
    x = x//10

print(cnt)