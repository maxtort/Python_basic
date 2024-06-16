                                # Сменить позицию в списке
#
# changable_list = [12, 3, 4, 10]
# changable_list = [1]
# changable_list = []
# changable_list = [12, 3, 4, 10, 8]

# changable_list_lenth = len(changable_list)
#
# if not changable_list:
#     print(changable_list)
# elif changable_list_lenth != 0:
#     variable_pop = changable_list.pop()
#     changable_list.insert(0, variable_pop)
#     print(changable_list)
# else:
#     print('Mistake')


#                                 Разделить список

# devided_list = [1, 2, 3, 4, 5, 6]
# devided_list = [1, 2, 3]
# devided_list = [1, 2, 3, 4, 5]
# devided_list = [1]
# devided_list = []
#
#
# devided_list_lenth = len(devided_list)
# if devided_list_lenth % 2 == 0:
#     print([devided_list[:devided_list_lenth//2], devided_list[devided_list_lenth//2:]])
# elif devided_list_lenth % 2 != 0:
#     print([devided_list[:devided_list_lenth//2+1], devided_list[devided_list_lenth//2+1:]])
# else:
#     print('Try again')


#                                   Калькулятор


# user_number_first = float(input('Введите первое число:'))
# user_operation = input('Введите действие:')
# user_number_second = float(input('Введите второе число:'))
#
# if user_operation == '+':
#     print(user_number_first + user_number_second)
# elif user_operation == '-':
#     print(user_number_first - user_number_second)
# elif user_operation == '*':
#     print(user_number_first * user_number_second)
# elif user_operation == '/':
#     if user_number_second == 0:
#         another_number = float(input('Делить на 0 нельзя, введите другое число:'))
#         print(user_number_first / another_number)
#     else:
#         print(user_number_first / user_number_second)
# else:
#     print('Wrong value')
#
#
