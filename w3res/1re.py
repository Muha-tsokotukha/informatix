import re
word = input()
pattern = '[^a-zA-Z0-9]'
correct = re.findall(pattern, word)
if len(correct) == 0:
    print('Yes')
else: print('No')
