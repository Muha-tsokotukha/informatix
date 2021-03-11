def is_ugly(num):
        if num == 0:
            return False
        for i in [2, 3, 5]:
            while num % i == 0:
                num /= i
        return num == 1

x = 0
for x in range(0,int(input())+1):
    if is_ugly(x):
        print(x,end=" ")