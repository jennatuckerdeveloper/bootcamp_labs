word = input("Enter a word or phrase to test without punctuation: ")

def palindrome(word):
    word = word.lower()
    for x in word:
        if x == " ":
            word = word.replace(" ", "")
    word2 = word[::-1]
    if word == word2:
        print("Yes")
    else:
        print("No")

palindrome(word)
