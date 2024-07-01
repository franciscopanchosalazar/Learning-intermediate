# This code asks the user for a sentence and create an acronym out of the words
print("Enter a sentence to create an acronym\nEnter quit to leave\n")

my_acronym = ''

while True:
    user_phrase = input("Enter phrase: ")

    if user_phrase.lower() == 'quit':
        print('YOU ENTER QUIT\nBye - Bye')
        break

    every_word = user_phrase.split(" ")  # Creates a list with every word separated by spaces

    for i in every_word:
        my_acronym += i[0].upper()

    #print(every_word)
    print(f'The acronym for: {user_phrase} is -----> {my_acronym}\n')
    every_word.clear()
    my_acronym = ''
