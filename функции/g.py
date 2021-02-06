def power(x,y):
    ans = 1
    if y > 0:
        while y >= 0:
            ans *= x
            y -= 1
        return ans
    elif y < 0:
        while y <= 0:
            ans *= x
            y += 1
        return ans
    else: return 1
    
a = float(input())
b = float(input())
print(pow(a,b))