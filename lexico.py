number  = int(input('Enter number of words:'))
list =[]
for x in range(number):
    list.append(input(f'{x}. Enter: ').lower())
lex_each = []
for i in list:
    min=i[0]
    for x in i:
        if ord(x)<ord(min):
            min=x
    lex_each.append(min)
lex_each.sort()
print(''.join(lex_each))
