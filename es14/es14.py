import common_functions as cm


def remove_duplicates1(input_list):
    new_list = []
    for element in input_list:
        if element not in new_list:
            new_list.append(element)
    return new_list


def remove_duplicates2(input_list):
    return list(set(input_list))


my_list = cm.random_integer_list()
print(my_list)
print(remove_duplicates1(my_list))
print(remove_duplicates2(my_list))
