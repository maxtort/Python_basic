# # # # # # # # # # # # # # # # # # # # Добавить 1 к числу

# def add_one(some_list):
#
#     value_string = int(''.join(map(str, some_list)))
#     addition = value_string +1
#     final_list = list(map(int, str(addition)))
#
#     return final_list
#
#
# assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
# assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
# assert add_one([0]) == [1], 'Test3'
# assert add_one([9]) == [1, 0], 'Test4'
# print("ОК")


# # # # # # # # # # # # # # # # # # # # Найти уникальное число

# def find_unique_value(some_list):
#
#     for n in some_list:
#         if some_list.count(n) == 1:
#             return n
#     return n
#
# assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
# assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
# assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
# print("ОК")


# # # # # # # # # # # # # # # # # # # Палиандром
import string
def is_palindrome(text):
    result = ''
    text = text.lower()
    for symb in text:
        if symb.isdigit():
            return False
        elif symb not in string.punctuation:
            result += symb
    text_split = result.split()
    join_text = ''.join(text_split)
    if join_text == join_text[::-1]:
        return True
    elif join_text != join_text[::-1]:
        return False

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
