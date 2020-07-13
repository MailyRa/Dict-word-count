# def list_of_words(file):

#     list_words = []

#     with open(file) as text_file:
#         for line in text_file:

#             line = line.rstrip()
#             words =line.split()

#             list_words.append(words)
#     return list_words

# print(list_of_words("test.txt"))


# def num_words(words):

#     word_count = {}

#     for word in words:
#         word_count[word] = word_count.get(word, 0) +1

#     return word_count

def list_of_words(file):
"""opens the file and counts how many spaces"""
    list_words = []

    file = open(file)

    for line in file:

        line = line.rstrip()
        words =line.split()

        list_words.append(words)

    return list_words

# print(list_of_words("test.txt"))



def poem(words):
""" Separates the words by space"""

#made my list a dictionary to access it later
    word_count = {}

#I want to do a for loop of my 
    for word in words:
        word_count[word] = word_count.get(word, 0) +1

    return words_count


def print_the_words(num_words):
""" Print the words"""
    for word, count in num_words.items()
        print(word, count)









