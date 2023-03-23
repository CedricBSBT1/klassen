class Teacher:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

class Students:
    def __init__(self, first_name: str, last_name: str):
        first_name = first_name
        last_name = last_name

class Course:
    def __init__(self, name: str):
        self.name = name

class Klasse:
    def __init__(self, name: str, Students: list[Student] = []):
        self.name = name
        self.student = students

class Grade:
    def __init__(self, level: int, student: Students, weight: float, course: Course, date: date):
        self.level = level
        self.student = student
        self.course = course
        self.weight = weight
        self.date = date