# #!/usr/bin/python3.8
import random

# 1
# a = int(input('Enter km: '))
# print(a, "km = ", a*1000, "m")

# # 2
# USD = 25.5
# EUR = 30.0
# RUB = .3
# s = float(input("Enter sum (UAH): "))
# print("EUR = ", s/EUR)
# print("USD = ", s/USD)
# print("RUB = ", s/RUB)

# 3
# price = float(input("Enter price: "))
# fuel_consumption = float(input("Enter fuel consumption: "))
# length = float(input("Enter path length: "))
# res = length/100 * fuel_consumption * price
# print('Result = ', res)

# 4
# a = random.randrange(0, 2)
# b = random.randrange(0, 2)
# c = random.randrange(0, 2)
# print(a,b,c)
# if a == b and b == c:
#     print('All equal')

# # 5
# exit = False
# while not exit:
#     choice = int(input("1. Add\n2. Div\n0. Exit\n==>"))
#     if choice == 1:
#         print("a+b")
#         print("sum: ", float(input("Enter a: "))+float(input("Enter b: ")))
#     elif choice == 2:
#         print("a/b")
#         print("div: ", float(input("Enter a: "))/float(input("Enter b: ")))
#     elif choice == 0:
#         exit = True

# 6
# -10 .. + 30
counter = 0
for number in range(7):
    t = random.randrange(-10, 30)
    print("T: ", t)
    if t > 10:
        counter += 1
print("Count = ", counter)
