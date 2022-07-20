dic1 = {'key1': 1, 'key2': 3, 'key3': 2}
dic2 = {'key1': 1, 'key2': 2}

for (key, value) in dic1.items() & dic2.items():
    print(f'{key}: {value} is present in both dictionaries')