class Student:
    def __init__(self,rlno,name,course,total):
        self.rolno=rlno
        self.name=name
        self.course=course
        self.total=total
st=Student(100,"ajay","mca",300)
st1=Student(101,"ram","bca",200)
st2=Student(102,"ravi","bca",500)
st3=Student(103,"viji","bca",400)
students=[]
students.append(st)
students.append(st1)
students.append(st2)
students.append(st3)
for student in students:
    if student.course=="mca":
        print(student.name)

# highest student with highest total
total=[]
total.append(st)
total.append(st1)
total.append(st2)
total.append(st3)