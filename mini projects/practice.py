import random

"""
# Exercise one
# Find the mean of every list in a 2D matrix

import random

# Solution one:

# Creates a list with 3 random numbers in it and append it to the matrix list
matrix = []
for lsts in range(3):   # determines how many list will be in the matrix list
    lst = [random.randint(1, 10) for i in range(3)]
    matrix.append(lst)

lsts_mean = []
for i in matrix:
    lsts_mean.append(sum(i)/len(i))

print(f"Matrix one: {matrix}")
print(f"Every list in matrix one average´s: {lsts_mean}\n")


# Solution two (short version):
matrix_2 = [[random.randint(1, 10) for i in range(3)] for i2 in range(3)]
means = [sum(x)/len(x) for x in matrix_2]

print(f"Matrix two: {matrix_2}")
print(f"Every list in matrix two average´s: {means}")
"""

"""
# Exercise two:
import random
# Creates a 5X5 matrix
sqr_matrix = [[random.randint(1, 10) for elements in range(5)] for lists in range(5)]

# Just to visualize the matrix (no necessary)
column_counter = 1
msg = "Column N°"
print(" " * len(msg) + "        " + "MATRIX")

for i in sqr_matrix:
    print(f"{msg}{column_counter}: {i}")
    column_counter += 1

matrix_diagonal = [sqr_matrix[i][i] for i in range(5)]
print(f"\nDiagonal    : {matrix_diagonal}")

diagonal_sum = sum(matrix_diagonal)
print(f"Diagonal sum: {diagonal_sum}")
"""

"""
# Exercise three:
# Count the number of occurrences of a specific value in a list.

import random

my_list = [random.randint(1, 10) for i in range(10)]
num_to_count = random.randint(1, 10)
count = my_list.count(num_to_count)

print(my_list)
if count > 1:
    print("%s appear %s times in the list" % (num_to_count, count))
else:
    print("%s appear %s time in the list" % (num_to_count, count))
"""

"""
# Replace all values in a list with the mean of the list.

my_list = [random.randint(1, 15) for i in range(random.randint(1, 6))]
print(my_list)

my_list = [sum(my_list)/len(my_list) for i in range(len(my_list))]
print(my_list)
"""

"""
my_list = [random.randint(1, 10) for i in range(5)]

max_in_list: int = 0
min_in_list = 0

for i in my_list:
    if i > max_in_list:
        max_in_list = i
        min_in_list = i

for i in my_list:
    if i < min_in_list:
        min_in_list = i

print(my_list)
print("Max value in list: %s" % max_in_list)
print("Min value in list: %s" % min_in_list)
"""

"""
# Replace all odd numbers in a list with -1.

my_list = [random.randint(0, 20) for x in range(10)]
no_odds = [-1 if i % 2 != 0 else i for i in my_list]
print(my_list)
print(no_odds)
"""

"""
# Convert a list of integers to a list of booleans where all non-zero values become True.

my_list = [random.randint(0, 20) for x in range(10)]
non_zero = [True if i != 0 else False for i in my_list]
print(my_list)
print(non_zero)

my_dict = {}
for x in my_list:
    if x != 0:
        my_dict[x] = True
    else:
        my_dict[x] = False

print(my_dict)
"""

"""
# Common items between lists:

# Solution one:
list_one = [random.randint(0, 10) for _ in range(10)]
list_two = [random.randint(0, 10) for _ in range(10)]
set_one = set(list_one)
set_two = set(list_two)
print(list_one, set_one, len(set_one))
print(list_two, set_two, len(set_two))
print(list(set_one & set_two))
print(list(set_one - set_two))  # Items in set one but not in set two
print(list(set_two - set_one))  # Items in set two but not in set one

# Solution two:
list_one = [random.randint(0, 10) for _ in range(10)]
list_two = [random.randint(0, 10) for _ in range(10)]
common_items = []
different_items = []
list_one.sort()
list_two.sort()

for _ in list_one:
    if _ in list_two and _ not in common_items:
        common_items.append(_)

    elif _ not in list_two and _ not in different_items:
        different_items.append(_)


print("List one: {}\nList two: {}".format(list_one, list_two))
print("Common_items: {}".format(common_items))
print("Different_items: {}".format(different_items))
"""

"""
# Create a code that take the larger number in a list and tells you all its repetitions index positions
# also see how many times this item is repeated
# the sum of the items repetition and the sum of all the numbers of the list without the larger number

my_list = [random.randint(0, 10) for _ in range(10)]

list_copy = my_list.copy()
max_value = max(my_list)
ind = []
control_lst = []
index_ctr = 0

while max_value in list_copy:
    for _ in list_copy:
        if _ == max_value and _ not in control_lst:
            control_lst.append(_)
            ind.append(list_copy.index(_))
            list_copy.remove(_)
            index_ctr += 1
        elif _ == max_value and _ in control_lst:
            control_lst.append(_)
            ind.append(list_copy.index(_) + index_ctr)
            list_copy.remove(_)
            index_ctr += 1


print(f"\nList: {my_list}\nLarger number: {max_value}\n"
      f"Larger number repetitions: {len(control_lst)}\n"
      f"Larger value index position: {ind}\n"
      f"Sum of all the numbers in list without larger number: {sum(list_copy)}\n"
      f"Sum of all the repetitions: {max_value * len(control_lst)}\n"
      f"Sum of all the elements in the list: {sum(my_list)}")
"""

