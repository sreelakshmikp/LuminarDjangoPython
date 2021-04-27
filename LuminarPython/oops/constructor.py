class Student:
    cname="GEC"
    def __init__(self,roll,name):
        self.roll=roll
        self.name=name
    def print_student(self):
        print(self.roll)
        print(self.name)
        print(Student.cname)
obj=Student(100,"akhil")
obj.print_student()