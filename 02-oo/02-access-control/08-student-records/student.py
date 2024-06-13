class Student:
    def __init__(self, name):
        self.name = name
        self.__courses = dict()

    def calculate_letter_grade(self, score):
        if score >= 90:
            return "A"
        if 90 > score > 79:
            return "B"
        if 80 > score > 69:
            return "C"
        if 70 > score >=60:
            return "D"
        if score < 60:
            return "F"


    def add_course(self, course_name, score):
        score = self.calculate_letter_grade(score)
        self.__courses[course_name] = score

    def get_courses(self):
        return self.__courses