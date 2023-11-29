#Name: Gianni Russell
#gianni.russell07@myhunter.cuny.edu
#Date: October 12, 2023


def count_plurals(nouns):
    words = nouns.split()
    num_plurals = sum(word.endswith('s') for word in words)
    return len(words), num_plurals / len(words)

nouns = input("Enter nouns: ")
num_words, fraction_plurals = count_plurals(nouns)
print("Number of words: ", num_words)
print("Fraction of your list that is plural is", fraction_plurals)
