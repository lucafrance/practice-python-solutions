import random as rm
import string


def words_list():
    return open("words_list.txt", "r").read().split()


def password_generator(password_strength=0):
    # 2 random words
    if password_strength == 0:
        return "".join(rm.sample(words_list(), 2))

    characters_list = []
    password_length = 8
    if password_strength >= 1:  # lowercase letters
        characters_list += list(string.ascii_lowercase)
    if password_strength >= 2:  # numbers
        characters_list += list(string.digits)
    if password_strength >= 3:  # uppercase letters
        characters_list += list(string.ascii_uppercase)
    if password_strength >= 4:  # symbols
        characters_list += list(string.punctuation)
    if password_strength >= 5:  # longer password
        password_length = 16

    return "".join(rm.sample(characters_list, password_length))


password_strength = int(input("How strong do you want your password to be 0 to 5? "))
print(password_generator(password_strength))
