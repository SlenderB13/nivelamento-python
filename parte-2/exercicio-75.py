def remove_from_list(list, number):
    while number in list:
        list.remove(number)
    print(len(list))

remove_from_list([1,2,3,4,5,6,7,5], 5)
remove_from_list([10, 10, 10, 10, 10], 10)
remove_from_list([10, 10, 10, 10, 10], 20)
remove_from_list([], 1)