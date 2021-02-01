x = float(input())
y = int(x * 10) % 10
if y >= 5:
    print(int(((x*10)-y)/10 + 1)    )
else:
    print( int(((x*10)-y)/10  ) )