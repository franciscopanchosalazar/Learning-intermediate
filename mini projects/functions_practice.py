# Write a function named capital_indexes. The function takes a single parameter,
# which is a string. Your function should return a list of all the indexes in the string
# that have capital letters.

# Solution one:
def capital_indexes(user_string: str):
    capital = []
    for i in user_string:
        if i == i.upper() and i != ' ':
            capital.append(user_string.index(i))

    return capital


print(capital_indexes('HellO WorlD')) # output [0, 4, 6, 10]


# Solution two:

def capital_indexes_two(user_string: str):
    capital = []
    for i in user_string:
        if i.isupper():
            capital.append(user_string.index(i))

    print(capital)


capital_indexes_two('HeLlO')


# Middle letter
# Write a function named mid that takes a string as its parameter.
# #Your function should extract and return the middle letter.
# #If there is no middle letter, your function should return the empty string.

def middle_letter(user_word=''):
    word_length = len(user_word)
    if word_length % 2 == 0:
        print('" "')
    else:
        middle_index = int((word_length/2) - 0.5)
        print(f'"{user_word[middle_index]}"')


middle_letter('abc')    # output " "
middle_letter("aaaa")   # output b


# Online status
# The aim of this challenge is, given a dictionary of people's online status,
# to count the number of people who are online.

# For example, consider the following dictionary:

# statuses = {
    # "Alice": "online",
    # "Bob": "offline",
    # "Eve": "online",
# }

# In this case, the number of people online is 2.
# Write a function named online_count that takes one parameter.
# The parameter is a dictionary that maps from strings of names to the string
# "online" or "offline", as seen above.
# Your function should return the number of people who are online.

def online_count(my_dict: dict):
    online = 0
    my_dict_values = my_dict.values()

    for i in my_dict_values:
        if i == 'online':
            online += 1

    return online


statuses = dict(Alice="online", Bob="offline", Eve="online")
online_people = online_count(statuses)

print(f'There are {online_people} online people')


# Type check
# Write a function named only_ints that takes two parameters.
# Your function should return True if both parameters are integers, and False otherwise.
# For example, calling only_ints(1, 2) should return True,
# while calling only_ints("a", 1) should return False.

def only_ints(a, b):
    if type(a) is int and type(b) is int:
        return True
    else:
        return False


print(only_ints(2, 3))
print(only_ints('Hi', 3))


# Double letters
# The goal of this challenge is to analyze a string to check if it contains
# two of the same letter in a row. For example, the string "hello" has l twice in a row,
# while the string "nono" does not have two identical letters in a row.
# Define a function named double_letters that takes a single parameter.
# The parameter is a string. Your function must return True
# if there are two identical letters in a row in the string, and False otherwise.


# Solution one:
def double_letters(user_string: str):
    a = 0
    for i in user_string:
        comparator_index = user_string.index(i) + 1

        if comparator_index < len(user_string):
            comparator_letter = user_string[comparator_index]
            if i == comparator_letter:
                a += 1
                print(i, comparator_letter)
                break

    if a > 0:
        print(f"\n{True}")
    else:
        print(f"\n{False}")


double_letters('pan')

# Adding and removing dots
# Write a function named add_dots that takes a string and adds "." in between each letter.
# For example, calling add_dots("test") should return the string "t.e.s.t".
# Then, below the add_dots function, write another function named remove_dots
# that removes all dots from a string. For example, calling remove_dots("t.e.s.t") should return "test".
# If both functions are correct, calling remove_dots(add_dots(string)) should return back the original
# string for any string.
# (You may assume that the input to add_dots does not itself contain any dots.)


def add_dots(user_string):
    user_string_dots = ''
    final_str = ''
    for i in user_string:
        user_string_dots += i + '.'

    for i in user_string_dots[0: len(user_string_dots) - 1]:
        final_str += i

    print(final_str)


# Solution two:
def add_dots_two(user_string):
    x = ".".join(user_string)

    print(x)


add_dots('pancho')
add_dots_two('lore')


# Counting syllables
# Define a function named count that takes a single parameter.
# The parameter is a string. The string will contain a single
# word divided into syllables by hyphens

