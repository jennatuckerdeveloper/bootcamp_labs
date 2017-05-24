print("Welcome to Mad Libs!")
noun = input("Type a noun: ").lower()
ajective = input("Type a ajective: ").lower()
exclamation = input("Type an exclamation: ").capitalize()
adverb = input("Type an adverb: ").lower()

print("{}, John! Grab that {}!  Otherwise this {} weather will ruin us! \
And run {} when you do!" .format(exclamation, noun, ajective, adverb))
