############################## Удалить теги с файла
# import codecs
#
#
# def delete_html_tags(html_file, result_file='cleaned.txt'):
#
#     with codecs.open(html_file, 'r', 'utf-8') as file:
#         html = file.read()
#         tag_in = False
#         only_text = ''
#         for char in html:
#             if char == '<':
#                 tag_in = True
#             elif char == '>':
#                 tag_in = False
#             elif not tag_in:
#                 only_text += char
#         lines = only_text.split()
#         cleaned_text = '\n'.join(lines)
#
#     with codecs.open(result_file, 'w', 'utf-8') as result:
#         result.write(cleaned_text)
#
#
# html_draft = 'draft.html'
# final_result_file = 'cleaned.txt'
# delete_html_tags(html_draft, final_result_file)


# # # # # # # # # # # # # # # # # Корзина покупок

# class Item:
#
#     def __init__(self, name, price, description, dimensions):
#         self.price = price
#         self.description = description
#         self.dimensions = dimensions
#         self.name = name
#
#     def __str__(self):
#         return f"{self.name}, price:{self.price}"
#
#
# lemon = Item('lemon', 5, "yellow", "small", )
# apple = Item('apple', 2, "red", "middle", )
# # print(lemon)  # lemon, price: 5
#
#
# class User:
#
#     def __init__(self, name, surname, numberphone):
#         self.name = name
#         self.surname = surname
#         self.numberphone = numberphone
#
#     def __str__(self):
#         return f"{self.name} {self.surname}"


# buyer = User("Ivan", "Ivanov", "02628162")
# buyer_1 = User("Andrey", "Petrov", "0123456789")
# print(buyer)  # Ivan Ivanov
# print(buyer_1)


# class Purchase:

#     def __init__(self, user):
#         self.products = {}
#         self.user = user
#         self.total = 0
#
#     def add_item(self, item, cnt):
#         self.products[item] = cnt
#
#     def __str__(self):
#         tmp = ''
#         for item, cnt in self.products.items():
#             tmp += f'{item.name}: {cnt} pcs. \n'
#         return f'User: {self.user}\nItems:\n{tmp}'
#
#     def get_total(self):
#         total = 0
#         for key, cnt in self.products.items():
#             total += key.price * cnt
#         return total
#
#
# cart = Purchase(buyer)
# cart_1 = Purchase(buyer_1)
# cart.add_item(lemon, 4)
# cart.add_item(apple, 20)
# cart_1.add_item(lemon, 3)
# cart_1.add_item(apple, 15)
# print(cart)
# print(cart_1)
# """
# User: Ivan Ivanov
# Items:
# lemon: 4 pcs.
# apple: 20 pcs.
# """
# assert isinstance(cart.user, User) is True, 'Екземпляр класу User'
# assert cart.get_total() == 60, "Всього 60"
# assert cart.get_total() == 60, 'Повинно залишатися 60!'
# cart.add_item(apple, 10)
# print(cart)
# """
# User: Ivan Ivanov
# Items:
# lemon: 4 pcs.
# apple: 10 pcs.
# """
# assert cart.get_total() == 40

