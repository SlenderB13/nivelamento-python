items = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}

for key, value in sorted(items.items(), key=lambda value: value[1], reverse=True)[0:3]:
    print(f'{key}: {value}')