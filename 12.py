# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3

# sum_of_numbers = int((input('Введите сумму искомых чисел: ')))
# composition_of_numbers = int((input('Введите произведение искомых чисел: ')))
# for i in range(1,sum_of_numbers + 1):
#     if i*(sum_of_numbers - i) == composition_of_numbers:
#         print(f'{i} {sum_of_numbers - i}')
#         break


sum_of_numbers = int((input('Введите сумму искомых чисел: ')))
composition_of_numbers = int((input('Введите произведение искомых чисел: ')))
num1 = int((sum_of_numbers - (sum_of_numbers * sum_of_numbers - 4 * composition_of_numbers) ** 0.5) / 2)
num2 = int((sum_of_numbers + (sum_of_numbers * sum_of_numbers - 4 * composition_of_numbers) ** 0.5) / 2)
print(num1)
print(num2)