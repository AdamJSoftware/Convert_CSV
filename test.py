a = ['num', 'a', 'b', 'c', 'num']
print([index for index, char in enumerate(a) if char == 'num'][1] - [index for index, char in enumerate(a) if char == 'num'][0] -1)
print()