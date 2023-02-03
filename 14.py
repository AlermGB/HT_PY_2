# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8

degree = 0
powered = 1
number = int(input('Введите число N: '))
while powered <= number:
    print(powered)
    powered *= 2
