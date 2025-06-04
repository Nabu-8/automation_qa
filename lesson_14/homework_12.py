class Student:

    def __init__(self, name, surname, age, average_grade):
        self.name = name
        self.surname = surname
        self.age = age
        self.average_grade = average_grade

    def __str__(self):
        return f'Student: {self.name} {self.surname} is {self.age} y.o., average grade: {self.average_grade} points'

    def change_average_grade(self, new_average_grade):  # метод інстанса класса
        self.average_grade = new_average_grade
        print(f'The new average grade of {self.name} {self.surname} who is {self.age} y.o. is {new_average_grade} points.')


student_1 = Student(name="Henry", surname="Smith", age=22, average_grade=99)
student_2 = Student(name="Elly", surname="Johnson", age=21, average_grade=88)
student_3 = Student(name="Riz", surname="Richards", age=23, average_grade=77)

print(student_1)
print(student_2)
print(student_3)

print("-"*80)

student_1.change_average_grade(100)
student_2.change_average_grade(55)
student_3.change_average_grade(88)