jk

def word_length_histogram(text):
    word_histogram = {}

    for line in text:

        # Used the split() list method to split the line_words 
        line_words = line.split()
        for word in line_words:
            word = word.replace("'", "")

            if len(word) in list(word_hist.keys()):
                word_histogram(len(word)) += 1

            else:
                word_histogram(len(word)) = 1


def print_report(hist):

