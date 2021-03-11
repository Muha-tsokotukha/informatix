arr = list(map(int, input().split()))
check = set(arr)
print('Yes' if len(check)==len(arr) else 'No')