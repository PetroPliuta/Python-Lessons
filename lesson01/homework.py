#!/usr/bin/python3.8
import random

# 1. Написати програму
# яка в залежності від введеної години виводить:
# good night, good day, good evening, good morning

# try:
#     hour = int(input("Enter hour (0-24): "))
# except ValueError:
#     print('This is not int. Exit.')
# else:
#     if 0 <= hour <= 6:
#         print("good night")
#     elif 6 < hour <= 12:
#         print("good morning")
#     elif 12 < hour <= 18:
#         print("good day")
#     elif 18 < hour <= 24:
#         print("good evening")
#     else:
#         print("Error. Wrong hour.")


# 2. Відомо, що 1 дюйм дорівнює 2.54 см.
# Розробити програму, що переводить дюйми в сантиметри и навпаки.
# Діалог с користувачем реалізувати через систему меню.

# INCH = 2.54
# while True:
#     choice = input("\n\n1. inch->cm\n2. cm->inch\n0. Exit\n==> ")
#     if choice == "0":
#         break
#     elif choice == "1" or choice == "2":
#         while True:
#             try:
#                 x = float(input("Enter value: "))
#             except ValueError:
#                 print("Not a number")
#                 continue
#             else:
#                 break
#         if choice == "1":
#             print(x, "inch =", x*INCH, "cm")
#         else:
#             print(x, "cm =", x/INCH, "inch")
#     else:
#         print("Wrong choice")


# 3. Розробити програму, що переводить значення температури
# в градусах по Цельсію в температуру по Фаренгейту та навпаки.
# Співвідношення між температурами визначається формулою:
# TF = TC *1.8 +32.
# Діалог с користувачем реалізувати через систему меню.

# while True:
#     choice = input("\n\n1. F->C\n2. C->F\n0. Exit\n==> ")
#     if choice == "0":
#         break
#     elif choice == "1" or choice == "2":
#         while True:
#             try:
#                 x = float(input("Enter temperature in " +
#                                 ("celsius" if choice == "2" else "farenheit") + ": "))
#             except ValueError:
#                 print("Not a number")
#                 continue
#             else:
#                 break
#         if choice == "1":
#             print("\n", x, "F =", (x-32) / 1.8, "C")
#         else:
#             print("\n", x, "C =", x*1.8 + 32, "F")
#     else:
#         print("Wrong choice")


# 4. Вводяться 8 чисел.
# Знайти добуток та середнє арифметичне цих чисел.

# mul = 1
# sum = 0
# numbers = []
# for i in range(8):
#     x = random.randint(-10,10)
#     # x = float(input("Enter "+ str(i+1)+ " value: "))
#     numbers.append(x)
#     mul *= x
#     sum += x
# print("numbers: ", numbers)
# print("sum: ", sum, "\nmul: ", mul)


# 5. Протягом тижня вимірювали температуру повітря.
# Знайти максимальну та мінмальну температуру.

# for i in range(7):
#     x = random.randint(-40, 50)
#     print(x)
#     if i == 0:
#         max_ = min_ = x
#     else:
#         if x < min_:
#             min_ = x
#         if x > max_:
#             max_ = x
# print("min:", min_)
# print("max:", max_)
