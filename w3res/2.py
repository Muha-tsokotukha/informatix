from random import shuffle 
from math import factorial
char_list = ['a','e','i','o','u']
n = 0
ans = set()

while factorial(len(char_list)) > n:
    shuffle(char_list)
    ans.add(''.join(char_list))
    n += 1
print(*ans)