"""
# Zip - I never used before
a = tuple(range(1, 11))
b = tuple(range(11, 21))
c = tuple(range(21, 31))
d = zip(a, b, c)
e = tuple(d)
print(a)
print(b)
print(c)
print(d)
print(e)
"""

"""
# map - Never used before either 


def add_2(my_num):
    print(f"{my_num} + 2 = {my_num + 2} ")


my_list = [x for x in range(1, 11)]
print(my_list)

a = map(add_2, my_list)
a = list(a)
"""

"""
# Convert all to negative and get square of all the negatives:

# Solution one:
my_list = list(range(1, 11))
print(my_list)

my_list = [-x for x in my_list]
print(my_list)

my_list = [x * x if x % 2 != 0 else x for x in my_list]
print(my_list)
"""

"""
# Create a 3x3 list of lists with random values and normalize it.

my_3x3_matrix = [[random.randint(1, 11) for i in range(5)] for ii in range(3)]
print(my_3x3_matrix)

normalized = my_3x3_matrix.copy()

in_index = 0
out_index = 0
max_num = 0

for i in my_3x3_matrix:
    for ii in my_3x3_matrix[out_index]:
        # print(my_3x3_matrix[out_index][in_index])
        max_num = ii if ii > max_num else max_num
        in_index += 1
    out_index += 1
    in_index = 0

out_index = 0
in_index = 0

for x in my_3x3_matrix:
    for xx in my_3x3_matrix[out_index]:
        normalized[out_index][in_index] = round((normalized[out_index][in_index]/max_num), 3)
        in_index += 1
    out_index += 1
    in_index = 0

print(normalized)
"""

"""
# Show index of all non-zero values
# Solution one:
m = [2, 1, 2, 4, 0, 0, 8, 9, 0]
ind = [m.index(i) if i != 0 else "F" for i in m]

while "F" in ind:
    for x in ind:
        if x == "F":
            ind.remove(x)
print(m)
print(ind)

# Solution two:
lst = [1, 2, 0, 0, 4, 0]
# enumerate creates a tuple with values i, x where i is the index and x is its value
understanding_enumerate = list(enumerate(lst))
print(understanding_enumerate)

non_zero_indices = [i for i, x in enumerate(lst) if x != 0]
print(non_zero_indices)
"""

"""
# Mean of individuals list in a matrix
my_list = [[random.randint(0, 10) for i in range(5)]for ii in range(3)]
mean_ind_lists = [sum(row)/len(row) for row in my_list]
print(my_list)
print(mean_ind_lists)
"""

"""
# Create a random 3x3 list of lists and replace all values greater than 0.5 with 1 and all others with 0.
my_list = [[round(random.random(), 3) for i in range(3)]for ii in range(3)]
print(my_list)

my_list = [[1 if val > 0.5 else 0 for val in row] for row in my_list]
print(my_list)
"""

"""
# Sort all the elements in a matrix:
# Solution one
my_list = [[random.randint(0, 10) for i in range(5)]for ii in range(2)]
print(my_list)

for row in my_list:
    row.sort()

print(my_list)

# Solution two:
my_list = [[random.randint(0, 10) for i in range(5)]for ii in range(2)]
sl = [sorted(row) for row in my_list]
print(sl)
"""


"""
def my_mode(numbs: list):
    # Find the mode of a list of numbers.
    my_list = numbs
    counter = 0
    mode = 0
    mode_dict = {}
    for i in my_list:
        ev = my_list.count(i)
        if ev >= counter and ev != 1:
            counter = ev
            mode_dict[i] = ev

    if len(mode_dict) == 0:
        print("all the numbers apper just one time on the list")
    else:
        print(f"Mode - repetitions:\n{mode_dict}")
"""


"""
from collections import Counter

#list_one = [random.randint(1, 10) for i in range(15)]
list_one = [1, 6, 4, 2, 4, 1, 10, 9, 5, 9, 5, 4, 1, 8, 4]
mode = Counter(list_one).most_common(5)     # [1][1]
print(list_one)
print(mode)
"""

"""
# Merge two dictionaries
# Solution one:
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict = {**dict1, **dict2}
print(merged_dict)
"""

"""
# Solution two:
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4, 'd': 10}
main_tuple = dict1, dict2   # I need to iterate inside the dicts contained in this tuple
merged_dicts = {}

for dicts_in_tuple in main_tuple:   # Iterate in the tuple
    for keys_in_dicts in dicts_in_tuple:    # Iterate in each keys of the internal dictionaries
        merged_dicts[keys_in_dicts] = dicts_in_tuple[keys_in_dicts]

print(merged_dicts)
"""

