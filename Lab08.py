'''
CLASSES
'''
'''Q1-Q6'''


class Student:
    def __init__(self, first_name, surname, student_id, email_address):
        self.__first_name = first_name.title()
        self.__surname = surname.title()
        self.__student_id = student_id
        self.__email_address = email_address
        self.__test_mark = 0
        self.__exam_mark = 0
        self.__lab_marks = []

    def __str__(self):
        return '{surname}, {first_name}: id={student_id} ({email_address})'.format(surname=self.__surname, first_name=self.__first_name, student_id=self.__student_id, email_address=self.__email_address)

    def set_test_mark(self, mark):
        if 0 <= mark <= 100:
            self.__test_mark = mark

    def get_test_mark(self):
        return self.__test_mark

    def set_exam_mark(self, mark):
        if 0 <= mark <= 100:
            self.__exam_mark = mark

    def get_exam_mark(self):
        return self.__exam_mark

    def add_lab_mark(self, mark):
        if 0 <= mark <= 100:
            self.__lab_marks.append(mark)

    def get_lab_marks(self):
        return self.__lab_marks

    def get_average_lab_mark(self):
        if len(self.get_lab_marks()) > 0:
            return round(sum(self.get_lab_marks()) / len(self.get_lab_marks()), 1)
        else:
            return 0

    def get_final_mark(self):
        lab_marks = sum(self.get_lab_marks()) * 0.1
        test_mark = self.get_test_mark() * 0.2
        exam_mark = self.get_exam_mark() * 0.4
        return lab_marks + test_mark + exam_mark

    def get_grade(self):
        if 90 <= self.get_final_mark() <= 100:
            return 'A'
        elif 75 <= self.get_final_mark() <= 89.9:
            return 'B'
        elif 50 <= self.get_final_mark() <= 74.9:
            return 'C'
        elif 40 <= self.get_final_mark() <= 49.9:
            return 'D'
        elif 30 <= self.get_final_mark() <= 39.9:
            return 'E'
        else:
            return 'F'


'''Q7-Q10'''


class SimplePolynomial:
    def __init__(self, c0=1, c1=1, c2=1):
        self.__coefficients = [c0, c1, c2]

    def __str__(self):
        d0 = self.__coefficients[0]
        d1 = self.__coefficients[1]
        d2 = self.__coefficients[2]
        if d0 > 0 and d1 > 0 and d2 > 0:
            return '{}x^2 + {}x + {}'.format(d2, d1, d0)
        elif d2 == 0:
            return '{}x + {}'.format(d1, d0)
        elif d1 == 0:
            return '{}x^2 + {}'.format(d2, d0)
        elif d0 == 0:
            return '{}x^2 + {}x'.format(d2, d1)
        else:
            return '{}x^2 + {}x + {}'.format(d2, d1, d0)

    def evaluate(self, x):
        d0 = self.__coefficients[0]
        d1 = self.__coefficients[1]
        d2 = self.__coefficients[2]
        return d2 * x ** 2 + d1 * x + d0

    def __add__(self, x):
        self.__coefficients[0] += x.__coefficients[0]
        self.__coefficients[1] += x.__coefficients[1]
        self.__coefficients[2] += x.__coefficients[2]
        return SimplePolynomial(self.__coefficients[0], self.__coefficients[1], self.__coefficients[2])
