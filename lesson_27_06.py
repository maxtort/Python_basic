 #  #  #  #  #  #  #  #  #  # Приветсвтие
# def say_hi(name, age):
#
#     return "Hi. My name is {} and I'm {} years old".format(name,age)
#
#
# assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
# assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
# print('ОК')


 #  #  #  #  #  #  #  #  #  # Модифицировать строку

# def correct_sentence(text):
#     result = list(text)
#     result[0] = result[0].upper()
#
#     for s in result:
#         if result[-1] != '.':
#             result.append('.')
#     text = ''.join(result)
#
#     return text
#
# assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
# assert correct_sentence("hello") == "Hello.", 'Test2'
# assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
# assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
# assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
# print('ОК')



#  #  #  #  #  #  #  #  #  # Поиск подстроки

# def second_index(text, some_str):
#
#      sym_index = text.rfind(some_str)
#      if sym_index == 0:
#          sym_index = None
#
#      return sym_index


# assert second_index("sims", "s") == 3, 'Test1'
# assert second_index("find the river", "e") == 12, 'Test2'
# assert second_index("hi", "h") is None, 'Test3'
# assert second_index("Hello, hello", "lo") == 10, 'Test4'
# print('ОК')


#  #  #  #  #  #  #  #  #  # Уникальный элемент


def common_elements():
    general_range = 100
    x = list(range(0, general_range + 1))
    new_general_range = 100
    new_x = list(range(0, general_range + 1))

    set_dev_3 = set()
    set_dev_5 = set()

    for num in x:
        if num % 3 == 0:
            set_dev_3.add(num)
    for numb in new_x:
        if numb % 5 == 0:
            set_dev_5.add(numb)

    union_set = set_dev_3.intersection(set_dev_5)

    print(union_set)
    return union_set

common_elements()
assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
