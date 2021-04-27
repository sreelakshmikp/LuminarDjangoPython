# single inheritance
class Parent:
    def phone(self):
        print("phone method")
class Child(Parent):
    pass
ch=Child()
ch.phone()
print(ch)

# multilevel inheritance
class Parent:
    def m1(self):
        print("inside parent")
class Child(Parent):
    def m2(self):
        print("inside child")
class Subchild(Child):
    def m3(self):
        print("inside subchild")
sb=Subchild()
sb.m3()
sb.m2()
sb.m1()
ch=Child()
ch.m2()
ch.m1()
# ch.m3()
p=Parent()
p.m1()
# p.m2()
# p.m3()

# multiple inhertance
class Parent:
    def m1(self):
        print("inside parent")
class Child:
    def m1(self):
        print("inside child")
class Subchild(Child,Parent):
    def m3(self):
        print("inside subchild")
sb=Subchild()
sb.m3()
sb.m1()