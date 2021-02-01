import math
a = float(input())
b = float(input())
c = float(input())
p = (a + b + c) / 2
s = float('%.6f' % math.sqrt(p*(p - a)*(p - b)*(p - c)))
print(s)