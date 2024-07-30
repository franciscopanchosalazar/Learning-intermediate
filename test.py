
"""
# String slicing
phrase = 'panchohernansalazarbravo'
print(len(phrase))
w1 = phrase[0:6]
w2 = phrase[6:12]
w3 = phrase[12:19]
w4 = phrase[19:24]
print(w1)
print(w2)
print(w3)
print(w4)

second_phrase = 'unamujersehaperdidoconocereldelirioyelpolvosehaperdidoestabellalocura'
print(len(second_phrase))
w1 = second_phrase[:3]
w2 = second_phrase[3:8]
w3 = second_phrase[8:10]
w4 = second_phrase[10:12]
w5 = second_phrase[12:19]
w6 = second_phrase[19:26]
w7 = second_phrase[26:28]
w8 = second_phrase[28:35]
w9 = second_phrase[35:]

print(f'{w1} {w2} {w3} {w4} {w5} {w6} {w7} {w8} {w9}')
"""

"""
# Practicing classes
class MyObject:
    def __init__(self, name: str, litres, quantity, price):
        self.name = name.capitalize()
        self.litres = litres
        self.quantity = quantity
        self.price = price
        self.total_price = 0
        print(self.name)

    def product_total_price(self):
        self.total_price = self.quantity * self.price
        return self.total_price


coke = MyObject('coke', 4, 300, 2).product_total_price()
print(coke)
"""

"""
# Trying to iterate inside a class
name = input('Name: ')
middle_name = input('Middle name: ')
surname = input('Surname: ')
second_surname = input('Second surname: ')


class Info:
    def __init__(self, nam, mid, sur, sec_sur):
        self.my_str = ''
        self.my_list = [nam, mid, sur, sec_sur]

        print(self.my_list)
        for i in self.my_list:
            self.my_str += i + ' '

        print(self.my_str)


u_1 = Info(name, middle_name, surname, second_surname)
"""
"""
lst = [2, 5, 8, 10, 12, 7, 13, 15]
count_within_range = sum(5 <= x <= 12 for x in lst)
print(count_within_range)

lst_2 = [3, 4, 5, 6, 11, 12]
counting_all = sum(lst_2)
over_10 = sum(x > 10 for x in lst_2)

print(counting_all)
print(over_10)

"""

"""
# Cool way to create a list:
a = [random.randint(1, 10) for i in range(3)]   # -----> output [x, x, x] where x are random values from 1 to 10
print(a)

# 2D List:
d2 = [[2 for x in range(3)] for z in range(2)]  # -----> output [[2, 2, 2], [2, 2, 2]]
print(d2)

d22 = [["x" for _ in range(4)] for _ in range(3)]
print(d22)  # -----> output [['x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x']]

# Iterating in the d2 list, in one line and as usual
# Short version
a = [sum(lst) for lst in d2]
print(a)

# Long version
y = []
for i in d2:
    y.append(sum(i))

print(y)
"""



