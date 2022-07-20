values = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]

new_list = set(value for dic in values for value in dic.values())
print('Unique values:', new_list)