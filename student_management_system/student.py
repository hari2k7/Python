class Student:
    def __init__(self,student_id,name,age,course):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course

    def to_dict(self): #json can only store dicts
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "course": self.course,
        }