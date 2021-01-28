def my_function(x):
    if x[-1] != '0':
        return x[::-1]
    else:
        return my_function(x[:-1])

mytxt = my_function(input())
print(mytxt)