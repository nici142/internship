# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print('Hello world!')
age = 42
first_name = 'Ahmed'
print(first_name, 'is', age, 'years old')
age = age + 3
print('Age in three years:', age)
element = 'helium'
print(element[0])
print(element[1])
element = 'sodium'
print (element[0:3])
print (len('helium'))
flabadab = 42
ewr_422_yY = 'Ahmed'
print(ewr_422_yY, 'is', flabadab, 'years old')
initial = "left"
position = initial
initial = "right"
print(position)
library_name = 'social sciences'
print('library_name[1:3] is:', library_name[1:3])
print(type(52))
title = 'Biochemistry'
print(type(title))
print(5 - 3)
full_name = 'Ahmed' + ' ' + 'Walsh'
print(full_name)
full_name = 'Ahmed' + 'Walsh'
print(full_name)
separator = '=' * 10
print(separator)
print(len(full_name))
print(1 + int('2'))
print(str(1) + '2')
first = 1
second = 5 * first
first = 2
print('first is', first, 'and second is', second)
print(type(3.4))
print(type(3.25 + 4))
num_students = 600
num_per_class = 42
num_classes = num_students // num_per_class
remainder = num_students % num_per_class
print(num_students, 'students,', num_per_class, 'per class')
print(num_classes, ' full classes, plus an extra class with only ', remainder, 'students')
print("string to float:", float("3.4"))
print("float to int:", int(3.4))
num_as_string = "3.4"
num_as_float = float(num_as_string)
num_as_int = int(num_as_float)
print(num_as_int)
int(float("3.4"))
print("I am an argument and must go here.")
print('before')
print()
print('after')
print(max(1, 2, 3))
print(min('a', 'b', 'c'))
print(min('a', 'A'))
help (round)
result = print('example')
print('result of print is', result)
import string
print('The lower ascii letters are', string.ascii_lowercase)
print(string.capwords('capitalise this sentence please.'))
from string import ascii_letters
print('The ASCII letters are', ascii_letters)
import string as s
print(s.capwords('capitalise this sentence again please.'))
import datetime
year = 2016
month = 10
day = 22
print(datetime.date(year, month, day))
import os
help (os)
import string as s
numbers = s.digits
print(numbers)
import string
numbers = string.digits
print(numbers)
from math import degrees, pi
angle = degrees (pi / 2)
print (angle)
zahlen = [1,2,3,4,5]
print(len(zahlen))
print(zahlen[3])
print('alte liste:', zahlen)
zahlen.append(6)
zahlen.append(7)
print('neue liste:', zahlen)
neue_zahlen = [8,9,10,11,12]
andere_zahlen = [55,67,89,99]
print('aktuelle zahlen:', zahlen)
zahlen.extend(neue_zahlen)
print('jetzt zahlen:',zahlen)
zahlen.append(andere_zahlen)
print('ergebnis:',zahlen)
neue_liste = [10,11,12,13,14,15]
print('bevor zerstörung',neue_liste)
del neue_liste[0]
print('nach zerstörung',neue_liste)
element = 'carbon'
print('zero:',element[0])
print('third:',element[3])
values = []
values.append(1)
values.append(3)
values.append(5)
print('first time:',values)
values = [3,5]
print('second time:',values)
print('string to list:', list('tin'))
print('list to string:', ''.join(['g', 'o', 'l', 'd']))
element = 'helium'
print(element[-1])
print(values[0:-1])
element = 'fluorine'
print(element[::2])
print(element[::-1])
element = 'lithium'
print(element[0:20])
print(element[-1:3])
letters = list('gold')
result = sorted(letters)
print('letters is', letters, 'and result is', result)
letters = list('gold')
result = letters.sort()
print('letters is', letters, 'and result is', result)
old = list('gold')
new = old      # simple assignment
new[0] = 'D'
print('new is', new, 'and old is', old)
old = list('gold')
new = old[:]   # assigning a slice
new[0] = 'D'
print('new is', new, 'and old is', old)
for number in [2,3,5]:
    print(number)
primes = [2, 3, 5]
for p in primes:
    squared = p ** 2
    cubed = p ** 3
    print(p, squared, cubed)
print('a range is not a list: range(0, 3)')
for number in range(0,3):
    print(number)
for number in range(5):
    print("Again!")
print(list(range(10)))
