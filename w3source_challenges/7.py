numbers = map(int,input().split())
numbers = sorted(numbers)
missing = list()
i = 0
while i < len(numbers):
    if i == len(numbers)-1:
        break
    if numbers[i] + 1 != numbers[i+1]:
        missing.append( numbers[i] + 1)
        k = 2
        while numbers[i] + k != numbers[i+1]:
            missing.append(numbers[i]+k)
            k += 1
    i += 1
print(missing)