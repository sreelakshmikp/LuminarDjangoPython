# method overloading
# method overriding
# operator overloading
# duck typing

# method overloading- same method name different no.of parameters
class Maths:
    def add(self):
        print("inside no arg method")
    def add(self,num1):
        print("inside one arg method")
    def add(self,num1,num2):
        print("inside two arg method")
math=Maths()
# work only recently implemented method
math.add(10,20)
# math.add(1) error
# math.add()  error

# method overriding
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return self.name
p=Person("ajay",25)
print(p)

# duck typing
