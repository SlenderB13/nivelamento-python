from collections import defaultdict

values = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

dict_values = defaultdict(list)

for key, value in values:
    dict_values[key].append(value)
print(dict(list(dict_values.items())))