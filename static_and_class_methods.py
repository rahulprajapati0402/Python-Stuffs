class Student:
    grade = "A"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_data(self):
        print({"name": self.name, "age": self.age, "grade": self.grade})

    # Static Method can be used without object
    @staticmethod
    def check_age(age):
        if age > 18:
            print("Above 18")
        else:
            print("Below 18")

    # Class Method is used to update the class variables
    @classmethod
    def update_grade(cls, grade):
        cls.grade = grade


a = Student("Rahul", 22)
b = Student("Chirag", 28)

Student.update_grade("B")
Student.check_age(2)

a.get_data()
b.get_data()
