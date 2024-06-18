import random

winning_number = random.randint(0, 27)  # Creates a number the user has to match
game_numbers = []   # Here we will storaging the numbers assigned to the keys in the options_dict
chosen_values = []  # Keys chosen by the user will be storage here
winning_number_scratch = "x"  # Controls the while loop
matches_counter = 0     # Counts how many times the user match the winning number

options_dict = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0,
                "m": 0, "n": 0, "ñ": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0,
                "x": 0, "y": 0, "z": 0}

for i in range(0, 27):
    game_numbers.append(random.randint(0, 27))

# put in a list all the keys from the dictionary
x = list(options_dict.keys())

# Assign the numbers from the game_numbers list to the keys in the options_dict
for i in range(0, len(x)):
    options_dict[x[i]] = game_numbers[i]

# print(options_dict)

# User Interaction Section

print("SCRATCH GAME")

while winning_number_scratch != "Y":
    winning_number_scratch = input("\nEnter ´Y´ to get your winning number or ´N´ to quit the game: ").upper()
    if winning_number_scratch == "Y":
        print("\nWinning number: {}".format(winning_number))
    elif winning_number_scratch == "N":
        print("\nBye-Bye")
        quit()
    else:
        print("{} is not a valid option, please try again!!!".format(winning_number_scratch))


print("\nNow You have to scratch 10 out of the 27 options (a to z), If you match the winning number two times, then \
you win.\n\nLets go and choose.")

for i in range(1, 11):  # Gives us the ten chances to scratch
    choosing = input(f"{i}- Choose: ")

    if choosing in chosen_values:
        # del options_dict[choosing]
        print(f"YOU ALREADY SCRATCHED ¨{choosing}¨")

    else:
        choosing_value = options_dict.get(choosing, f"{choosing} is not a valid option")
        print(f"{choosing_value}")
        chosen_values.append(choosing)

        if choosing_value == winning_number:
            matches_counter += 1
            if matches_counter == 2:
                print("\nYou got two matches, you Win\nSee you soon")
                quit()

print("\nSorry, you lost")