"""
# Create a dictionary from two lists.


def list_to_dict(l1: list, l2: list):
    md = {}
    l2_index = 0
    if len(l1) != len(l2):
        return "both list need to be the same length"
    else:
        for i in l1:
            md[i] = l2[l2_index]
            l2_index += 1
        return md


l_1 = [1, 2, 3, 4]
l_2 = ["a", "b", "c", "d"]
my_mixed_list = list_to_dict(l_1, l_2)
print(my_mixed_list)
"""

"""
# Invert a dictionary (swap keys and values).

# Solution one:

my_dict = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
inverted_dict = {}
for i in my_dict:
    inverted_dict[my_dict[i]] = i

print(inverted_dict)


# Solution two:
d = {'a': 1, 'b': 2, 'c': 3}
inverted_dict = {v: k for k, v in d.items()}
# .items create a list with tuples of (key, values), so we use a for loop to iterate over that and assign the
# key values to k, v
print(inverted_dict)
"""

# Create a dictionary with a default value

"""
# Solution one:
my_list = [4, 5, 6, 3, 2, 1]
my_dict = {}
default_value = "Default"

for i in my_list:
    my_dict[i] = default_value
print(my_dict)

# Solution two:
default_value = "Default"
my_list = [4, 5, 6, 3, 2, 1]
my_dict = {k: default_value for k in my_list}
print(my_dict)
"""

"""
# Convert a dictionary to a list of tuples.
my_dict = {'a': 1, 'b': 2, 'c': 3}
list_of_tuples = list(my_dict.items())
print(list_of_tuples)
"""

# Find the length of the longest string in a list.

"""
from words import words

list_of_words = []
longest_word = ""
len_words = 0

for i in range(10):
    chosen_word = random.choice(words)
    while "-" in chosen_word or " " in chosen_word:
        chosen_word = random.choice(words)
    list_of_words.append(chosen_word)

print(list_of_words)

# Solution one:

# longest_word = i if len(i) > len_words else "" for i in list_of_words
for i in list_of_words:
    print(f"Word: {i} - Length: {len(i)}")
    if len(i) > len_words:
        longest_word = i
        len_words = len(longest_word)


print(f"Longest word: {longest_word} - Length: {len_words}")


# Solution two:
max_length = max(len(x) for x in list_of_words)
print(max_length)

# Solution two:
sentence = "Hello pancho and world"
# ['world', 'and', 'pancho', 'Hello']
reversed_sentence = sentence.split()[::-1]

print(reversed_sentence)
"""

"""
from collections import Counter
my_word = "hello"
char_count = Counter(my_word)
print(char_count)
"""

"""
# Calculate the element-wise square of the difference between two lists.
lst1 = [1, 12, 3]
lst2 = [4, 5, 6]
l3 = zip(lst1, lst2)
l3l = list(l3)
print(l3l, "\n")

element_square = [(x - y) ** 2 for x, y in l3l]
squared_difference = [(x - y) ** 2 for x, y in zip(lst1, lst2)]

print(squared_difference)
print(element_square)
"""


"""
# Replace all even numbers in a list with the next odd number.

my_list = [random.randint(1, 10) for _ in range(10)]
print(my_list)

no_even = [x + 1 if x % 2 == 0 else x for x in my_list]
print(no_even)
"""


"""
# Find the median of a list of numbers.
# Solution one:
my_list = [random.randint(1, 20) for _ in range(random.randint(3, 8))]
my_list.sort()
print(my_list)

median = None
lst_len = len(my_list)

if lst_len % 2 != 0:
    lst_index = lst_len // 2
    median = my_list[lst_index]

else:
    v1 = lst_len // 2 - 1
    v2 = lst_len // 2
    median = (my_list[v1] + my_list[v2]) / 2

print(f"Median: {median}")

# Solution two:

lst_len = len(my_list)
median = (my_list[lst_len // 2] if lst_len % 2 != 0 else (my_list[lst_len // 2 - 1] + my_list[lst_len // 2]) / 2)
print(median)
"""

"""
# Find the least common multiple (LCM) of two numbers.
# Solution one:
n1 = 6     # Make it smaller than n2
n2 = 23

if n1 > n2:
    print("n1 must be smaller than n2")

else:
    n_tev1 = n1
    n_tev2 = n2
    nev1 = []
    nev2 = []
    multiplier = 1

    while n_tev1 not in nev2:
        n_tev1 = n1 * multiplier
        n_tev2 = n2 * multiplier

        # nev1.append(n_tev1)
        nev2.append(n_tev2)
        multiplier += 1

    print(f"LCM: {n_tev1}")


# Solution two:
def lcm(a, b):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    return a * b // gcd(a, b)


print(lcm(5, 4))
"""

s = "123.4"
is_valid_number = s.replace('.', '', 1).isdigit()
print(is_valid_number)