# Solution one:
def count(word):
    syllables = word.count("-") + 1
    print(syllables)


count('fran-cis-co')


# Solution two:
def count_two(word: str):
    syllables = len(word.split('-'))
    print(syllables)


count_two('com-pu-ta-dor')


# Anagrams
# Write a function named is_anagram that takes two strings as its parameters.
# Your function should return True if the strings are anagrams, and False otherwise

# Solution one:
def anagram(word_one, word_two):
    w1 = {}
    w2 = {}
    for i in word_one:
        if i not in w1:
            a = word_one.count(i)
            w1[i.upper()] = a

    for i in word_two:
        if i not in w2:
            a = word_two.count(i)
            w2[i.upper()] = a

    sorted_w1 = sorted(w1.items())
    sorted_w2 = sorted(w2.items())
    # print(f"w1 = {sorted_w1}\nw2 = {sorted_w2}\n") # TESTER

    if sorted_w1 == sorted_w2:
        return True
    else:
        return False


# Solution two:

def anagram_two(word_one, word_two):
    sw1 = sorted(word_one.upper())
    sw2 = sorted(word_two.upper())
    # print(f"sw1 = {sw1}\nsw2 = {sw2}\n") # TESTER

    if sw1 == sw2:
        return True
    else:
        return False


print(anagram('typhoon', 'opython'))

print(anagram_two('toro', 'roto'))


# Flatten a list
# Write a function that takes a list of lists and flattens it into a one-dimensional list.
# Name your function flatten. It should take a single parameter and return a list.

# Solution one:
def flatten(l1, l2):
    nl = []
    for i in l1:
        nl.append(i)

    for i in l2:
        nl.append(i)

    print(nl)


# Solution two:
def flatten_two(*args):
    nl = []
    co = 0

    for i in args:
        for j in args[co]:
            # print(f"I = {i}, J = {j}")
            nl.append(j)
        co += 1
    print(nl)


# Solution three:
def flatten_three(*args):
    nl = []
    co = 0

    while co < len(args):
        for i in args[co]:
            # print(f"I = {i}")
            nl.append(i)
        co += 1
    print(nl)


flatten([9, 6, 9, 1], [1, 4, 7, 9])
flatten_two([8, 1, 5, 9], [6, 8, 1, 5])     # Add as many lists as you want
flatten_three([8, 4, 1, 3], [0, 2, 5, 5])   # Add as many lists as you want


# Min-maxing
# Define a function named largest_difference that takes a list of numbers as its only parameter.
# Your function should compute and return the difference between the largest and smallest number in the list.

def largest_difference(user_list):
    min_num = 100
    max_num = -100

    for i in user_list:
        if 100 >= i > max_num:
            max_num = i
        elif -100 <= i < min_num:
            min_num = i

    print("min %s max %s" % (min_num, max_num))
    return max_num - min_num


a = largest_difference([6, 1, -30, -101, 4, 3, 3, 99, 102])
print(a)


# Divisible by 3
# Define a function named div_3 that returns True if its single integer parameter is divisible by 3
# and False otherwise

def div_3(num):
    return True if num % 3 == 0 else False


print(div_3(5))     # Return False
print(div_3(15))    # Return True

# Up and down
# Define a function named up_down that takes a single number as its parameter.
# Your function return a tuple containing two numbers; the first should be
# one lower than the parameter, and the second should be one higher.


def up_down(num):
    d = num - 1
    u = num + 1
    return d, u


num_to_evaluate = 345
down_value, up_value = up_down(num_to_evaluate)
print(f"{down_value} - '{num_to_evaluate}' - {up_value}")


# Consecutive zeros
# The goal of this challenge is to analyze a binary string consisting of only zeros and ones.
# Your code should find the biggest number of consecutive zeros in the string.

def consecutive_zeros(bin_number):
    zeros = 0

    split_bin = bin_number.split('1')
    print(split_bin)
    for i in split_bin:
        if len(i) > zeros:
            zeros = len(i)

    return zeros


b_num = "00100000000100000100001"
print(consecutive_zeros(b_num))
print(consecutive_zeros("1001101000110"))

