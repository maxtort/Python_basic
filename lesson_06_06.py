user_input = input('Ведитие число:')
first_number = int(user_input) // 1000
y = int(user_input) % 1000
second_number = y // 100
x = int(user_input) % 100
third_number = x // 10
fourth_number = int(user_input) % 10

print(first_number)
print(second_number)
print(third_number)
print(fourth_number)


user_input_second = input('Введите число:')
number_1 = int(user_input_second) // 10000
a = int(user_input_second) % 10000
number_2 = a // 1000
b = int(user_input_second) % 1000
number_3 = b // 100
c = int(user_input_second) % 100
number_4 = c // 10
d = int(user_input_second) % 10
number_5 = d // 1
print(number_5,number_4, number_3, number_2, number_1, sep='')

