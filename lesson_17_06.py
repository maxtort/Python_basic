# # # # # # # # # # # # # # Переместить нули вконец списка # # # # # #

# value_list = [0, 1, 0, 12, 3]
# value_list = [0]
# value_list = [1, 0, 13, 0, 0, 0, 5]
# value_list = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
# #
# value_list.sort(reverse=True, key=bool)
# print(value_list)



# # # # # # # # # # # # # # # # Найти сумму элементов с парными индексами # # # #

# user_list = [0, 1, 7, 2, 4, 8]
# user_list = [1, 3, 5]
# user_list = [6]
# user_list = []
#
# result = 0
# summ = 0
#
# for index_user_list, value_user_list in enumerate(user_list):
#         if index_user_list % 2 == 0:
#             summ += value_user_list
#             result = summ * user_list[-1]
#
# print(result)





##############################    Список из 3 элементов

# base_list = [1, 2, 3, 4, 5, 6, 7, 9]
# base_list = [1, 1, 2, 1]
# base_list = [6, 3, 7]
#
# copy_base_list_1 = base_list.copy()
# copy_base_list_2 = base_list.copy()
# copy_base_list_3 = base_list.copy()
# value_new_list_1 = copy_base_list_1.pop(0)
# value_new_list_2 = copy_base_list_2.pop(2)
# value_new_list_3 = copy_base_list_3.pop(-2)
# my_new_list = [value_new_list_1, value_new_list_2, value_new_list_3]
#
# print(my_new_list)