#Class Example
class Student:

    #class variable
    school_name = 'ABC School'

    def __init__(self, rollno, name, course):
        self.rollno = rollno
        self.name = name
        self.course = course

    def __str__(self):
        return f'{self.rollno} ,{self.name} ,{self.course}, {self.school_name}'

s1 = Student(1, 'St1', '10')
s2 = Student(101, 'St2', '6')
s1.school_name = 'Hello'
print(s1)
print(s2)