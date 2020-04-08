# !/usr/bin/python3.8
# print("Env")

from mylib.calc import summ, minus, mul, div
# import lib

print("Summ: ", summ(1, 3, 4))
print("Minus: ", minus(1, 3, 4))
print("Mul: ", mul(1, 3, 4))
print("Div: ", div(1, 3, 4))

print("Div0: ", div(1, 1, 4, 0))
