# input: hello world
# olleh dlrow
def reverse_word_string(sentence):
    store_word = sentence.split(" ")
    stored_back = []
    for word in store_word:
        word = word[::-1]
        stored_back.append(word)

    output_string = ''
    for word in stored_back:
        output_string = output_string + " " + word
    return output_string


def count_string_letter(string):
    count_dict = {}
    for letter in string:
        if letter in count_dict:
            count_dict[letter] = count_dict[letter] + 1
        else:
            count_dict[letter] = 1
    print(count_dict)

