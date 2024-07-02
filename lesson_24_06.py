import string
import keyword
# # # # # # # # # # # # # Имя переменной # # # # # # # # # # # #

# user_input = input('Enter definition:').lower()
# result = user_input.isidentifier()
#
# if user_input in keyword.kwlist:
#     result = False
# if user_input.count('_') == len(user_input) > 1:
#     result = False
# for symbol in user_input:
#     if not result:
#         break
#     if symbol == '_':
#         result = True
#         continue
#     elif symbol in string.punctuation:
#         result = False
#         break
#
# print(result)
#

# # # # # # # # # # # # # # Диапазон букв # # # # # # # # # # # #

# letters = "a-c"
# letters = "a-a"
# letters = "s-H"
# letters = "a-A"
#
# alphabet = string.ascii_letters
# a, b = letters[0], letters[-1]
# a = alphabet.find(a)
# b = alphabet.find(b)
#
# print(alphabet[a:b+1])


# # # # # # # # # # # # # # # # Добуток чисел # # # # # #

# user_input = int(input('Введите целое число:'))
# result = 1
# while user_input > 9:
#     for num in str(user_input):
#         result *= int(num)
#     user_input = result
#     result = 1
#
# print(user_input)


# # # # # # # # # # # # # # # # Конвертор из числа в дату

all_time = int(input('Введите число от 0 до 8640000:'))

if 0 <= all_time <= 8640000:
    days, balance = divmod(all_time, 86400)
    hours, balance = divmod(balance, 3600)
    minutes, seconds = divmod(balance, 60)

    if days % 10 == 1 and days != 11:
        day_definition = 'день'
    elif 2 <= days % 10 <= 4 and (days % 100 <10 or days % 100 >=20):
        day_definition = 'дня'
    else:
        day_definition = 'дней'

    print(f'{days} {day_definition}, {hours}:{minutes}:{seconds}')
else:
    print('Вы ввели неверное число')

