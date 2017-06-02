#creating a class
#bullets are what you want it to do
#class that has methods that give answers
#report on the book in a text file
#more advanced would be for it to run as many files as are in a folder

#natural language module, NLTK

import re
from os import system

class Book:
    def __init__(self, file):
        self.file = open(file, "r").read()
        #both opens and returns the file

    def total_char(self):
        """Finds total characters without white spaces."""
        chars = re.findall(r"([\w!.,\?\-'\":;)(\]\[#*<>&%$@_{}])", self.file)
        return len(chars)

    def total_words(self):
        """Finds total word count."""
        #words = re.findall("Achilles", self.file)
        words = re.findall(r"(?<=[\n\r (—\"“-])[A-Za-z'’]+(?=[ ”\",;\.!\?\n\r-—])", self.file)
        return len(words)

    def words_list(self):
        """Creates dictionary of words with number of occurrences."""
        word = {}
        all = re.findall("", self.file)
        for item in all:
            if item not in words:
                word[item] = 1
            elif item in words:
                word[item] += 1


    def lex_density(self):
        """Determines lexical density."""

    def longest_words(self):
        """Creates array of the longest words."""

    def shortest_words(self):
        """Creates array of shortest words."""

    def unique_word_count(self):
        """Finds how many different words are in the book."""

    def rarest_words(self):
        """Finds rarest words in book."""

    def word_frequency(self):
        """Finds number of occurrences of a given word."""

    def sentences(self):
        """Finds the number of sentences."""
        sents = re.findall(r"(?<!\.)(?<=[\da-zI])[\.!\?](?=[ \r\n'\"”])", self.file)
        osents = re.findall(r":--", self.file)
        return len(sents) + len(osents)

    def average_sentence_length(self):
        """Finds average sentence length."""

    def min_sentence_length(self):
        """Finds min sentence length."""

    def max_sentence_length(self):
        """Finds max setence length."""

    def call_mimic(self):
        """Calls mimic module."""

    def count_syllables(self):
        """Counts syllables in an entry."""

    def ari_score(self):
        """Finds ARI score."""

    def report(self):
        """Outputs report file."""

iliad = Book("iliad.txt")
#print(iliad.sentences())
#system("ls")
#print(iliad.fil# e)
#print(iliad.total_char())
rld = Book("the_room_with_the_little_door.txt")
#print(rld.sentences())
print(iliad.total_words())
print(rld.total_words())