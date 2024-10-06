import random as rand

class SchoolEntity:

    def __init__(self, name):
        self.__name = name
        self.__id = self.generate_id()

    @staticmethod
    def generate_id():
        return f"ID-{rand.randint(1000, 9999)}"

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

class Teacher(SchoolEntity):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def get_info(self):
        return f"Teacher {self.get_name()}, Subject: {self.subject}, {self.get_id()}"

class Student(SchoolEntity):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

    def get_info(self):
        return f"Student {self.get_name()}, Grade: {self.grade}, {self.get_id()}"

class Manager:
    def __init__(self, responsibility):
        self.responsibility = responsibility

    def manage(self):
        return f"Managing: {self.responsibility}"

class Administrator(Teacher, Manager):
    def __init__(self, name, subject, responsibility):
        Teacher.__init__(self, name, subject)
        Manager.__init__(self, responsibility)

    def get_info(self):
        return f"Administrator {self.get_name()} oversees {self.responsibility} and teaches {self.subject}"

class Rosklad:
    def __init__(self):
        self.lessons = []

    def add_lesson(self, teacher, student, time_slot):
        self.lessons.append((teacher, student, time_slot))

    def display_rosklad(self):
        for teacher, student, time_slot in self.lessons:
            print(f"{time_slot}: {teacher.get_name()} teaches {teacher.subject} to {student.get_name()} (Grade {student.grade})")

teacher = Teacher("Mr. Green", "Mathematics")
student = Student("Alice", 9)
admin = Administrator("Ms. Black", "Science", "School Operations")
rosklad = Rosklad()
print(admin.manage())
rosklad.add_lesson(teacher, student, "09:00 - 10:00")
print(SchoolEntity.generate_id())
print(teacher.get_info())
print(student.get_info())
print(admin.get_info())
rosklad.display_rosklad()
