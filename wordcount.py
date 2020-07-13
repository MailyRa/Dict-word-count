
def list_of_words(file):
    word_count = {}

    file = open(file)

    for line in file:

        line = line.rstrip()
        words =line.split()

        for word in words:
            word_count[word] = word_count.get(word, 0) + 1

    return word_count


def print_the_words(word_dict):

    for word, count in word_dict.items():
        print(word, count)

word_count = list_of_words("test.txt")

print_the_words(word_count)









