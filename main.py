"""Программа для вычисления квадратного уравнения"""
print("Введите значение a:")
a = int(input())
print("Введите значение b:")
b = int(input())
print("Введите значение c:")
c = int(input())
d = b**2 - 4 * a * c
if d > 0:
    print("Дискримминант имеет два корня")
    x1 = (-b + d**0.5) / 2*a
