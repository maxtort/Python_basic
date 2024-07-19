# # # # # # # # # # # # # # # # Генератор простых чисел
# def simple_num(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
#
# def prime_generator(end):
#     i = 2
#     while i <= end:
#         if simple_num(i):
#             yield i
#         i += 1
#
# from inspect import isgenerator
#
# gen = prime_generator(1)
# assert isgenerator(gen) == True, 'Test0'
# assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
# assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
# assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
# print('Ok')


# # # # # # # # # # # # # # # # Добавление кубов в список
# def generate_cube_numbers(end):
#
#     for n in range(2, end + 1):
#         val_cube = n ** 3
#         if val_cube >= end + 1:
#             break
#         yield val_cube
#
# from inspect import isgenerator
#
# gen = generate_cube_numbers(1)
# assert isgenerator(gen) == True, 'Test0'
# assert list(generate_cube_numbers(10)) == [8]
# assert list(generate_cube_numbers(100)) == [8, 27, 64]
# assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000], '10 у кубі це 1000'
# print('Ok')

# # # # # # # # # # # # # # # # Найти парность

# couple = ('0', '2', '4', '6', '8')
# def is_even(number):
#     number = tuple(''.join(map(str, str(number))))
#     if number[-1] in couple:
#         return True
#     elif number[-1] not in couple:
#         return False
#
# assert is_even(2494563894038**2) == True, 'Test1'
# assert is_even(1056897**2) == False, 'Test2'
# assert is_even(24945638940387**3) == False, 'Test3'
# print('Ok')