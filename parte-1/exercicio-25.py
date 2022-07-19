list = input('Type the values you want, separate by comma[EX: 1,2,3,4]: ').split(',')

value = input('Which value do you want to check in the list?')

if value in list:
    print(f'{value} is in position {list.index(value)} in the list')
else:
    print('The value is not in the list')
