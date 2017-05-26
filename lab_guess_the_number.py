from random import randint
import time
print('Welcome to the game Guess A Number!')
while True:
    try:
        level = int(input("""Choose a difficulty level:
        1. Easy
        2. Moderate
        3. Hard
        4. Very Hard
        5. Aggrevating
        6. Quit """))
    except ValueError:
    #this allows your progam to keep running
    #otherwise, Python would kick the user out and stop running
        print('I did not understand that.')
        continue
    if level == 1:
        rng = 10
        break
    elif level == 2:
        rng = 100
        break
    elif level == 3:
        rng = 1000
        break
    elif level == 4:
        rng = 10000
        break
    elif level == 5:
        rng = 100000
        break
    elif level == 6:
        quit()

computer_guess = randint(1, rng)
user_guess = int(input("Guess a number "))

play = True
score = 0

while play:
    time.sleep(2)
    if user_guess > rng:
        score = score + 1
        print("Score: ", score)
        print("Don't guess over", rng, ".")
        user_guess = int(input("Guess a number: "))
    elif user_guess < computer_guess:
        score = score + 1
        print("Score: ", score)
        user_guess = int(input('Guess higher: '))
    elif user_guess > computer_guess:
        score = score + 1
        print("Score: ", score)
        user_guess = int(input('Guess lower: '))
    elif user_guess == computer_guess:
        print('You win! Computer guessed: ', computer_guess)
        print(score)
        break
