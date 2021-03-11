nums = input().split() 
x1 = ''
x2 = ''

for a in reversed(nums[0]):
    x1+=a
for a in reversed(nums[1]):
    x2+=a

summint = str(int(x1) + int(x2))
for x in reversed(summint):
    print(x,end='',sep='')