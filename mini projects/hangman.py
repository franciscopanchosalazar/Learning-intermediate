from words import words
import random
import string


def select_word(words_list):
    chosen_word = random.choice(words_list)
    while "-" in chosen_word or " " in chosen_word:
        chosen_word = random.choice(words_list)

    return chosen_word.upper()


def hangman():
    actual_chosen_word = select_word(words)
    word_letters = set(actual_chosen_word)
    alphabet = set(string.ascii_uppercase)
    user_used_letters = set()
    user_lives = 6

    while len(word_letters) > 0 and user_lives != 0:
        print(f"Lives: {user_lives}")
        to_show = [letter if letter in user_used_letters else "-" for letter in actual_chosen_word]
        print(str(to_show) + "\n")
        user_letters = input("Enter a letter: ").upper()

        if user_letters in alphabet and user_letters not in user_used_letters:
            user_used_letters.add(user_letters)
            if user_letters in word_letters:
                word_letters.remove(user_letters)
            else:
                user_lives -= 1

        elif user_letters in user_used_letters:
            print("You already used that letter\n")

        else:
            print("{} is not a valid character\n" .format(user_letters))

    if user_lives == 0:
        print(f"You have lost, the word was {actual_chosen_word} 😥")

    else:
        print(f"You won, the word was actually {actual_chosen_word} 😉")


hangman()


