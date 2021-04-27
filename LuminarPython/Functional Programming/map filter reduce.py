# map
lst=[2,4,5,6,7]
squares=list(map(lambda num:num**2,lst))
print(squares)

# convert names to uppercase
names=["akhil","anu","harsha","shirin"]
upper=list(map(lambda name:name.upper(),names))
print(upper)

numbers=[4,5,8,9,3,2]
new_numbers=list(map(lambda num:num+1 if num>5 else num-1,numbers))
print(new_numbers)

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
upper=list(map(lambda student:student.name.upper(),students))
print(upper)
# give 50 bonus mark
bonus=list(map(lambda student:student.total+50,students))
print(bonus)