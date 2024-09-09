# Задача 1. Нахождение наибольшего общего делителя (НОД) двух чисел
#
# Программа принимает два целых числа и находит их наибольший общий
# делитель (НОД).
# Алгоритм Евклида основан на принципе, что наибольший общий делитель двух чисел не изменяется, если большее число заменить его разностью с меньшим числом.
#
# a = int(input('Введите первое число:'))
# b = int(input('Введите второе число:'))
#
# while a != 0 and b != 0:
#
#     if a > b:
#
#         a = a % b
#     else:
#
#         b = b % a
#
# gcd = a + b
# print(gcd)
#

# Задание 2. Преобразование числа в шестнадцатеричное представление
# Напишите программу, которая получает целое число и возвращает его
# шестнадцатеричное строковое представление. Функцию hex используйте для
# проверки своего результата.

numbers = (20, 10, 16, 34, -5)
hex_digits = '0123456789ABCDEF'

for  number  in numbers:
    if number == 0:
        hex_string = '0'
    else:
        is_negative = number < 0
        if is_negative:
            number = -number

    hex_string = ''
    while number > 0:
        remainder = number % 16
    hex_string = hex_digits[remainder] + hex_string
    number //= 16

    if is_negative:
        hex_string = '-' + hex_string
    print(hex_string)
    






