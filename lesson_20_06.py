# # # # # ## # # # # # # # # # # #  Hashtag
#
# import string
#
# us_input = input('Enter your hashtag:').title()
#
# result = ''
#
# for symb in us_input:
#     if not  symb in string.punctuation:
#         result += symb
#
# new = result.split()
# user_hashtag = ''.join(new)
#
# print('#', user_hashtag[:140], sep='')
#




                                    # Калькулятор 2.0

# while True:
#     user_number_first = float(input('Введите первое число:'))
#     user_operation = input('Введите действие:')
#     user_number_second = float(input('Введите второе число:'))
#
#     result = 0
#
#     if user_operation not in ('+', '-', '*', '/'):
#         result = 'Wrong value'
#     if user_operation == '+':
#         result = (user_number_first + user_number_second)
#     elif user_operation == '-':
#         result = (user_number_first - user_number_second)
#     elif user_operation == '*':
#         result = (user_number_first * user_number_second)
#     elif user_operation == '/' and user_number_second == 0:
#         result = 'Делить на 0 нельзя'
#     elif user_operation == '/' and user_number_second != 0:
#         result = (user_number_first / user_number_second)
#
#     print(result)
#
#     client_decision = input("Enter Y or Yes for continue or another symbol for break:")
#     client_result = client_decision.lower()
#
#     if client_result == 'y' or client_result == 'yes':
#         continue
#     else:
#         break
















