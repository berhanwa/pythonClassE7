jk

def word_length_histogram(text):
    word_histogram = {}

    # Iterated through each element inside text
    for line in text:

        # Used the split() list method to split the line_words string into a list with each word being a list item
        line_words = line.split()

        # In this nested loop, quotes get removed and checks if the length of a word is an existing key in the dictionary
        for word in line_words:
            word = word.replace("'", "")

            if len(word) in list(word_hist.keys()):
                word_histogram(len(word)) += 1

            else:
                word_histogram(len(word)) = 1


def print_report(hist):

