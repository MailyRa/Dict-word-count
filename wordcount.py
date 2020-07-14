import sys

from collections import Counter

# print(sys.argv)

def list_of_words(file):
    word_count = {}

    file = open(file)

    for line in file:

        line = line.rstrip()
        words =line.split()


        for word in words:

            word = word.lower()    
            word = word.strip("'\",.!?-#$%^&();:_")
            #is thre another way to strip special characters?

            word_count[word] = word_count.get(word, 0) + 1



    return word_count


def print_the_words(word_dict):

    for word, count in word_dict.items():
        print(word, count)

final_word_count = list_of_words(sys.argv[1])

print_the_words(final_word_count)

# def list_of_words(file):

#     word_count = []

#     file = open(file)


#     for line in file:

#         line = line.strip()
#         words = line.split()

#         for word in words:

#             word = word.lower()    
#             word = word.strip("'\",.!?-#$%^&();:_")

#         word_count = word + 1

#     print(word_count)

#     cnt = Counter()

#     for word in word_count:
#         cnt[word] += 1

    


# print(list_of_words(sys.argv[1]))






