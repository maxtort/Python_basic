############################# Класс учеников с исключением
class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.gender}, {self.age} years old)\n"


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        self.record_book = record_book
        super().__init__(gender, age, first_name, last_name)

    def __str__(self):
        resp = super().__str__()
        return f"Student {self.record_book}: " + resp


class Group:

    def __init__(self, number, max_students):
        self.number = number
        self.max_students = max_students
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= self.max_students:
            raise ValueError('Достигнут максимум студентов')
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)

        if student is not None:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = ''
        for student in self.group:
            all_students += str(student)

        return f'Number:{self.number}\n{all_students}'


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Male', 31, 'Michael', 'Jacson', 'AN143')
st4 = Student('Female', 26, 'Marilyn', 'Monroe', 'AN144')
st5 = Student('Male', 30, 'Joy', 'Triv', 'AN142')
st6 = Student('Male', 30, 'Karl', 'Ovo', 'AN142')
st7 = Student('Male', 30, 'Frodo', 'Beggins', 'AN142')
st8 = Student('Male', 30, 'Gendalf', 'Gray', 'AN142')
st9 = Student('Male', 30, 'Nick', 'Bushemy', 'AN142')
st10 = Student('Male', 30, 'Jon', 'Travolta', 'AN142')
st11 = Student('Female', 25, 'Liza', 'Kudrow', 'AN145')


gr = Group('PD1', 10)


for student in [st1, st2, st3, st4, st5, st6, st7, st8, st9, st10]:
    gr.add_student(student)
try:
    gr.add_student(st11)
except ValueError as e:
    print(f'Ошибка: {e}')


# print(gr)

assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод пошуку має повертати екземпляр'

gr.delete_student('Taylor')

# print(gr)


gr.delete_student('Taylor')


