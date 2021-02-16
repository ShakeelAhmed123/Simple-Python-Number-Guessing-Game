import random

print("******************")
print("*WELCOME STRANGER*")
print("*      TO A      *")
print("*NUMBER GUESSING *")
print("*      GAME      *")
print("******************")

answer = random.randint(0, 20)


def easy_mode():
    print(">.< PLEASE GUESS THE NUMBER >.<")

    try:
        user_guess = int(input(">"))

        if user_guess == answer:
            print("\n~You have won, but at what cost~")

        elif user_guess > answer:
            print("~You went higher than the actual answer~\n")
            easy_mode()

        elif user_guess < answer:
            print("~You went lower than the actual answer~\n")
            easy_mode()

    except ValueError:
        print(">.< Please enter a number >.<")


def hard_mode():
    print(">.< PLEASE GUESS THE NUMBER >.<")
    try:

        tries = 0
        while tries < 5:
            user_guess = int(input(">"))

            if user_guess == answer:
                print()
                print("~You have won, but at what cost~")
                exit()

            elif user_guess > answer:
                print("~You went higher than the actual answer~\n")
                tries += 1
                if tries == 5:
                    print(f"\n~You failed at guessing the correct number. You had {tries} tries~")
                else:
                    print(">.< PLEASE GUESS THE NUMBER >.<")

            elif user_guess < answer:
                print("~You went lower than the actual answer~\n")
                tries += 1
                if tries == 5:
                    print(f"\n~You failed at guessing the correct number. You had {tries} tries~")
                else:
                    print(">.< PLEASE GUESS THE NUMBER >.<")
    except ValueError:
        print(">.< Please enter a number >.<")


def pre_game():
    print("So, How would you like to play? Easy or Hard?")
    print("~1 for Easy and 2 for Hard. Press 3 for HELP~")
    operation = input(">")

    if operation == "1":
        easy_mode()

    elif operation == "2":
        hard_mode()

    if operation == "3":
        print("\n~In Easy mode you have unlimited tries.~\n ~And in Hard mode, you only have 5 tries.~\n")
        pre_game()


pre_game()
