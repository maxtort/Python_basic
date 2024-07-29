# # # # # # # # # # # # # # # # # # # # Группа учеников
#
# class Human:
#
#     def __init__(self, gender, age, first_name, last_name):
#         self.gender = gender
#         self.age = age
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def __str__(self):
#         return f"Пол: {self.gender}, Возраст: {self.age}, Имя/фамилия: {self.first_name} {self.last_name}"
#
#
# class Student(Human):
#
#     def __init__(self, gender, age, first_name, last_name, record_book):
#         super().__init__(gender, age, first_name, last_name)
#         self.record_book = record_book
#
#     def __str__(self):
#         return super().__str__() + f", Запись: {self.record_book}"
#
#
# class Group:
#
#     def __init__(self, number):
#         self.number = number
#         self.group = set()
#
#     def add_student(self, student):
#         if isinstance(student, Student):
#             self.group.add(student)
#
#     def delete_student(self, last_name):
#         student = self.find_student(last_name)
#         if student:
#             self.group.remove(student)
#
#     def find_student(self, last_name):
#         for student in self.group:
#             if student.last_name == last_name:
#                 return student
#         return None
#
#     def __str__(self):
#         all_students = ''
#         for student in self.group:
#             all_students += str(student) + '\n'
#         return f'Number:{self.number}\n{all_students}'
#
#
# st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
# st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
#
# # print(st1)
# # print(st2)
# gr = Group('PD1')
# gr.add_student(st1)
# gr.add_student(st2)
#
# print(gr)
# assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
# assert gr.find_student('Jobs2') is None, 'Test2'
# assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'
# #
# gr.delete_student('Taylor')
# print(gr)
# #
# gr.delete_student('Taylor')



# # # # # # # # # # # # # # # # # # # # Цифровой счетчик
# class Counter:
#
#     def __init__(self, current=1, min_value=0, max_value=10):
#         self.current = current
#         self.min_value = min_value
#         self.max_value = max_value
#
#         if self.current < self.min_value:
#             self.current = self.min_value
#         elif self.current > self.max_value:
#             self.current = self.max_value
#         else:
#             self.current = current
#
#     def set_current(self, start):
#         if start > self.max_value:
#             self.current = self.max_value
#         elif start < self.min_value:
#             self.current = self.min_value
#         else:
#             self.current = start
#
#     def set_max(self, max_max):
#         if max_max < self.min_value:
#             raise ValueError('Новое максимальное значение не может быть меньше минимального значения')
#         self.max_value = max_max
#
#         if self.current > self.max_value:
#             self.current = self.max_value
#
#     def set_min(self, min_min):
#         if min_min > self.max_value:
#             raise ValueError('Новое минимальное значение не может быть больше максимального значения')
#         self.min_value = min_min
#
#         if self.current < self.min_value:
#             self.current = self.min_value
#
#     def step_up(self):
#         if self.current >= self.max_value:
#             raise ValueError('Достигнут максимум')
#         self.current += 1
#
#     def step_down(self):
#         if self.current <= self.min_value:
#             raise ValueError('Достигнут минимум')
#         self.current -= 1
#
#     def get_current(self):
#         return self.current
#
#
# counter = Counter()
# counter.set_current(7)
# counter.step_up()
# counter.step_up()
# counter.step_up()
# assert counter.get_current() == 10, 'Test1'
# try:
#     counter.step_up()
# except ValueError as e:
#     print(e)
# assert counter.get_current() == 10, 'Test2'
#
# counter.set_min(7)
# counter.step_down()
# counter.step_down()
# counter.step_down()
# assert counter.get_current() == 7, 'Test3'
# try:
#     counter.step_down()
# except ValueError as e:
#     print(e)
# assert counter.get_current() == 7, 'Test4'
