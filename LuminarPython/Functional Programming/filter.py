lst=[2,4,6,7,8,9]
even=list(filter(lambda num:num%2==0,lst))
print(even)

# print name starting with a
names=["akhil","harsha","anu","shirin","kavya"]
name_a=list(filter(lambda name:name[0]=="a",names))
print(name_a)

# print detail of students with mca
class Student:
    def __init__(self,rlno,name,course,total):
        self.rolno=rlno
        self.name=name
        self.course=course
        self.total=total
    def __str__(self):
        return self.name
st=Student(100,"ajay","mca",300)
st1=Student(101,"ram","bca",200)
st2=Student(102,"ravi","bca",500)
st3=Student(103,"viji","bca",400)
students=[]
students.append(st)
students.append(st1)
students.append(st2)
students.append(st3)
mca_stud=list(filter(lambda student:student.course=="mca",students))
for student in mca_stud:
    print(student)

# another method--chain method(no need of for loop and __str__)
mca_name=list(map(lambda st:st.name,list(filter(lambda student:student.course=="mca",students))))
print(mca_name)

maxmark=max(list(map(lambda st:st.total,students)))
print(maxmark)
minmark=min(list(map(lambda st:st.total,students)))
print(minmark)