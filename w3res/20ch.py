seq = list(map(int, input().split()))
i = 2
d = seq[1] - seq[0]

isseq = True
while i < len(seq):
    if seq[i] - seq[i-1] != d:
        isseq = False
        break
    i += 1
print('Yes' if isseq else 'No')