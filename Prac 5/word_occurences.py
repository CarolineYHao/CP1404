"""
count the occurrences of words in a string. The program should ask the user for a string, then print the counts of how
many of each word are in the file.
"""

text = input("Text: ")
text_to_word_count = {}
word_length = 0
word_list = sorted(text.split(" "))
for word in word_list:
    if len(word) > word_length:
        word_length = len(word)
    try:
        text_to_word_count[word] += 1
    except KeyError:
        text_to_word_count[word] = 1
# print(text_to_word_count)
for word, count in text_to_word_count.items():
    print("{:{}} : {}".format(word, word_length, count))
