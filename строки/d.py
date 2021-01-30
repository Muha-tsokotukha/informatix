words = input()
x = words.find(" ")
print(words[(x+1):] , words[:x] )