class Student:
    def __init__(self, name, student_id, major):
        self.name = name
        self.student_id = student_id
        self.major = major

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f"Major: {self.major}")
        print("-" * 25)

    def introduce(self):
        print(f"My name is {self.name} and I study {self.major}.")


student1 = Student("Ali", 123, "AI")
student2 = Student("Sara", 456, "Computer")

student1.display_info()
student1.introduce()

student2.display_info()
student2.introduce()
