







from random import randint



def play():
    random_int = randint(0, 100)

    while True:
        user_guess = int(input("what number did we guess (0,100)?"))

        if user_guess == randint:
            print(f"you found the number({random_int}). congrats!")
            break

        if user_guess < random_int:
            print("yor number is less than the number we guessed.")
            continue

        if user_guess > random_int:
            print("your number is more than the number we guessed.")
            continue

        if __name__ == '_name_':
            play()
