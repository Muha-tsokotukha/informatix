nums = []
def is_ugly(num):
        nums.append(num)
        if num == 0:
            return False
        for i in [2, 3, 5]:
            while num % i == 0:
                num /= i
                nums.append(num)
        return num == 1

if is_ugly(int(input())) != 1:
    print(0)
    exit()
else:
    print(*nums)
