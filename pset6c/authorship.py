# text = ["blah"]

def word_length_histogram(input_text):

    word_histogram = {}

    # Iterated through each element inside text
    for line in input_text:

        # Used the split() list method to split the line_words string into a list with each word being a list item
        line_words = line.split()

        # In this nested loop, quotes get removed and checks if the length of a word is an existing key in the dictionary
        for word in line_words:
            word = word.replace("'", "")

            # If the length is a key, the length of the dictionary is increased by one
            if len(word) in word_histogram.keys():
                word_histogram[len(word)] += 1
            else:
                word_histogram[len(word)] = 1

    return word_histogram


def print_report(word_dict):

    total_words = sum(word_dict.values())

    for len_word in word_dict:
       print(f'Proportion of {len_word}-letter words: 100*{(word_dict[len_word]/total_words)*100:.4f} ({word_dict[len_word]}) ')


def main():

    # Opens the file and then saves the external text in this program as input_text
    with open('romeo_and_juliet_data.txt', 'r') as f:
        input_text = f.readlines()

    # Generates the word_length_histogram from the text data
    word_dict = word_length_histogram(input_text)

    # Prints the results
    print_report(word_dict)

main()
