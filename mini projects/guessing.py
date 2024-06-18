import random

computer_number = random.randint(0, 20)

tries = 0

print("The computer generated a number between 0 and 20, you have FIVE chances to get it\n")
while tries < 5:
    try:
        user_guess = int(input("Guess: "))
        if user_guess == computer_number:
            print("Congrats, you got the number\n")

            keep = "a"
            while keep != "Y":
                keep = input("Would you like to play again? (y/n): ").upper()
                if keep == "Y":
                    tries = 0
                    computer_number = random.randint(0, 20)
                    print("\n A new number has been generated.\n")
                elif keep == "N":
                    print("\nBye - Bye")
                    quit()
                else:
                    print("{} is not a valid option\n".format(keep))

        elif user_guess > computer_number:
            print("You should go down\n")
            tries += 1

        elif user_guess < computer_number:
            print("You should go up\n")
            tries += 1

    except ValueError:
        print(f'\nNot a valid option\n')

print("\nSorry, you lost, the number was {}" .format(computer_number))
