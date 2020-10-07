import random as rm


def reversed_sentence(sentence):
    words_list = sentence.split(" ")
    words_list.reverse()
    return " ".join(words_list)


def random_sentence():
    list_of_words = open("words_list.txt", "r").read().split()
    list_of_words = rm.sample(list_of_words, rm.randint(1, 20))
    return " ".join(list_of_words)


my_sentence = random_sentence()
print(my_sentence)
print(reversed_sentence(my_sentence))

