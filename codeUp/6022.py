str = input()

for i in range(0, 6, 2):
    if (i == 4):
        term = ''
    else:
        term = ' '
    print(str[i:i+2], end=term)
