"""
count the occurrences of words in a string. The program should ask the user for a string, then print the counts of how
many of each word are in the file.
"""

text = input("Text: ")
text_to_word_count = {}
word_list = sorted(text.split(" "))
word_length = max(len(word) for word in word_list)
for word in word_list:
    text_to_word_count[word] = text_to_word_count.get(word, 0) + 1
# print(text_to_word_count)
for word, count in text_to_word_count.items():
    print("{:{}} : {}".format(word, word_length, count))
