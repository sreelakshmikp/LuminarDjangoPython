class Student:
    cname="GEC"
    def set_student(self,roll,name):
        self.roll=roll
        self.name=name
    def print_student(self):
        print(self.roll)
        print(self.name)
        print(Student.cname)
obj=Student()
obj.set_student(100,"akhil")
# to print outside the class
print(obj.name)
print(obj.roll)
print(Student.cname)