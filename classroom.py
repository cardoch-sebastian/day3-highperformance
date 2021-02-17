from person import Person

class Student(Person):
    def __init__(self, first_name, last_name, subject_area):
        Person.__init__(self,first_name, last_name)
        self.subject_area = subject_area

    def printNameSubject(self):
        print(f"{self.first_name} {self.last_name}, {self.subject_area}")

class Teacher(Person):
    def __init__(self, first_name, last_name, course_name):
        Person.__init__(self, first_name, last_name)
        self.course_name = course_name
    
    def printNameCourse(self):
        print(f"{self.first_name} {self.last_name}, {self.course_name}")