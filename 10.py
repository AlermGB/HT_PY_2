# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

count = 0
coin_side = ''

n = int(input('Введите количество монеток: '))
counter = n
print('Последовательно вводите состояние монетки "0" или "1": ')
while counter > 0:
    coin_side = input()
    if coin_side == '0' or coin_side == '1':
        if coin_side == '1':
            count +=1
        counter -=1
    else:
        print('НЕВЕРНЫЙ ВВОД!!!')
print('Требуется переворотов: ')
if count < n - count:
    print(count)
else:
    print(n - count)