import re
word = input()
pattern = '.*a(0|b+)'
correct = re.findall(pattern, word)
if len(correct) != 0:
    print('Yes')
else : print('No')
print(correct)