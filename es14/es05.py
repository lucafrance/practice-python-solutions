import common_functions as cm


def list_common_elements(list1, list2):
    common = set()
    for num in a + b:
        if num in a and num in b:
            common.add(num)
    return list(common)


a = cm.random_integer_list()
b = cm.random_integer_list()

print(a)
print(b)
print(list_common_elements(a, b))