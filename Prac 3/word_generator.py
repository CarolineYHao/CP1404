"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random
VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"


def main():
    word_format = input("Enter word pattern where 'c' is a consonant and 'v' is a vowel. (eg. ccvcvvc): \n").lower()
    is_valid_format(word_format)
    while is_valid_format(word_format) is False:
        print("Only 'c' and 'v' are allowed")
        word_format = input("Enter word pattern where 'c' is a consonant and 'v' is a vowel. (eg. ccvcvvc): \n").lower()
    word = ""
    for kind in word_format:
        if kind == "c":
            word += random.choice(CONSONANTS)
        else:
            word += random.choice(VOWELS)
    print(word)


def is_valid_format(word_format):
    for char in word_format:
        if char in 'cv':
            return True
        else:
            return False


main()
