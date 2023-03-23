import datetime


class Teacher:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name


class Student:
    def __init__(self, first_name: str, last_name: str):
        first_name = first_name
        last_name = last_name


class Course:
    def __init__(self, name: str):
        self.name = name


class Klasse:
    def __init__(self, name: str, students: list[Student] = []):
        self.name = name
        self.students = students


class Grade:
    def __init__(self, level: int, student: Student, weight: float, course: Course, date):
        self.level = level
        self.student = student
        self.course = course
        self.weight = weight
        self.date = date


lukas = Student("Lukas", "Lang")
biologie = Course("Biologie")
mark = Grade(5, lukas, biologie, 2, datetime.date.today())
# Kommentar