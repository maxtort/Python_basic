# # # # # # # # # # # # # # # # # # # Класс Прямоугольник

# class Rectangle:
#
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def get_square(self):
#         return self.width * self.height
#
#     def __eq__(self, other):
#         if isinstance(other, Rectangle):
#             return self.get_square() == other.get_square()
#         return NotImplemented
#
#     def __add__(self, other):
#         if isinstance(other, Rectangle):
#             total_square = self.get_square() + other.get_square()
#             return Rectangle(1, total_square)
#         return NotImplemented
#
#     def __mul__(self, n):
#         if isinstance(n, (int, float)):
#             total_square = self.get_square() * n
#             return Rectangle(1, total_square)
#         return NotImplemented
#
#     def __str__(self):
#         return "Rectangle [width = {}, height = {}]".format(self.width, self.height)
#
#
# r1 = Rectangle(2, 4)
# r2 = Rectangle(3, 6)
#
# assert r1.get_square() == 8, 'Test1'
# assert r2.get_square() == 18, 'Test2'
#
# r3 = r1 + r2
# assert r3.get_square() == 26, 'Test3'
#
# r4 = r1 * 4
#
# assert r4.get_square() == 32, 'Test4'
#
# assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'


# # # # # # # # # # # # # # # # # # # Правильные дроби


class Fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __mul__(self, other):
        if isinstance(other, Fraction):
            numerator = self.a * other.a
            denominator = self.b * other.b
            return Fraction(numerator, denominator)
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Fraction):
            numerator = self.a * other.b + self.b * other.a
            denominator = self.b * other.b
            return Fraction(numerator, denominator)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Fraction):
            numerator = self.a * other.b - self.b * other.a
            denominator = self.b * other.b
            return Fraction(numerator, denominator)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Fraction):
            res = self.a / self.b == other.a / other.b
            return res
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Fraction):
            res = self.a * other.b > self.b * other.a
            return res
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Fraction):
            res = self.a * other.b < self.b * other.a
            return res
        return NotImplemented

    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"


f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
assert str(f_c) == 'Fraction: 21, 18'
f_d = f_b * f_a
assert str(f_d) == 'Fraction: 6, 18'
f_e = f_a - f_b
assert str(f_e) == 'Fraction: 3, 18'
#
assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True
f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2  # True
print('OK')
