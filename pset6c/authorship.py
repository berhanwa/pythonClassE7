

def word_length_histogram(text):
    word_histogram = {}

    # Iterated through each element inside text
    for line in text:

        # Used the split() list method to split the line_words string into a list with each word being a list item
        line_words = line.split()

        # In this nested loop, quotes get removed and checks if the length of a word is an existing key in the dictionary
        for word in line_words:
            word = word.replace("'", "")

            # If the length is a key, the length of the dictionary is increased by one
            if len(word) in list(word_hist.keys()):
                word_histogram[len(word)] += 1

            else:
                word_histogram[len(word)] = 1

    return word_histogram


def print_report(hist):

    with open('romeo_and_juliet_data.txt', 'r') as f:
        input_text = f.readlines()
    word_dict = word_length_histogram(input_text)
    total_words = sum(list(word_dict.values()))

    for len_word in word_dicts:
        print('The proportion of ', len_word, '-letter words is ', word_dict(len_word), word_dict(len_word)/total_words)

# def main():
