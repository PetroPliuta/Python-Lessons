#!/usr/bin/python3.8
import random

# 1. Написати функцію,
# яка отримує в якості параметрів
# два цілих числа і повертає суму
# чисел з діапазону між ними.


# def sum(start, stop):
#     res = 0
#     if start > stop:
#         start, stop = stop, start
#     for i in range(start+1, stop):
#         res += i
#     return res


# res = sum(4, 1)
# print(res)

# 2. Написати функцію, яка отримує відстань,
# яку пробіг спортсмен та час пробігу
# і повертає швидкість спортсмена.
# Відстань та час пробігу вводяться користувачем

# def v(l, t):
#     return l/t


# l = float(input("Enter length: "))
# t = float(input("Enter time: "))

# res = v(l, t)
# print("Speed is", res)

# 3. Дано список 10 елементів .
# Замінити всі від’ємні елементи додатніми.
# Діапазон - 20 +30
# a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# for i in range(len(a)):
#     a[i] = random.randint(-20, 30)
# print(a)
# for i in range(len(a)):
#     if a[i] < 0:
#         a[i] = -a[i]
# print(a)

# car = ("BMW", "Renault", "VW", "Audi")
# print(car)
# # for i in car:
# #     print(i)
# print(car[0])
# print(car[-1])
# print(len(car))
# print(car.count("BMW ".strip()))

# person = ("Bill", 34)

# name, age = person
# print("Name:", name,"\nAge:",age)

countries = {
    1: "Ukraine",
    2: "USA",
    "3": "Brasil",
}
print(countries)

for key, value in countries.items():
    print("key:", key, " value:", value)

# countries.pop(1)
# print(countries)
print(countries[1])
countries["IT"] = 123
print(countries)
# for key in countries.keys():
#     print("key:", key)
# for val in countries.values():
#     print("val:", val)

#pip3 install requests
#api.covid19api.com/summary
#
# Зробити Sort
# вивід в консоль
