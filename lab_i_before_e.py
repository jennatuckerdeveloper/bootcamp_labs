word = input("Enter an English word that has an 'e' sound: ")
word = word.lower()
i = 0
def checker(word):
    place = word.find("ie", 0, len(word))
    if word[place - 1] == "c":
        print("no")
    oplace = word.find("ei", 0, len(word))
    if word[oplace - 1] == "c":
        print("yes")
checker(word)
