import string
# # # # # # # # # # # # # # # # # # # Парные числа
# def is_even(digit):
#     """ Перевірка чи є парним число """
#     div, mod = divmod(digit, 2)
#     if mod == 0:
#         return True
#     elif mod != 0:
#         return False
#
#
# assert is_even(2) == True, 'Test1'
# assert is_even(5) == False, 'Test2'
# assert is_even(0) == True, 'Test3'
# print('OK')

# # # # # # # # # # # # # # # # # # # Найти первое слово
# def first_word(text):
#     """ Пошук першого слова """
#     after_strip = text.strip(string.punctuation)
#     new_text = after_strip.replace(',', ' ').replace('.', ' ').split()
#     find_word = new_text.pop(0)
#
#     return find_word
#
# assert first_word("Hello world") == "Hello", 'Test1'
# assert first_word("greetings, friends") == "greetings", 'Test2'
# assert first_word("don't touch it") == "don't", 'Test3'
# assert first_word(".., and so on ...") == "and", 'Test4'
# assert first_word("hi") == "hi", 'Test5'
# assert first_word("Hello.World") == "Hello", 'Test6'
# print('OK')


# # # # # # # # # # # # # # # # # # Генераторная функция

def pow(x):
    return x ** 2

def some_gen(begin, end, func):
    """
     begin: перший елемент послідовності
     end: кількість елементів у послідовності
     func: функція, яка формує значення для послідовності
    """

    yield begin


    for num in range(1, end):
        begin = func(begin)
        yield begin


from inspect import isgenerator

gen = some_gen(2, 4, pow)

assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')
