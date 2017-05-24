def case_check(word):
    for x in word:
        if x == "_":
            print("snake_case")
            break
        elif x in "ABCDEFGHIJKLMNOPQSTUVWXYZ":
            print("CamelCase")
            break

word = input("Enter a word in either snake_case or CamelCase: ")

case_check(word)
