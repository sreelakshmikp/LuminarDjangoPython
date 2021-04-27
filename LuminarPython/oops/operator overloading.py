class Book:
    def __init__(self,pages):
        self.pages=pages
# obj=Book(200)
# obj1=Book(100)
# print(obj+obj1)
    def __add__(self, other):
        return self.pages+other.pages
obj=Book(100)
obj1=Book(200)
print(obj+obj1)

# sub
class Book:
    def __init__(self,pages):
        self.pages=pages
    def __sub__(self, other):
        return self.pages-other.pages
obj=Book(200)
obj1=Book(900)
print(obj-obj1)

# with 3 objects
class Book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self, other):
        return Book(self.pages+other.pages)
    def __str__(self):
        return str(self.pages)
obj=Book(200)
obj1=Book(100)
obj2=Book(300)
print(obj+obj1+obj2)

