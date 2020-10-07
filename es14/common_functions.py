import random as rm


def random_integer_list():
    list_len = rm.randint(1, 20)
    random_list = []
    while list_len:
        random_list.append(rm.randint(1, 10))
        list_len -= 1
    random_list.sort()
    return random_list