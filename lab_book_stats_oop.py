#creating a class
#bullets are what you want it to do
#class that has methods that give answers
#report on the book in a text file
#more advanced would be for it to run as many files as are in a folder

#natural language module, NLTK

import re
#from os import system

import nltk

import operator

class Book:
    def __init__(self, data_file):
        self.data_file = open(data_file, "r").read()
        #both opens and returns the file

    def total_char(self):
        #add without spaces and label them
        """Finds total characters without white spaces."""
        chars = re.findall(r"([\w!.,\?\-'\":;)(\]\[#*<>&%$@_{}])", self.data_file)
        return len(chars)

    def words(self):
        pattern = re.compile(r"""
                             (?<=[\s(_—‘"“\-])
                             [èA-Za-z'’]+
                             (?:[-.]?[èA-Za-z'’]+)*
                             (?=[\s”’"),;:\.!\?\-_—])
                             """, re.VERBOSE)
        matches = pattern.findall(self.data_file)
        return matches

    def words_list(self):
        """Creates dictionary of words with number of occurrences."""
        word = {}
        #sorter = []
        matches = self.words()
        for item in matches:
            item = item.lower()
            if item not in word:
                #sorter.append(item)
                word[item] = 1
            elif item in word:
                word[item] += 1
        #sorter = sorted(sorter)
        #for item in sorter:
        return word

    def words_list2(self):
        word_freq = nltk.FreqDist(self.data_file)
        return word_freq

    def total_words(self):
        """Finds total word count."""
        #words = re.findall("Achilles", self.file)
        matches = self.words()
        return len(matches)

    def lex_density(self):
        """Determines lexical density."""

    def longest_word(self):
        """Creates array of the longest words."""
        dict = self.words_list()
        largest_word = [""]
        for key in dict.keys():
            if len(key) > len(largest_word[0]):
                largest_word = [""]
                largest_word[0] = key
            elif len(key) == len(largest_word[0]):
                largest_word.append(key)
        return largest_word

    def longest_words(self):
        """Uses library to creat list of longest words."""
        dict = self.words_list()
        sorted_dict = sorted(dict.items(), key=lambda word: len(word[0]))
        return sorted_dict[-9:]

    def shortest_words(self):
        """Creates array of shortest words."""
        dict = self.words_list()
        sorted_dict = sorted(dict.items(), key=lambda word: len(word[0]))
        return sorted_dict[:20]

    def most_common_words(self):
        dict = self.words_list()
        sorted_dict = sorted(dict.items(), key=operator.itemgetter(1))
        return(sorted_dict[:9])

    def unique_word_count(self):
        """Finds how many different words are in the book."""
        dict = self.words_list()
        answer = len(dict.keys())
        return answer

    def rarest_words(self):
        """Finds rarest words in book."""
        dict = self.words_list()
        sorted_dict = sorted(dict.items(), key=operator.itemgetter(1))
        return sorted_dict[0:199]

    def word_frequency(self):
        """Finds number of occurrences of a given word."""
        return self.words_list()

    def sentences(self):
        """Creates a list of sentences."""
        sents = re.findall(r"(?:(?<![\.(Mr|Dr|Mrs)])(?<=[\da-zI])[\.!\?](?=[ \r\n'\"”]))|(?::--)", self.data_file)
        return sents

    def average_sentence_length(self):
        """Finds average sentence length."""
        av = []
        sents = self.sentences()
        new_sents = []
        for s in sents:
            while "\n\n" in s:
                s = s[s.index("\n\n") + 2:]
            new_sents.append(s)
        for sent in new_sents:
            words = self.words()
            sent_len = len(words)
            av.append(sent_len)
        return sum(av) / len(av)

    def min_sentence_length(self):
        """Finds min sentence length."""
        dict_lens = {}
        sents = self.sentences()
        new_sents = []
        for s in sents:
            while "\n\n" in s:
                s = s[s.index("\n\n") + 2:]
            new_sents.append(s)
        for sent in new_sents:
            words = self.words()
            sent_len = len(words)
            if sent not in  dict_lens:
                dict_lens[sent] = sent_len
        sorted_dict = sorted(dict_lens.items(), key=lambda sent: len(sent[0]))
        return sorted_dict[:9]

    def max_sentence_length(self):
        """Finds max setence length."""
        dict_lens = {}
        sents = self.sentences()
        new_sents = []
        for s in sents:
            while "\n\n" in s:
                s = s[s.index("\n\n") + 2:]
            new_sents.append(s)
        for sent in new_sents:
            words = self.words()
            sent_len = len(words)
            if sent not in dict_lens:
                dict_lens[sent] = sent_len
        sorted_dict = sorted(dict_lens.items(), key=lambda sent: len(sent[0]))
        return sorted_dict[-9:]

    def call_mimic(self):
        """Calls mimic module."""

    def count_syllables(self):
        """Counts syllables in an entry."""

    def ari_score(self):
        """Finds ARI score."""

    def report(self):
        """Outputs report file."""

iliad = Book("iliad.txt")
rld = Book("the_room_with_the_little_door.txt")
# print(iliad.total_char())
# print(rld.total_char())
print(iliad.sentences()) #printing funny
print(rld.sentences()) #printing funny
# print(iliad.words())
# print(rld.words())
# print(iliad.words_list())
# print(rld.words_list())
# print(iliad.words_list2())
# print(rld.words_list2())
# print(iliad.total_words())
# print(rld.total_words())
# print(iliad.lex_density())
# print(rld.lex_density())
# print(iliad.longest_word())
# print(rld.longest_word())
# print(iliad.longest_words())
# print(rld.longest_words())
# print(iliad.shortest_words())
# print(rld.shortest_words())
# print(iliad.most_common_words())
# print(rld.most_common_words())
# print(iliad.unique_word_count())
# print(rld.unique_word_count())
# print(iliad.rarest_words())
# print(rld.rarest_words())
# print(iliad.word_frequency())
# print(rld.word_frequency())
# print(iliad.sentences())
# print(rld.sentences())
# print(iliad.average_sentence_length())
# print(rld.average_sentence_length())
# print(iliad.min_sentence_length())
# print(rld.min_sentence_length())
# print(iliad.max_sentence_length())
# print(rld.max_sentence_length())