# # # # # # # # # # # # # # # # # Популярные слова
# def popular_words(text, words):
#     new_text = list(text.lower().split())
#     new_dict = {}
#     new_dict_1 = {}
#
#     for word in new_text:
#         new_dict[word] = new_text.count(word)
#         for uniq_word in words:
#             new_dict_1[uniq_word] = new_text.count(uniq_word)
#
#     return new_dict_1
#
#
# assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'
# print('OK')


# # # # # # # # # # # # # # # # # Найти разницу

def difference(*args):
    result = 0
    if not args:
      return result

    result = max(args)-min(args)
    if result != int:
        result = round(result, 2)

    return result

assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')

